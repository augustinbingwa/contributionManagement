from django.test import TestCase
from mod_helpers.views import numberGenerate

# Create your tests here.
class helperTeste(TestCase):
    # test the laste number save
    def get_last_number_test(self):
        return numberGenerate.get_last_number(self)
    # generate number for the first like (prefix + year + month)
    def get_number_first_test(self):
        return numberGenerate.get_number_first('clm')

    def get_new_number_test(self):
        return numberGenerate.get_new_number('clm')