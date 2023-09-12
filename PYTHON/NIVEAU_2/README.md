Voici un guide pour créer un projet Django avec un CRUD complet, y compris les vues basées sur des templates. Nous allons créer un gestionnaire de tâches avec une interface utilisateur. Assurez-vous d'avoir Django installé avant de commencer.

**Installation de django** 

pip install Django

1. **Créer un projet :** Ouvrez votre terminal et exécutez les commandes suivantes pour créer un nouveau projet Django et accéder au dossier du projet :

   ```sh
   django-admin startproject task_manager_project
   cd task_manager_project
   ```

2. **Créer une application :** Dans le même terminal, exécutez la commande pour créer une nouvelle application à l'intérieur du projet :

   ```sh
   python manage.py startapp tasks
   ```

3. **Configurer les modèles :** Dans `tasks/models.py`, définissez le modèle pour représenter les tâches :

   ```python
   from django.db import models

   class Task(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       completed = models.BooleanField(default=False)

       def __str__(self):
           return self.title
   ```

4. **Configurer les vues :** Dans `tasks/views.py`, créez des vues pour afficher la liste des tâches, créer une nouvelle tâche, mettre à jour une tâche existante et supprimer une tâche :

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

5. **Créer les templates :** Créez un dossier `templates` dans le répertoire de votre application. À l'intérieur, créez un sous-dossier `tasks` et ajoutez les templates HTML suivants :

   - `task_list.html` : Affiche la liste des tâches et les liens pour créer, mettre à jour et supprimer des tâches.
   - `create_task.html` : Affiche le formulaire de création de tâche.
   - `update_task.html` : Affiche le formulaire de mise à jour de tâche.
   - `delete_task.html` : Affiche la confirmation de suppression de tâche.

6. **Configurer les URLs :** Dans `tasks/urls.py`, définissez les URL pour les vues créées :

   ```python
   from django.urls import path
   from .views import task_list, create_task, update_task, delete_task

   urlpatterns = [
       path('', task_list, name='task_list'),
       path('create/', create_task, name='create_task'),
       path('update/<int:task_id>/', update_task, name='update_task'),
       path('delete/<int:task_id>/', delete_task, name='delete_task'),
   ]
   ```

7. **Configurer les URLs du projet :** Dans `task_manager_project/urls.py`, ajoutez les URLs de l'application :

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('tasks/', include('tasks.urls')),
   ]
   ```

8. **Exécution :** Exécutez le serveur de développement Django en exécutant la commande :

   ```sh
   python manage.py runserver
   ```

   Vous pouvez accéder à l'interface utilisateur à l'adresse `http://127.0.0.1:8000/tasks/`. Vous pourrez alors afficher la liste des tâches, créer de nouvelles tâches, mettre à jour des tâches existantes et supprimer des tâches.

N'oubliez pas d'ajouter des styles CSS pour améliorer l'apparence de vos templates. Ce guide vous fournit une base pour développer davantage votre projet et l'adapter à vos besoins spécifiques.