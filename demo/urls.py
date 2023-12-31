from . import views

from django.urls import path

app_name = 'demo'

urlpatterns = [
    path(route='', view=views.index, name='index'),
]
