from django.conf.urls import url
from testcase import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
)
