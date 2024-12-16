from django.contrib import admin
from . models import Facilities, Teacher, Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display=('name','email','child_name','child_age','message')
admin.site.register(Facilities)
admin.site.register(Teacher)
admin.site.register(Appointment, AppointmentAdmin)