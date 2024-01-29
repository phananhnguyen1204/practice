from django.shortcuts import render
from employees.models import Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def employee_detail(request, pk):
  employee = get_object_or_404(Employee, pk=pk)
  context = {
    'employee' : employee
  }
  return render(request, 'employee_detail.html', context)