"""Django settings applicable to wbinventory."""

from django.conf import settings


ASSEMBLY_MODEL = getattr(settings, 'WBINVENTORY_ASSEMBLY_MODEL', 'wbinventory.Assembly')
CATEGORY_MODEL = getattr(settings, 'WBINVENTORY_CATEGORY_MODEL', 'wbinventory.Category')
CURRENCY_MODEL = getattr(settings, 'WBINVENTORY_CURRENCY_MODEL', 'wbinventory.Currency')
ITEM_MODEL = getattr(settings, 'WBINVENTORY_ITEM_MODEL', 'wbinventory.Item')
LOCATION_MODEL = getattr(settings, 'WBINVENTORY_LOCATION_MODEL', 'wbinventory.Location')
THIRD_PARTY_MODEL = getattr(settings, 'WBINVENTORY_THIRD_PARTY_MODEL', 'wbinventory.ThirdParty')
UOM_MODEL = getattr(settings, 'WBINVENTORY_UOM_MODEL', 'wbinventory.UnitOfMeasure')

PRICE_DECIMAL_PLACES = getattr(settings, 'WBINVENTORY_QUANTITY_DECIMAL_PLACES', 4)
PRICE_MAX_DIGITS = getattr(settings, 'WBINVENTORY_QUANTITY_MAX_DIGITS', 16)

QUANTITY_DECIMAL_PLACES = getattr(settings, 'WBINVENTORY_QUANTITY_DECIMAL_PLACES', 6)
QUANTITY_MAX_DIGITS = getattr(settings, 'WBINVENTORY_QUANTITY_MAX_DIGITS', 16)
