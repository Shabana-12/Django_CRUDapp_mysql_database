from django.contrib import admin
from django.urls import path
from crudapp import views
urlpatterns = [
    path('', views.create_view, name='create'),
    path('list', views.list_view, name='list'),
    path('<id>', views.detail_view, name='detail'),
    path('update/<id>', views.update_view, name='update'),
    path('delete/<id>', views.delete_view, name='delete'),
    
    
]    