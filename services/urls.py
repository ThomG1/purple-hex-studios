from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_services, name='services'),
    path('detail/<int:service_id>/',
         views.service_detail,
         name='service_detail'),
    path('add/', views.add_service, name='add_service'),
    path('delete/<int:service_id>/',
         views.delete_service,
         name='delete_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),
]
