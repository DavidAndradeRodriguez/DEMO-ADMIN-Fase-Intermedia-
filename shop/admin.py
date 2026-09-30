from django.contrib import admin
from shop.models import Tecnologia
from shop.models import Limpieza
from shop.models import Ropa
from shop.models import Comida
# Register your models here.
admin.site.register(Tecnologia)
admin.site.register(Limpieza)
admin.site.register(Ropa)
admin.site.register(Comida)