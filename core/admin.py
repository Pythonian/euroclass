from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import (
    Subject, FrequentlyAskedQuestion,
    Application, Picture, PTAManagement, PTAMeetingResolution,
    SchoolContactInfo, SchoolManagement, Tuition, About)


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(PTAManagement)
class PTAManagementAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role']


@admin.register(SchoolManagement)
class SchoolManagementAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'title']


@admin.register(PTAMeetingResolution)
class PTAMeetingResolutionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Application)
admin.site.register(Picture)
admin.site.register(SchoolContactInfo)
admin.site.register(Tuition)
admin.site.register(About)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

admin.site.site_header = 'Euroclass Admin'
admin.site.index_title = 'Content Admin'
admin.site.site_title = 'Euroclass administration'
