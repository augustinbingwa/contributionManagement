from mod_settings.models import GlobalVariables
from django.core.exceptions import ObjectDoesNotExist


# --------------------------------------------------------------------------------
class GlobalVariable():
    def save_global_variables():
        """
        create application information before launch
        """
        obj = GlobalVariables(group="AMOUNT", key="MINIMUMAMOUNTCONTRIBUTION", value=100000,
                             description="Minimum amount for contribution")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="AMOUNT", key="MIXIMUMAMOUNTCONTRIBUTION", value=300000,
                             description="Maximum amount for contribution")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="ASSOCIATION", key="NAME", value="ASSOCIATION NAME", description="Association name")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="ASSOCIATION", key="ADDRESS", value="ASSOCIATION ADDRESS",
                             description="Association Address")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="ASSOCIATION", key="CONTACT", value="Phone : +257 00000000",
                             description="Association phone number")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="ASSOCIATION", key="DATESTARTACTIVITY", value="01/01/2023",
                             description="Start date of association activity")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="ASSOCIATION", key="EMAIL", value="association@gmail.com",
                             description="Association email address")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        # Impôt foncier, nombre d'années max d'exhoneration d'une déclaration de construction (à utliser dans la date de mise en valeur d'une déclaration)
        obj = GlobalVariables(group="ASSOCIATION", key="ACRONYM", value="the acronym of the association",
                             description="the acronym of the association")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="INTERESTRATE", key="INTEREST_RATE_MONTH_LOAN", value=6,
                             description="Interest rate for a month of loan")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="INTERESTRATE", key="INTEREST_RATE_MORE_THAN_ONE_MONTH_LOAN", value=10,
                             description="Interst rate for more than one month of loan")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        obj = GlobalVariables(group="PENALTYRATE", key="PENALTYRATEONEMONTHLATE",
                             value=5,
                             description="Penallty rate for one month late")
        if not GlobalVariables.objects.filter(group=obj.group, key=obj.key):
            obj.save()

        return

    def get_global_variable(self,group, key):
        """
        Find the variable global object
        """
        try:
            obj = GlobalVariable.objects.filter(group=group, key=key)[0]
        except ObjectDoesNotExist:
            return None

        return obj