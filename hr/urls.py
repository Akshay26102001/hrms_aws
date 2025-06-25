from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('leaves/', views.leave_status, name='leave_status'),
    path('notices/', views.notices_view, name='notices'),
    path('employees/', views.employee_list, name='employee_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]