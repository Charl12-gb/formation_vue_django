It's simple django
Just remember 4 things: 
1. Models => they allow you to create entities
2. Functions => allow you to manage the entities you've created
3. Routes => Allow you to redirect your application.
4. Views => To create interfaces where users can simply click and see the list, add information, update or perform other operations.

Here's a guide to creating a Django project with a full CRUD, including template-based views. We're going to create a task manager with a user interface. Make sure you have Django installed before you start.

**django installation 

pip install Django

1. **Create a project:** Open your terminal and run the following commands to create a new Django project and access the project folder:

   ```sh
   django-admin startproject task_manager_project
   cd task_manager_project
   ```

2. **Create an application:** In the same terminal, run the command to create a new application inside the project:

   ```sh
   python manage.py startapp tasks
   ```

3. **Configure models:** In `tasks/models.py`, define the model to represent the tasks:

   ```python
   from django.db import models

   class Task(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       completed = models.BooleanField(default=False)

       def __str__(self):
           return self.title
   ```

4. **Configure views:** In `tasks/views.py`, create views to display the task list, create a new task, update an existing task and delete a task:

   ```python
   from django.shortcuts import render, redirect
   from .models import Task

   def task_list(request):
       tasks = Task.objects.all()
       return render(request, 'tasks/task_list.html', {'tasks': tasks})

   def create_task(request):
       if request.method == 'POST':
           title = request.POST['title']
           description = request.POST['description']
           Task.objects.create(title=title, description=description)
           return redirect('task_list')
       return render(request, 'tasks/create_task.html')

   def update_task(request, task_id):
       task = Task.objects.get(pk=task_id)
       if request.method == 'POST':
           task.title = request.POST['title']
           task.description = request.POST['description']
           task.save()
           return redirect('task_list')
       return render(request, 'tasks/update_task.html', {'task': task})

   def delete_task(request, task_id):
       task = Task.objects.get(pk=task_id)
       if request.method == 'POST':
           task.delete()
           return redirect('task_list')
       return render(request, 'tasks/delete_task.html', {'task': task})
   ```

5. **Create a `templates` folder in your application directory. Inside, create a `tasks` subfolder and add the following HTML templates:

   - `task_list.html`: Displays the task list and links for creating, updating and deleting tasks.
   - `create_task.html`: Displays the task creation form.
   - update_task.html`: Displays the task update form.
   - `delete_task.html`: Displays the task deletion confirmation.

6. **Configure URLs:** In `tasks/urls.py`, define the URLs for the views created:

   ``python
   from django.urls import path
   from .views import task_list, create_task, update_task, delete_task

   urlpatterns = [
       path('', task_list, name='task_list'),
       path('create/', create_task, name='create_task'),
       path('update/<int:task_id>/', update_task, name='update_task'),
       path('delete/<int:task_id>/', delete_task, name='delete_task'),
   ]
   ```

7. **Configure project URLs:** In `task_manager_project/urls.py`, add the application URLs:

   python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('tasks/', include('tasks.urls')),
   ]
   ```

8. **Run:** Run the Django development server by executing the command :

   ```sh
   python manage.py runserver
   ```

   You can access the user interface at `http://127.0.0.1:8000/tasks/`. Here you can view the list of tasks, create new tasks, update existing tasks and delete tasks.