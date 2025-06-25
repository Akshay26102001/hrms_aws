from django.contrib import admin
from django.urls import path, include
from hr import views as hr_views
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hr.urls')),
    path('', hr_views.employee_list, name='employee_list'),
    path('add/', hr_views.add_employee, name='add_employee'),
    path('login/', auth_views.LoginView.as_view(template_name='hr/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='hr/login.html')),

]
