from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'), #homeScreen
 path('result', views.result, name='add'), #screen2
 path('analysis', views.analysis, name='analysis') #screen3
]