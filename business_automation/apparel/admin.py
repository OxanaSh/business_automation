from django.contrib import admin
from .models import TypeOfApparel, Apparel, SizeOfApparel, ColourOfApparel, Warehouse, Pack

admin.site.register(TypeOfApparel)
admin.site.register(Apparel)
admin.site.register(SizeOfApparel)
admin.site.register(ColourOfApparel)
admin.site.register(Warehouse)
admin.site.register(Pack)

