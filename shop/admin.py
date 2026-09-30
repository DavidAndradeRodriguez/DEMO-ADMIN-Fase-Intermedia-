from django.contrib import admin
from shop.models import Tecnologia
from shop.models import Limpieza
from shop.models import Ropa
from shop.models import Comida

class shopAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion']
# Register your models here.
admin.site.register(Tecnologia, shopAdmin)
admin.site.register(Limpieza, shopAdmin)
admin.site.register(Ropa, shopAdmin)
admin.site.register(Comida, shopAdmin)