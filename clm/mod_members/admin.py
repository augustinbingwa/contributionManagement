from django.contrib import admin
from .models import *
from mod_helpers.views import *
from mod_settings.enums import PREFIX_REGISTRER_NUMBER
from mod_helpers.views import *
from mod_helpers.models import *
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        new_number = numberGenerate.get_new_number(PREFIX_REGISTRER_NUMBER)
        obj_number = generateNumbers.objects.get(prefix=PREFIX_REGISTRER_NUMBER)
        obj_number.last_chrono = new_number
        registration_number = new_number
        instance = form.save(commit=False)
        if not change or not instance.registration_number:
            instance.registration_number = registration_number
        instance.save()
        form.save_m2m()
        obj_number.save()
        return instance

admin.site.register(Member,MemberAdmin)