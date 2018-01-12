from . import views
from django.urls import path,include,re_path

app_name = 'usr'

urlpatterns = [
    re_path(r'^$',views.robustUserhandler),
    re_path(r'^(?P<pk>\d+)/(?P<type>.+)/$',views.userViewModifyandDelete),
    re_path(r'^(?P<type>.+)/$',views.userCreate),
]


