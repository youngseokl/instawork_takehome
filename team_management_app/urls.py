from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.AddMember, name='add-member'),
    path('edit/<int:pk>', views.EditMember, name='edit-member'),
    path('delete/<int:pk>', views.DeleteMember, name='delete-member'),
]