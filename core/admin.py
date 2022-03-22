from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from .models import (
    Subject, FrequentlyAskedQuestion,
    Application, Gallery, PTAManagement, PTAMeetingResolution,
    SchoolContactInfo, SchoolManagement, Tuition, About)

from ckeditor.widgets import CKEditorWidget


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Application)
admin.site.register(Gallery)
admin.site.register(PTAManagement)
admin.site.register(PTAMeetingResolution)
admin.site.register(SchoolContactInfo)
admin.site.register(SchoolManagement)
admin.site.register(Tuition)
admin.site.register(About)
