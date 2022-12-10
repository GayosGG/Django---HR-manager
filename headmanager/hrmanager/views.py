from django.contrib.auth.decorators import login_required
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

from headmanager.serializers import VacancySerializer, CandidateSerializer
from hrmanager.models import Vacancy, Candidate


def login_test(request):
    return render(request, 'll.html')


class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('post', 'company', 'status', 'priority', 'hr_manager')


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('post', 'hr_manager')


@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
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


@login_required
@api_view(['GET'])
def vacancyList(request):
    vacancys = Vacancy.objects.all()
    serializer = VacancySerializer(vacancys, many=True)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def vacancyUpdate(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    serializer = VacancySerializer(instance=vacancy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def vacancyDelete(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    vacancy.delete()
    return Response("Вакансия удалена")


@login_required
@api_view(['GET'])
def vacancyDetail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    serializer = VacancySerializer(vacancy, many=False)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def vacancyCreate(request, **kwargs):
    serializer = VacancySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(kwargs)
    return Response(serializer.data)


#Кандидаты:

@login_required
@api_view(['GET'])
def candidateList(request):
    vacancys = Candidate.objects.all()
    serializer = CandidateSerializer(vacancys, many=True)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def candidateUpdate(request, pk):
    vacancy = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(instance=vacancy, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def candidateDelete(request, pk):
    vacancy = Candidate.objects.get(id=pk)
    vacancy.delete()
    return Response("Вакансия удалена")


@login_required
@api_view(['GET'])
def candidateDetail(request, pk):
    vacancy = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(vacancy, many=False)
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def candidateCreate(request, **kwargs):
    serializer = CandidateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(kwargs)
    return Response(serializer.data)
