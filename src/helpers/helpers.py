import random
from datetime import datetime

now = datetime.now()

class Helpers:

    def date_now():
        formatear_date = now.strftime("%d/%m/%Y")
        return formatear_date
    
    def num_random(rango_uno, rango_dos):
        num = random.randint(rango_uno, rango_dos)
        return num
    