from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark-as-done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark-as-un-done/<int:pk>/', views.mark_as_un_done, name='mark_as_un_done')
]
