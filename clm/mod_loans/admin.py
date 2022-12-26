from django.contrib import admin
from .models import *


# Register your models here.
class LoanAdmin(admin.ModelAdmin):
    exclude = ('number_lated_month', 'created_at', 'updated_at', 'validated_at',
               'created_by', 'valideted_by', 'amount_lated_repay',)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.save()
        form.save_m2m()
        return instance

# admin.site.register(Loan)
admin.site.register(Loan, LoanAdmin)
