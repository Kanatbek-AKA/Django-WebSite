from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views4

urlpatterns = [
    
    path(route='week4/onlinecourse3/course/<int:pk>/enroll/', view=views4.EnrollView2.as_view(), name='enroll'),
    path(route='week4/onlinecourse3/', view=views4.CourseListView2.as_view(), name='popular_course_list3'),
    path(route='week4/onlinecourse3/course/<int:pk>/', view=views4.CourseDetailsView2.as_view(), name='course_details'),
    # Authentication related urls
    path('registration/', views4.registration_request, name='registration'),
    path('login/', views4.login_request, name='login'),
    path('logout/', views4.logout_request, name='logout'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

