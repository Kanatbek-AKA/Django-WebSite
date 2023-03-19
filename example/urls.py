from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from example import views
from week1 import views1
from week2 import views2
from week3 import views3
from week4 import views4
from week5 import views5

# app_name = 'example'
urlpatterns = (
    [
        path(
            route="", view=views.HomePageView.as_view(), name="home"
        ),  # URL has been named as home
        path(route="week1/", view=views.Week1PageView.as_view(), name="week1"),
        path(route="week2/", view=views.Week2PageView.as_view(), name="week2"),
        path(route="week3/", view=views.Week3PageView.as_view(), name="week3"),
        path(route="week4/", view=views.Week4PageView.as_view(), name="week4"),
        path(route="week5/", view=views.Week5PageView.as_view(), name="week5"),
        # Hands-on Labs
        # Week 1
        path(route="week1/handson/", view=views1.index, name="lab1"),
        path(route="week1/handson/exercise1/", view=views1.get_date, name="date"),
        # Week 2
        path(
            "week2/handson2/", include(("week2.urls", "week2"), namespace="lab2")
        ),  # giving namespace
        #  Week 3
        path("week3/handson3/", include(("week3.urls", "week3"), namespace="lab3")),
        # Week 4
        path("week4/handson4/", include(("week4.urls", "week4"), namespace="lab4")),
        # Week 5
        path("week5/handson5/", include(("week5.urls", "week5"), namespace="lab5")),
        #
        # re_path(r'^registration/$', views.registration_request, name='registration'),
        # re_path(r'^login/$', views.login_request, name='login'),
        # re_path(r'^logout/$', views.logout_request, name='logout'),
        # Admin page
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
