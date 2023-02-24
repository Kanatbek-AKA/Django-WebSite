from django.urls import include, path, re_path  # regex_path
from example import views

urlpatterns = [
    re_path(r'^$', views.HomePageView.as_view(), name='home'),  # URL has been named as home
    re_path(r'^week1/$', views.Week1PageView.as_view(), name='week1'), 
    re_path(r'^week2/$', views.Week2PageView.as_view(), name='week2'), 
    re_path(r'^week3/$', views.Week3PageView.as_view(), name='week3'), 
    re_path(r'^week4/$', views.Week4PageView.as_view(), name='week4'), 
    re_path(r'^week5/$', views.Week5PageView.as_view(), name='week5'), 
    # Hands-on Labs
    re_path(r'^data/$', views.DataPageView.as_view(), name='data'),
    
    # Admin page
]
