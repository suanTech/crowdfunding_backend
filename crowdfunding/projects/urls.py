from django.urls import path, include
from . import views

urlpatterns = [
  path('projects/', views.ProjectList.as_view()),
  path('projects/<int:pk>/', views.ProjectDetail.as_view())
]