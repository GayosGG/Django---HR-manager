from django.contrib import admin

from .models import *


class VacancyAdmin(admin.ModelAdmin):
    ADMIN_FIELDS = ('id', 'post', 'status', 'priority', 'description', 'hr_manager', 'show')
    list_display = ADMIN_FIELDS
    list_display_links = ('id', 'post')
    search_fields = ADMIN_FIELDS
    list_editable = ('status', 'priority', 'description', 'show')


class CandidateAdmin(admin.ModelAdmin):
    ADMIN_FIELDS = ('id', 'post', 'status', 'estimation', 'estimation', 'hr_manager', 'in_archive')
    list_display = ADMIN_FIELDS
    list_display_links = ('id', 'post')
    search_fields = ADMIN_FIELDS
    list_editable = ('status', 'in_archive')


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Candidate, CandidateAdmin)
