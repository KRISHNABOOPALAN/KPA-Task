from django.db import models

class BogieChecksheet(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bogie_details = models.JSONField()
    bogie_checksheet = models.JSONField()
    bmbc_checksheet = models.JSONField()

class WheelSpec(models.Model):
    form_number = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.JSONField()
