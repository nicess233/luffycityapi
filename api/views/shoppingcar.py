from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from django.db import transaction
from api import models
from api.utils.response import BaseResponse

SHOPPING_CAR = {

}

class ShopingCarView(ViewSetMixin,APIView,BaseResponse):

    def create(self,request,*args,**kwargs):
        """
        1. 接受用户选中的课程ID和价格策略ID
        2. 判断合法性
            - 课程是否存在？
            - 价格策略是否合法？
        3. 把商品和价格策略信息放入购物车 SHOPPING_CAR

        注意：用户ID=1
        """
        try:
            ret = BaseResponse()
            print(request.data)
            course_id = int(request.data.get("course_id"))
            price_id = int(request.data.get("price_id"))

            obj = models.Course.objects.filter(id=course_id).first()
            if obj:
                id_list = obj.price_policy.values_list("id")
                for price_policy_id in id_list:
                    if price_id in price_policy_id:
                        price_policy_list = obj.price_policy.values("id", "valid_period", "price")
                        choice_price_policy = models.PricePolicy.objects.filter(id=price_id).values("id", "valid_period", "price")
                        with transaction.atomic():
                            global SHOPPING_CAR
                            SHOPPING_CAR = {
                                1:{
                                    course_id: {
                                        "name": obj.name,
                                        "course_type": obj.get_course_type_display(),
                                        "brief": obj.brief,
                                        "level": obj.get_level_display(),
                                        "choice_price_policy": choice_price_policy,
                                        "price_policy": price_policy_list,
                                    }
                                }
                            }
                            ret.data = SHOPPING_CAR
                            print(SHOPPING_CAR)
                        return Response(ret.dict)
            ret.code = 401
            ret.error = "购物车数据有误"
            print(SHOPPING_CAR)
            return Response(ret.dict)
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "请传入正确的数字"
            return Response(ret.dict)

    def update(self,request,*args,**kwargs):
        try:
            ret = BaseResponse()
            print(request.data)
            course_id = int(request.data.get("course_id"))
            price_id = int(request.data.get("price_id"))

            obj = models.Course.objects.filter(id=course_id).first()
            if obj:
                id_list = obj.price_policy.values_list("id")
                for price_policy_id in id_list:
                    if price_id in price_policy_id:
                        price_policy_list = obj.price_policy.values("id", "valid_period", "price")
                        choice_price_policy = models.PricePolicy.objects.filter(id=price_id).values("id", "valid_period", "price")
                        with transaction.atomic():
                            global SHOPPING_CAR
                            SHOPPING_CAR = {
                                1:{
                                    course_id: {
                                        "name": obj.name,
                                        "course_type": obj.get_course_type_display(),
                                        "brief": obj.brief,
                                        "level": obj.get_level_display(),
                                        "choice_price_policy": choice_price_policy,
                                        "price_policy": price_policy_list,
                                    }
                                }
                            }
                            ret.data = SHOPPING_CAR
                            print(SHOPPING_CAR)
                        return Response(ret.dict)
            ret.code = 401
            ret.error = "购物车数据有误"
            print(SHOPPING_CAR)
            return Response(ret.dict)
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "请传入正确的数字"
            return Response(ret.dict)

    def distroy(self,request,*args,**kwargs):
        try:
            ret = BaseResponse()
            course_id = int(request.data.get("course_id"))
            price_id = int(request.data.get("price_id"))

            obj = models.Course.objects.filter(id=course_id).first()
            if obj:
                id_list = obj.price_policy.values_list("id")
                for price_policy_id in id_list:
                    if price_id in price_policy_id:
                        with transaction.atomic():
                            global SHOPPING_CAR
                            del SHOPPING_CAR[1][course_id]
                            print(SHOPPING_CAR)
                            ret.data = SHOPPING_CAR
                            print(SHOPPING_CAR)
                        return Response(ret.dict)
            ret.code = 401
            ret.error = "购物车数据有误"
            print(SHOPPING_CAR)
            return Response(ret.dict)
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "请传入正确的数字"
            return Response(ret.dict)