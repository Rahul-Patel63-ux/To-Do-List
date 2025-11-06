"""
URL configuration for ToDoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import TaskListCreateView, TaskListModifyView, LoginView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskListModifyView.as_view(), name='task_modify'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/register/', RegisterView.as_view(), name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # get new access token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),     # optional: verify token
]
