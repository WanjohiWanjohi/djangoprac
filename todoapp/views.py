from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import Todo
# Create your views here.

def index(request):
	todos = Todo.objects.all()
	return render(request , 'index.html', {'todos':todos})