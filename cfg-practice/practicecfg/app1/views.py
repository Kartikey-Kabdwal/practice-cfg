from django.shortcuts import render

from .models import Student
from .forms import StudentData
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def student(request):
    return render(request, 'student.html')


def dashboard(request):
    return render(request, 'dashboard2.html')
