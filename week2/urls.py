from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views2

urlpatterns = (
    [
        path(
            route="onlinecourse1/",
            view=views2.popular_course_list,
            name="popular_course_list",
        ),
        path(
            route="onlinecourse1/course2/<int:course2_id>/enroll/",
            view=views2.enroll,
            name="enroll",
        ),
        path(
            route="onlinecourse1/course2/<int:course2_id>/",
            view=views2.course_details,
            name="course_details",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
