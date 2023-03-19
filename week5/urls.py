from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views5


urlpatterns = [
    path(route='project/', view=views5.CourseListView3.as_view(), name='index'),
    path('registration/', views5.registration_request, name='registrationF'),
    path('login/', views5.login_request, name='loginF'),
    path('logout/', views5.logout_request, name='logoutF'),
    path('project/course5/<int:pk>/', views5.CourseDetailView3.as_view(), name='course_detailsF'),
    path('project/course5/<int:course5_id>/enroll/', views5.enroll5, name='enrollF'),
    path('project/course5/<int:course5_id>/submit/', views5.submit5, name='submitF'),
    path('project/course5/<int:course5_id>/submission/<int:submission5_id>/result/', views5.show_exam_result, name='show_exam_resultF'),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
