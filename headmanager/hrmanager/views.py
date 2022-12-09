from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework import filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from headmanager.serializers import VacancySerializer
from hrmanager.models import Vacancy


class VacancysPage(ListView):
    model = Vacancy
    template_name = 'hrmanager/vacancys.html'
    context_object_name = 'vacancys'
    extra_context = {'title': 'Вакансии'}


def login(request):
    return render(request, 'hrmanager/login.html')


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('post', 'company', 'status', 'priority', 'hr_manager')



def delete_vacancy(request, vacancy_id):
    vacancy_item = Vacancy.objects.get(id=vacancy_id)
    vacancy_item.delete()



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/vacancy-list/',
        'Detail View': '/vacancy-detail/<str:pk>/',
        'Create': '/vacancy-create/',
        'Update': '/vacancy-update/<str:pk>/',
        'Delete': '/vacancy-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def vacancyList(request):
    vacancys = Vacancy.objects.all()
    serializer = VacancySerializer(vacancys, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def vacancyUpdate(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    serializer = VacancySerializer(instance=vacancy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def vacancyDelete(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    vacancy.delete()
    return Response("Вакансия удалена")


@api_view(['GET'])
def vacancyDetail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    serializer = VacancySerializer(vacancy, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def vacancyCreate(request, **kwargs):
    serializer = VacancySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(kwargs)
    return Response(serializer.data)
