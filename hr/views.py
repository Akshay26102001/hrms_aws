from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import LeaveForm

@login_required
def dashboard(request):
    emp = Employee.objects.get(user=request.user)
    context = {
        "total_employees": Employee.objects.count() if emp.role == 'Admin' else None,
        "leaves_today": Leave.objects.filter(start_date=date.today()).count(),
        "notices": Notice.objects.all().order_by('-created_at')[:5]
    }
    return render(request, 'hr/dashboard.html', context)

@login_required
def profile(request):
    emp = Employee.objects.get(user=request.user)
    return render(request, 'hr/profile.html', {"employee": emp})

@login_required
def attendance_view(request):
    emp = Employee.objects.get(user=request.user)
    data = Attendance.objects.filter(employee=emp)
    return render(request, 'hr/attendance.html', {"attendance": data})

@login_required
def leave_status(request):
    emp = Employee.objects.get(user=request.user)
    leaves = Leave.objects.filter(employee=emp)
    return render(request, 'hr/leave_status.html', {"leaves": leaves})

@login_required
def apply_leave(request):
    emp = Employee.objects.get(user=request.user)
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = emp
            leave.save()
            return redirect('leave_status')
    else:
        form = LeaveForm()
    return render(request, 'hr/leave_application.html', {'form': form})

@login_required
def notices_view(request):
    return render(request, 'hr/notices.html', {"notices": Notice.objects.all().order_by('-created_at')})