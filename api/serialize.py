from api import models
from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    teacher = serializers.SerializerMethodField()
    def get_teacher(self,obj):
        teacher_list = obj.teachers.all()
        return [ {"id":i.id, "name":i.name} for i in teacher_list]

class ScholarshipSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    scholarship = serializers.SerializerMethodField()
    def get_scholarship(self,obj):
        lis = obj.scholarship_set.all()
        return [ {"id":i.id, "time_percent":i.time_percent,"value":i.value} for i in lis]

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class DegreeCourseModelNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    degree_course = serializers.SerializerMethodField()
    def get_degree_course(self,obj):
        lis = obj.course_set.all()
        return [{"id":i.id,"name":i.name} for i in lis]

class CourseDetailSeriaizer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.CharField(source="get_level_display")
    why_study = serializers.CharField(source="coursedetail.why_study")
    what_to_study_brief = serializers.CharField(source="coursedetail.what_to_study_brief")
    recommend_courses = serializers.SerializerMethodField()
    def get_recommend_courses(self,obj):
        lis = obj.coursedetail.recommend_courses.all()
        return [{"id":i.id,"name":i.name} for i in lis]

class CourseOftenAskedQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    question = serializers.SerializerMethodField()
    def get_question(self,obj):
        lis = obj.asked_question.all()
        return [{"question":i.question,"answer":i.answer} for i in lis]

class CourseOutlineSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    course_outline = serializers.SerializerMethodField()
    def get_course_outline(self,obj):
        lis = obj.coursedetail.courseoutline_set.all()
        return [{"title":i.title,"content":i.content} for i in lis]

class CourseChapterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    course_chapter = serializers.SerializerMethodField()
    def get_course_chapter(self,obj):
        lis = obj.coursechapters.all()
        return [{"chapter":i.chapter, "name":i.name, "summary":i.summary, "pub_date":i.pub_date} for i in lis]