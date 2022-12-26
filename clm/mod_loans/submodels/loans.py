from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from mod_settings.enums import *
from mod_members.models import Member
from mod_settings.models import GlobalVariables
from decimal import Decimal


class Loan(models.Model):
    """
    Loan model
    """
    rate_obj = GlobalVariables.objects.filter(group='INTERESTRATE')
    rate_value_choice = {}
    for rate_list in rate_obj:
        rate_value_choice[rate_list.key] = rate_list.value
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    description = models.CharField(max_length=200, unique=True)
    amount_loan = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('10000'))])
    amount_to_repay = models.DecimalField(decimal_places=2, max_digits=10,
                                          validators=[MinValueValidator(Decimal('10000'))])
    amount_lated_repay = models.DecimalField(decimal_places=2, max_digits=10,
                                             validators=[MinValueValidator(Decimal('0'))])
    loan_date = models.DateField()
    loan_repayment_date = models.DateField()
    interest_rate = models.IntegerField(choices=[(i,v) for i,v in enumerate(rate_value_choice)], default=0)
    number_lated_month = models.IntegerField(default=0)
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
