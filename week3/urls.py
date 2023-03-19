from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views3

urlpatterns = (
    [
        # Add path here
        path(
            route="onlinecourse2/",
            view=views3.popular_course_list_Changed,
            name="popular_course_list2",
        ),
        path(
            route="onlinecourse2/course3/<int:course3_id>/enroll/",
            view=views3.enroll_Changed,
            name="enroll2",
        ),
        path(
            route="onlinecourse2/course3/<int:course3_id>/",
            view=views3.course_details__Changed,
            name="course_details2",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
