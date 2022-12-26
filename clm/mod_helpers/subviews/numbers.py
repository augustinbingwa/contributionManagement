from mod_helpers.models import *
from datetime import datetime

class numberGenerate():
    # get last number save in table generateNumbers
    def get_last_number(self):
        return generateNumbers.objects.get(prefix=self)

    # if its is the first number save in table generateNumbers and decte if the number can containt year and month
    def get_number_first(self):
        res = ''
        obj = generateNumbers.objects.get(prefix=self)
        if obj:
            res = obj.prefix
            if obj.year:
                res += datetime.now().strftime('%Y')
            if obj.month:
                res += datetime.now().strftime('%m')
        return res

    def get_new_number(self):
        obj = numberGenerate.get_last_number(self)
        if obj:
            if obj.year and obj.month:
                number = obj.number
                get_year_month = obj.last_number[len(self):-number]
                month = get_year_month[-2:]
                new_month = datetime.now().strftime('%m')

                if month != new_month:
                    first_number = numberGenerate.get_number_first(self)
                    first_number = first_number + str(1).zfill(obj.number)

                    return first_number

            get_number = obj.last_number.rstrip()
            if get_number != '':
                get_number = get_number[-obj.number:]
                get_number = int(get_number) + 1
                get_number = str(get_number).zfill(obj.number)

                return obj.last_number[:-obj.number] + get_number
            else:
                get_number = numberGenerate.get_number_first(self)
                get_number = get_number + str(1).zfill(obj.number)

                return get_number

        return None
