from django.contrib import admin
from appoinment.models import *
# Register your models here.

admin.site.register(appointments)
admin.site.register(patient)
admin.site.register(hospital)
admin.site.register(records)
admin.site.register(reports)