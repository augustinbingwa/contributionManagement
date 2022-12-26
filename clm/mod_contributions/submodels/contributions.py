from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from mod_settings.enums import *
from decimal import Decimal
from mod_members.models import *

class Contribution(models.Model):
    """
    Contribution model
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=200, unique=True)
    periode_type = models.IntegerField(choices=period_choice)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('20000'))])
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='%(class)s_requests_created')
    valideted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                     related_name='%(class)s_requests_validated', null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.periode_type
