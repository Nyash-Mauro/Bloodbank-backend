from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from datetime import *
# from __future__ import unicode_literals
from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password=password, **extra_fields)

class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  DONOR = 1
  RECIPIENT = 2
  ADMIN = 3
  ROLE_CHOICES = (
      (DONOR, 'donor'),
      (RECIPIENT, 'recipient'),
      (ADMIN, 'admin'),
  )
  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True,default= None)
  def __str__(self):
      return self.get_id_display()
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True,blank=True)
    is_admin = models.BooleanField( default=False)
    is_staff = models.BooleanField( default=False)

    is_active = models.BooleanField(_('active'), default=False)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role',default=None)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Condition(models.Model):
    condition_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    other_details = models.CharField(max_length=200)

    def __str__(self):
      return self.condtion_name
      
class Donations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facility = models.CharField(max_length=200)
    donate_date = models.DateTimeField(auto_now_add=True)
    last_donate_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    medical_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

    def __str__(self):
        return self.blood_group

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='user')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,null=True)
    age = models.IntegerField(null=True, blank=False)
    gender = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)
    phone_number = models.IntegerField(unique=True)
    location = models.CharField(max_length=50)
    weight = models.IntegerField(null=True, blank=False)
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

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.hospital_name

class BloodStock(models.Model):
    # hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE,primary_key=True,related_name='hospital',default=None)
    hospital = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hospital',default=None)
    donations = models.ForeignKey(Donations, on_delete=models.CASCADE,null= True)
    blood_type = models.CharField(max_length=3)
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
