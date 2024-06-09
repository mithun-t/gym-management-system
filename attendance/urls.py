from django.urls import path
from . import views

urlpatterns = [
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance_stats/', views.attendance_stats, name='attendance_stats'),
]
