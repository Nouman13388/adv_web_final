from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resource/create/', views.resource_create, name='resource_create'),
    path('resource/<int:pk>/update/', views.resource_update, name='resource_update'),
    path('resource/<int:pk>/delete/', views.resource_delete, name='resource_delete'),
]
