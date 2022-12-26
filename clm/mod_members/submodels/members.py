from django.db import models
from mod_settings.enums import *

class Member(models.Model):
    """
    Member model
    """
    registration_number = models.CharField(max_length=20,unique=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    kind_identity = models.IntegerField(choices=identity_choice, default=0 , verbose_name="kind of identity")
    identity_number = models.CharField(max_length=50, unique=True)
    identity_delivery_date = models.DateField(blank=True, null=True)
    identity_delivery_location = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50,choices=choice_of_nationality)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return f"{self.registration_number} {self.first_name} {self.last_name}"
