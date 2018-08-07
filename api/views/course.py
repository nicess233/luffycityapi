from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination
from api import models
from api import serialize
from api.utils.response import BaseResponse

class DegreeCoursesTeacherView(APIView):
    '''
    查看所有学位课并打印学位课名称以及授课老师
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            page = PageNumberPagination()
            teacher_list = page.paginate_queryset(queryset,request,self)
            ser = serialize.TeacherSerializer(instance=teacher_list,many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = "获取数据失败"
        return Response(ret.dict)

class DegreeCoursesScholarshipView(APIView):
    '''
    查看所有学位课并打印学位课名称以及学位课的奖学金
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            page = PageNumberPagination()
            scholarship_list = page.paginate_queryset(queryset, request, self)
            ser = serialize.ScholarshipSerializer(instance=scholarship_list, many=True)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

class CoursesView(APIView):
    '''
    c.展示所有的专题课
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            queryset = models.Course.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset,request,self)
            ser = serialize.CourseSerializer(instance=course_list,many=True)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)
class DegreeCourseModelNameView(APIView):
    '''
    查看id=1的学位课对应的所有模块名称
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            obj = models.DegreeCourse.objects.filter(pk=1).first()
            ser = serialize.DegreeCourseModelNameSerializer(obj)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)

class CourseDetailViews(APIView):
    '''
    获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            obj = models.Course.objects.filter(pk=1).first()
            ser = serialize.CourseDetailSeriaizer(instance=obj)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)

class CourseOftenAskedQuestionViews(APIView):
    '''
    获取id = 1的专题课，并打印该课程相关的所有常见问题
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            obj = models.Course.objects.filter(pk=1).first()
            ser = serialize.CourseOftenAskedQuestionSerializer(instance=obj)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)

class CourseOutlineView(APIView):
    '''
    获取id = 1的专题课，并打印该课程相关的课程大纲
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            obj = models.Course.objects.filter(pk=1).first()
            ser = serialize.CourseOutlineSerializer(instance=obj)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)


class CourseChapterView(APIView):
    '''
    获取id = 1的专题课，并打印该课程相关的所有章节
    '''
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            obj = models.Course.objects.filter(pk=1).first()
            ser = serialize.CourseChapterSerializer(instance=obj)
            ret.data = ser.data
        except Exception as e:
            print(e)
            ret.code = 500
            ret.error = "或取数据失败"
        return Response(ret.dict)