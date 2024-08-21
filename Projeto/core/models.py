from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.urls import reverse

class User(AbstractUser,PermissionsMixin):
    username = models.CharField(
        db_column = 'tx_username',
        null=False,
        max_length=64,
        unique=True
    )
    password = models.CharField(
        db_column='tx_password',
        null= False,
        max_length = 104
    )
    name = models.CharField(
        db_column = 'tx_name',
        null=True,
        max_length=256
    )
    email = models.EmailField(
        db_column = 'tx_email',
        null = True,
        blank = True,
        max_length = 256
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True
    )
    is_active = models.BooleanField(
        db_column = 'cs_active',
        null = False,
        default = True
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        null= True,
        default = False
    )
    is_staff = models.BooleanField(
        db_column = 'cs_staff',
        null= True,
        default = False
    )
    is_default = models.BooleanField(
        db_column = 'cs_default',
        null= False,
        default = False
    )
    def get_absolute_url(self):
        return reverse ('user_detail', kwargs={'pk':self.id})

    def __str__ (self):
        return self.username

    class Meta:
        managed = True
        db_table = 'auth_User'







    