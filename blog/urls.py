from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')

]
