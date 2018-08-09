import redis
import json

from django.conf import settings
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.versioning import URLPathVersioning

from api import models
from api.utils.response import BaseResponse


CONN = redis.Redis(host="192.168.11.122",port=6379)
USER_ID = 1

class ShopingCarView(ViewSetMixin,APIView,BaseResponse):

    def list(self,request,*args,**kwargs):
        '''
        获取购物车详情
        :param
        :param args:
        :param kwargs:
        :return:包含状态码，数据和错误信息的字典
        '''
        ret = BaseResponse()
        try:
            shopping_car_course_list = []
            pattern = settings.LUFFYCITY_SHOPPING_CAR % (USER_ID, "*")
            user_key_list = CONN.keys(pattern)
            for key in user_key_list:
                temp = {
                    "id":CONN.hget(key, "id").decode("utf8"),
                    "name":CONN.hget(key, "name").decode("utf8"),
                    "img":CONN.hget(key, "img").decode("utf8"),
                    "default_price_id":CONN.hget(key, 'default_price_id').decode('utf-8'),
                    "price_policy_dict":json.loads(CONN.hget(key, "price_policy_dict").decode("utf8"))
                }
                shopping_car_course_list.append(temp)
            ret.data = shopping_car_course_list
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "获取数据失败"

        return Response(ret.dict)

    def create(self,request,*args,**kwargs):
        '''
        购物车添加课程
        :param request:课程id和价格策略id
        :param args:
        :param kwargs:
        :return: 状态码，数据，错误信息
        '''
        ret = BaseResponse()
        try:
            course_id = request.data.get("course_id")
            policy_id = request.data.get("price_id")
            course_obj = models.Course.objects.filter(id=course_id).first()
            if not course_obj:
                ret.code = 404
                ret.error = "课程不存在"
                return Response(ret.dict)
            price_policy_queryset = course_obj.price_policy.all()
            price_policy_dict = {}
            for item in price_policy_queryset:
                temp = {
                    "id":item.id,
                    "price":item.price,
                    "valid_period":item.valid_period,
                    "valid_period_display":item.get_valid_period_display()
                }
                price_policy_dict[item.id] = temp
            if policy_id not in price_policy_dict:
                ret.code = 404
                ret.error = "价格不存在"
                return Response(ret,dict)

            pattern = settings.LUFFYCITY_SHOPPING_CAR % (USER_ID,"*")
            keys = CONN.keys(pattern)
            if keys and len(keys) >= 1000:
                ret.code = 501
                ret.error = "购物车内的商品已达到最大数量！！！"
                return Response(ret.data)
            key = settings.LUFFYCITY_SHOPPING_CAR % (USER_ID, course_id)
            CONN.hset(key, "id", course_id)
            CONN.hset(key, "name", course_obj.name)
            CONN.hset(key, "img", course_obj.course_img)
            CONN.hset(key, "default_price_id", policy_id)
            CONN.hset(key, "price_policy_dict", json.dumps(price_policy_dict))

            CONN.expire(key, 60*60*24) # 设置在24小时后在内存中清除这条记录
        except Exception as e:
            print(e)
            ret.code = 505
            ret.error = "获取数据失败"
        return Response(ret.dict)


    def destroy(self,request,*args,**kwargs):
        '''
        删除购物车中的课程
        :param request:
        :param args:
        :param kwargs:
        :return: 将是否删除的结果返回
        '''

        ret = BaseResponse()
        try:
            course_id = request.GET.get("course_id")
            key = settings.LUFFYCITY_SHOPPING_CAR % (USER_ID,course_id)
            CONN.delete(key) # CONN.hdel删除的是和CONN.hset相对应的值
            ret.data = '删除成功'
        except Exception as e:
            print(e)
            ret.code = 404
            ret.error = "删除失败"
        return Response(ret.dict)


    def update(self,request,*args,**kwargs):
        '''
        修改购物车的课程
        :param request:
        :param args:
        :param kwargs:
        :return:将修改的结果返回
        '''
        ret = BaseResponse()
        try:
            course_id = request.data.get("course_id")
            price_id = str(request.data.get("price_id")) if request.data.get("price_id") else None
            key = settings.LUFFYCITY_SHOPPING_CAR % (USER_ID, course_id)
            if not CONN.exists(key): # exists判断redis中是否有这个键
                ret.code = 404
                ret.error = "课程不存在"
            price_policy_dict = json.loads(CONN.hget(key, "price_policy_dict").decode("utf8"))
            if price_id not in price_policy_dict:
                ret.code = 405
                ret.error = "价格策略不存在"
            CONN.hset(key, "default_price_dict", price_id)
            CONN.expire(key, 5)
            ret.data = "购物车课程修改成功"
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "数据删除失败"
        return Response(ret.data)


