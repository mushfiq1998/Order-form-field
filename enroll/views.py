from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    form = StudentRegistration()
    # Arrange form fields in custom order  
    form.order_fields(field_order=['name', 'email', 'address'])
    return render(request, 'enroll/userregistration.html',
                  {'form': form})

'''
def showformdata(request):
    form = StudentRegistration()
    # Arrange form fields in default order according to sequence 
    # as I write in forms.py.
    form.order_fields(field_order=None)
    return render(request, 'enroll/userregistration.html',
                  {'form': form})'''