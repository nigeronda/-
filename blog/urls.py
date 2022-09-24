from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable, name='timetable'),
    path('VIOL', views.VIOL, name='VIOL'),
    path('update', views.update_timetable, name='update_timetable'),
    path('create', views.create_timetable, name='create_timetable'),
]