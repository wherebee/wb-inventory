from django.contrib import admin

from wbinventory.models import (
    Category,
    Currency,
    Item,
    ItemCategory,
    ItemLocation,
    ItemPrice,
    ItemSupplier,
    Location,
    ThirdParty,
    UnitOfMeasure,
    Zone,
)


class ItemCategoryInline(admin.TabularInline):

    model = ItemCategory


class ItemLocationInline(admin.TabularInline):

    model = ItemLocation


class ItemPriceInline(admin.TabularInline):

    model = ItemPrice


class ItemSupplierInline(admin.TabularInline):

    model = ItemSupplier


class LocationInline(admin.TabularInline):

    model = Location


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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ThirdParty, ThirdPartyAdmin)
admin.site.register(UnitOfMeasure, UnitOfMeasureAdmin)
admin.site.register(Zone, ZoneAdmin)
