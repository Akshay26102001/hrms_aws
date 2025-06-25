from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Employee, Leave, Payroll
from datetime import date
from django.db.models import Sum


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'hr/employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hr/add_employee.html', {'form': form})


def dashboard(request):
    context = {
        "total_employees": Employee.objects.count(),
        "leaves_today": Leave.objects.filter(start_date=date.today()).count(),
        "pending_requests": Leave.objects.filter(status='Pending').count(),
        "total_salary": Payroll.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
    }
    return render(request, 'hr/dashboard.html', context)