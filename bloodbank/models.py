from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Condition(models.Model):
    condition_name = models.Charfield(max_length=200)
    description = models.Charfield(max_length=200)
    other_details = models.Charfield(max_length=200)

    def __str__(self):
      return self.condtion_name


class Donations(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  facility = models.Charfield(max_length=200)
  donate_date = models.DateTimeField(auto_now_add=True)
  last_donate_date = models.DateField(auto_now_add=True)
  location = models.Charfield(max_length=50)
  blood_group = models.Charfield(max_length=50)
  medical_condition = models.ForeignKey(Donors, on_delete=models.CASCADE)

  def __str__(self):
    return self.blood_group
