from django.contrib import admin
from .models import *


class DailyScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'topic', 'page', 'question', 'start', 'end']


admin.site.register(Type)
admin.site.register(Topic)
admin.site.register(Book)
admin.site.register(Part)
admin.site.register(Page)
admin.site.register(Question)
admin.site.register(DailySchedule, DailyScheduleAdmin)
