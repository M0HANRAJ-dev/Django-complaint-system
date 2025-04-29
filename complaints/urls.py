from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_list_create, name='complaint_list'),
    path('download_csv/', views.download_complaints_csv, name='download_complaints_csv'),
]