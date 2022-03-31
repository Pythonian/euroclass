from django.contrib import admin

from .models import Pupil, Caution


class CautionInline(admin.StackedInline):
    model = Caution
    extra = 0


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'pupil_class', 'date_of_registration']
    inlines = [CautionInline]
