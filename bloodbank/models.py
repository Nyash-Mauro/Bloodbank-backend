from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Condition(models.Model):
    condition_name = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    other_details = models.CharField(max_length=200,null=True)

    def __str__(self):
      return self.condtion_name
      
class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)
    phone_number = models.IntegerField(unique=True)
    location = models.CharField(max_length=50)
    weight = models.IntegerField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email

    def save_profile(self):
        self.save()

    def email_update(self, email):
        self.email = email
        self.save_profile()

    def delete_profile(self):
        self.delete()


class Donations(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  facility = models.CharField(max_length=200)
  donate_date = models.DateTimeField(auto_now_add=True)
  last_donate_date = models.DateField(auto_now_add=True)
  location = models.CharField(max_length=50)
  blood_group = models.CharField(max_length=50)
  medical_condition = models.ForeignKey(Condition, on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.blood_group

class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)
    phone_number = models.IntegerField(unique=True)
    location = models.CharField(max_length=50)
    weight = models.IntegerField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email

    def save_profile(self):
        self.save()

    def email_update(self, email):
        self.email = email
        self.save_profile()

    def delete_profile(self):
        self.delete()

  
class Blood_stock(models.Model):
    blood_type = models.CharField(max_length=3)
    hospital_name = models.CharField(max_length=50)
    blood_volume = models.FloatField()

    def __str__(self):
        return self.hospital_name

    def save_bloodstock(self):
        self.save()

    def blood_volume_update(self, blood_volume):
        self.blood_volume = blood_volume
        self.save_bloodstock()

    def delete_stock(self):
        self.delete()
