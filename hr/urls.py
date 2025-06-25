from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
