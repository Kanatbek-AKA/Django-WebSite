from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views5

urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='week5/project/', view=views5.CourseListView3.as_view(), name='index'),
    # 
    path('registration/', views5.registration_request, name='registration'),
    path('login/', views5.login_request, name='login'),
    path('logout/', views5.logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('week5/project/course/<int:pk>/', views5.CourseDetailView3.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('week5/project/course/<int:course_id>/enroll/', views5.enroll, name='enroll'),

    # <HINT> Create a route for submit view
    # path('onlinecourse/course/<int:course_id>/', views.submit, name='submit'),
    # <HINT> Create a route for show_exam_result view
    # path('onlinecourse/course/<int:course_id>/', views.show_exam_result, name='show_exam_result'),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
