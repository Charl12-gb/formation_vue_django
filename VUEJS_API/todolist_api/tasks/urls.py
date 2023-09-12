from django.urls import path
from .views import LoginView, UserTokenRefreshView, Logout, register_user
from .views_project import create_project, user_projects, project
from .views_tasks import create_project_task, project_tasks, task

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('token/refresh', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('logout', Logout.as_view(), name='logout'),
    path('register/', register_user, name='register_user'),

    path('create_project/', create_project, name='create_project'),
    path('user_projects/', user_projects, name='user_projects'),
    path('project/<int:project_id>/', project, name='project'),
    path('task/<int:task_id>/', task, name='task'),
    path('project_tasks/<int:project_id>/', project_tasks, name='project_tasks'),
    path('create_project_task/<int:project_id>/', create_project_task, name='create_project_task'),
]