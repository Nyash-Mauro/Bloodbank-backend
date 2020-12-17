from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
    # medical_condition = models.ForeignKey(Medical_Condition, on_delete=models.CASCADE,null=True)
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
    # donations = models.ForeignKey(Donations, on_delete=models.CASCADE,null= True)
    blood_type = models.CharField(max_length=3)
    hospital_name = models.CharField(max_length=50)
    blood_volume = models.FloatField()

    def __str__(self):
        return self.blood_type

    def save_bloodstock(self):
        self.save()

    def blood_volume_update(self, blood_volume):
        self.blood_volume = blood_volume
        self.save_bloodstock()

    def delete_stock(self):
        self.delete()












