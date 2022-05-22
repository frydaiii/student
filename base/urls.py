from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_list, name='students_list'),
    path('students/<int:student_id>', views.student_detail, name='student')
]