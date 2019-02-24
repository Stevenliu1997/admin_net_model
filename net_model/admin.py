from django.contrib import admin

# Register your models here.

from net_model import models

admin.site.register(models.CSV)
admin.site.register(models.PatientInfo)
admin.site.register(models.DoctorUser)
admin.site.register(models.PatientRecord)

