from django.contrib import admin

from wbinventory import models


class AssemblyItemInline(admin.TabularInline):

    model = models.AssemblyItem


class ItemCategoryInline(admin.TabularInline):

    model = models.ItemCategory


class ItemLocationInline(admin.TabularInline):

    model = models.ItemLocation


class ItemPriceInline(admin.TabularInline):

    model = models.ItemPrice


class ItemSupplierInline(admin.TabularInline):

    model = models.ItemSupplier


class LocationInline(admin.TabularInline):

    model = models.Location


class AssemblyAdmin(admin.ModelAdmin):

    inlines = [
        AssemblyItemInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    pass


class CurrencyAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):

    inlines = [
        ItemCategoryInline,
        ItemLocationInline,
        ItemSupplierInline,
        ItemPriceInline,
    ]


class LocationAdmin(admin.ModelAdmin):
    pass


class ThirdPartyAdmin(admin.ModelAdmin):
    pass


class UnitOfMeasureAdmin(admin.ModelAdmin):
    pass


class ZoneAdmin(admin.ModelAdmin):

    inlines = [
        LocationInline,
    ]


admin.site.register(models.Assembly, AssemblyAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.ThirdParty, ThirdPartyAdmin)
admin.site.register(models.UnitOfMeasure, UnitOfMeasureAdmin)
admin.site.register(models.Zone, ZoneAdmin)
