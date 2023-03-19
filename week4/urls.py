from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views4

urlpatterns = (
    [
        path(
            route="onlinecourse3/course4/<int:pk>/enroll/",
            view=views4.EnrollView2.as_view(),
            name="enroll3",
        ),
        path(
            route="onlinecourse3/",
            view=views4.CourseListView2.as_view(),
            name="popular_course_list3",
        ),
        path(
            route="onlinecourse3/course4/<int:pk>/",
            view=views4.CourseDetailsView2.as_view(),
            name="course_details3",
        ),
        # Authentication related urls
        path("registration/", views4.registration_request, name="registration3"),
        path("login/", views4.login_request, name="login3"),
        path("logout/", views4.logout_request, name="logout3"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
