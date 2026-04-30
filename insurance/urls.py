from django.urls import path
from . import views

app_name = 'insurance'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.entry_list, name='entry_list'),
    path('new/', views.entry_create, name='entry_create'),
    path('<int:pk>/', views.entry_detail, name='entry_detail'),
    path('<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('<int:pk>/delete/', views.entry_delete, name='entry_delete'),
]