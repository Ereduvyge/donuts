from django.contrib import admin
from .models import Donut
# Register your models here.

admin.autodiscover()


class DonutAdmin(admin.ModelAdmin):
    list_display=('name','price')
    list_filter=['onSale', 'isSpecial']
    search_fields=['name']

admin.site.register(Donut, DonutAdmin)
