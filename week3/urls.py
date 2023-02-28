from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views3

urlpatterns = [
    # Add path here
    path(route='onlinecourse2/', view=views3.CourseListView.as_view(), name='popular_course_list2'),
    path(route='onlinecourse2/course/<int:pk>/enroll/', view=views3.Enroll.as_view(), name='enroll'),
    path(route='onlinecourse2/course/<int:pk>/', view=views3.CourseDetails.as_view(), name='course_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

