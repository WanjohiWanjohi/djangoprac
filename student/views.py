from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student

# Create your views here.

def index(request):
	data = Student.objects.all()
	return HttpResponse(data)
