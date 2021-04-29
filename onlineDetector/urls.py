from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('result', views.result, name='add'),
 path('analysis', views.analysis, name='analysis')
]