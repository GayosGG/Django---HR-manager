from rest_framework.serializers import ModelSerializer

from hrmanager.models import Vacancy, Candidate


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
