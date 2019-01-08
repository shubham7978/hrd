from django.urls import path
from . import views

urlpatterns=[
 path('', views.index, name='index'),
 # ex: /jobs/5/
 path('<int:job_id>/', views.description, name='description'),
]

