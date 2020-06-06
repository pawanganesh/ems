from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

# Create your views here.
def employee_form(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance=employee)
        context = {'form': form}
        return render(request, 'employee/employee_form.html', context)
    else:
        if id == 0:
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,('Employee Registered Successfully'))
                return redirect('employee_list')
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
    
    return redirect('employee_list')

def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee/employee_list.html', context)

def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    messages.success(request,('Employee Deleted Successfully'))
    return redirect('employee_list')

def view_employee(request, id):
    employee = Employee.objects.get(pk = id)
    context = {'employee': employee}
    return render(request, 'employee/view_employee.html',context)
