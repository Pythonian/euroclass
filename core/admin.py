from django.contrib import admin

from .models import (
    Subject, FrequentlyAskedQuestion,
    Application, Gallery, PTAManagement, PTAMeetingResolution,
    SchoolContactInfo, SchoolManagement, Tuition, About, Legal)


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
admin.site.register(Legal)
