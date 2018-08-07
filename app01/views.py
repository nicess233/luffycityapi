from django.shortcuts import render,HttpResponse

# Create your views here.

from api import models

def index(request):
    # a. 查看所有学位课并打印学位课名称以及授课老师
    # obj_list = models.DegreeCourse.objects.all()
    # for item in obj_list:
    #     for i in item.teachers.all():
    #         print(item.name,i.name)

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    # obj_list = models.DegreeCourse.objects.all()
    # for item in obj_list:
    #     for i in item.scholarship_set.all():
    #         print(i.value)

    # c.展示所有的专题课
    # obj_list = models.Course.objects.filter(degree_course__isnull=True).all()
    # for item in obj_list:
    #     print(item.name)

    # d. 查看id=1的学位课对应的所有模块名称
    # obj = models.DegreeCourse.objects.filter(id=1).first()
    # for i in obj.course_set.all():
    #     print(i.name)

    # e. 获取id=1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    # obj = models.Course.objects.filter(id=1,degree_course__isnull=True).first()
    # level = obj.get_level_display()
    # print(obj.name,level,obj.coursedetail.why_study,obj.coursedetail.what_to_study_brief,obj.coursedetail.recommend_courses.all())

    # f. 获取id=1的专题课，并打印该课程相关的所有常见问题
    # obj = models.Course.objects.filter(id=1,degree_course__isnull=True).first()
    # for item in obj.asked_question.all():
    #     print(item)

    # g. 获取id=1的专题课，并打印该课程相关的课程大纲
    #obj = models.Course.objects.filter(id=1, degree_course__isnull=True).first()
    # obj1 = models.Course.objects.filter(id=1, degree_course__isnull=True).values_list("coursedetail__courseoutline__content")
    # print(obj,obj1)

    # h. 获取id=1的专题课，并打印该课程相关的所有章节
    # obj = models.Course.objects.filter(id=1, degree_course__isnull=True).first()
    # print(obj.coursechapters.all())

    # i. 获取id=1的专题课，并打印该课程相关的所有课时
    # obj = models.Course.objects.filter(id=1, degree_course__isnull=True).first()
    # obj2 = obj.coursechapters.all()
    # print(obj)
    # for item in obj2:
    #     print(item.name)
    #     for i in item.coursesections.all():
    #         print(i.name)

    # j.  获取id=1的专题课，并打印该课程相关的所有的价格策略
    obj = models.Course.objects.filter(id=1, degree_course__isnull=True).first()
    print(obj.price_policy.all())

    return HttpResponse('ok')