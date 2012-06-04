from models import *
from django.contrib import admin


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'employees', 'sales', 'description',)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'description',)

class SafeComponentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class SafeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class SafeFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class SafeProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacturer', 'store',)

class SafeComponentProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacturer', 'store', 'category',)

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Store)

admin.site.register(LockRating, RatingAdmin)
admin.site.register(SafeRating, RatingAdmin)
admin.site.register(SafeComponentCategory, SafeComponentCategoryAdmin)
admin.site.register(SafeCategory, SafeCategoryAdmin)

admin.site.register(SafeFeature, SafeFeatureAdmin)

admin.site.register(SafeProfile, SafeProfileAdmin)
admin.site.register(SafeComponentProfile, SafeComponentProfileAdmin)


