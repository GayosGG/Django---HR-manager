from django.urls import path, re_path
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('vacancy-list', vacancyList, name="vacancy-list"),
    path('vacancy-detail/<str:pk>/', vacancyDetail, name="vacancy-detail"),
    path('vacancy-create/', vacancyCreate, name="vacancy-create"),
    path('vacancy-update/<str:pk>/', vacancyUpdate, name="vacancy-update"),
    path('vacancy-delete/<str:pk>/', vacancyDelete, name="vacancy-delete"),

    path('candidate-list', candidateList, name="candidate-list"),
    path('candidate-detail/<str:pk>/', candidateDetail, name="candidate-detail"),
    path('candidate-create/', candidateCreate, name="candidate-create"),
    path('candidate-update/<str:pk>/', candidateUpdate, name="candidate-update"),
    path('candidate-delete/<str:pk>/', candidateDelete, name="candidate-delete"),
]
