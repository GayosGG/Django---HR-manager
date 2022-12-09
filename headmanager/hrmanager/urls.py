from django.urls import path, re_path
from django.urls import include, path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('', apiOverview, name="api-overview"),
    path('vacancy-list', vacancyList, name="vacancy-list"),
    path('vacancy-detail/<str:pk>/', vacancyDetail, name="vacancy-detail"),
    path('vacancy-create/', vacancyCreate, name="vacancy-create"),

    path('vacancy-update/<str:pk>/', vacancyUpdate, name="vacancy-update"),
    path('vacancy-delete/<str:pk>/', vacancyDelete, name="vacancy-delete"),
]
