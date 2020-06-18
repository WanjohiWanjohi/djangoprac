from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from todoapp.models import Todo
# Create your views here.

def index(request):
	if request.method == 'POST':
		new_todo = request.POST['todo']

		if not new_todo or len(new_todo) < 3:
			return redirect('index')
		todo = Todo()
		todo.todo = new_todo
		todo.save()
		return redirect('index')

	todos = Todo.objects.all()
	return render(request , 'index.html', {'todos':todos})

def delete(request , todo_id):

	if request.method == 'POST':
		if request.POST.get('delete'):
			todo = get_object_or_404(Todo , pk=todo_id)
			todo.delete()
			return redirect('index')

		if request.POST.get('complete'):
			todo = get_object_or_404(Todo , pk=todo_id)
			if todo.is_complete == True:
				todo.is_complete = False
			else:
				todo.is_complete = True
				
			todo.save()
			return redirect('index')

		if request.POST.get('update'):
			return render(request , 'update.html' , {'todo_id': todo_id})


def update(request , todo_id):
	todo = get_object_or_404(Todo , pk=todo_id)
	todo.todo = request.POST['todo']
	todo.save()
	return redirect('index')