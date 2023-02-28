from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from . import views1

urlpatterns = [
    path(route='', view=views1.index, name='app1'),
    path(route='app1/', view=views1.get_date, name='date'),

]
