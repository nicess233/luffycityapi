from django.conf.urls import url
from api.views import course

urlpatterns = [
    url(r"a/$",course.DegreeCoursesTeacherView.as_view()),
    url(r"b/$",course.DegreeCoursesScholarshipView.as_view()),
    url(r"c/$",course.CoursesView.as_view()),
    url(r"d/$",course.DegreeCourseModelNameView.as_view()),
    url(r"e/$",course.CourseDetailViews.as_view()),
    url(r"f/$",course.CourseOftenAskedQuestionViews.as_view()),
    url(r"g/$",course.CourseOutlineView.as_view()),
    url(r"h/$",course.CourseChapterView.as_view()),
]

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'course', views.CourseViewSet)
# router.register(r'coursedetail', views.CourseViewSet)
# urlpatterns += router.urls