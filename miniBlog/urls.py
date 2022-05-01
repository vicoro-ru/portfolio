from django.urls import path
from . import views

app_name = 'miniBlog'

urlpatterns = [
    path('', views.Blog, name='Blog'),
    path('<int:blog_id>/', views.Detail, name='detail'),
]