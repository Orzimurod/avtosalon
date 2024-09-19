from django.contrib import admin

from apps.models import Car, CarBrand, CarColor, Category, Image

admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarColor)
admin.site.register(Image)
admin.site.register(Category)

