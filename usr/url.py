from . import views
from django.urls import path,include,re_path

app_name = 'usr'

urlpatterns = [
    re_path(r'^$',views.index, name='index'),

]