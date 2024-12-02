from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm, Task
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    
    context = {
        'title' : 'Home'
    }
    return render(request, 'home.html', context)

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(initial={'user':request.user})
    context = {
        'title' : 'Add Task',
        'form' : form
    }
    return render(request, 'add_task.html', context)


@login_required
def view_task(request):    
    task = Task.objects.filter(user = request.user)
    context = {
        'title': 'View Task',
        'tasks' : task  
    }
    return render(request, 'view_task.html', context)


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid():
            form.save()  
            return redirect('view_task')  
    else:
        form = TaskForm(instance=task)  
    
    context = {
        'title': 'Update Task',
        'form': form
    }
    return render(request, 'add_task.html', context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  
    task.delete()  
    return redirect('view_task') 


@login_required
def view_task(request):    
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    uncompleted_tasks = Task.objects.filter(user=request.user, completed=False)
    context = {
        'title': 'View Tasks',
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks  
    }
    return render(request, 'view_task.html', context)




        
        
    