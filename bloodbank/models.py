from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.


class Recipients(models.Model):
    medical_facility = models.CharField(max_length=200)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    location = models.ForeignKey(User,on_delete = models.CASCADE)
    blood_volume = models.IntegerField(null=True)

    def __str__(self):
      return self.medical_facility

    def create_recipient(self):
        self.save()

    def delete_recipient(self):
        self.delete()