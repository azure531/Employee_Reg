from django.shortcuts import render, redirect
# from django import forms
# from forms import EmployeeForm
from .models import Employee
from django.template import loader

# Create your views here.

# Create Employee...

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')
    
# Retrieve Employees...

def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )
    

# Update Employees...

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)
  

# Delete Employees...

def remove_emp(request,pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)
    
