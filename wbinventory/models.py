from django.db import models

from wbinventory.settings import (
    CATEGORY_MODEL,
    CURRENCY_MODEL,
    ITEM_MODEL,
    LOCATION_MODEL,
    THIRD_PARTY_MODEL,
    UOM_MODEL,
    PRICE_DECIMAL_PLACES,
    PRICE_MAX_DIGITS,
    QUANTITY_DECIMAL_PLACES,
    QUANTITY_MAX_DIGITS,
)


def price_field(**kwargs):
    """Create a DecimalField for a price with pre-set decimal places and max digits."""
    return models.DecimalField(decimal_places=PRICE_DECIMAL_PLACES, max_digits=PRICE_MAX_DIGITS, **kwargs)


def quantity_field(**kwargs):
    """Create a DecimalField for a quantity with pre-set decimal places and max digits."""
    return models.DecimalField(decimal_places=QUANTITY_DECIMAL_PLACES, max_digits=QUANTITY_MAX_DIGITS, **kwargs)


class Category(models.Model):
    """A categorization of items."""

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Currency(models.Model):
    """A type of currency used in the purchase or sale of items."""

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __unicode__(self):
        return self.code


class Item(models.Model):
    """A type of item being controlled."""

    number = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    default_uom = models.ForeignKey(UOM_MODEL)
    default_location = models.ForeignKey(LOCATION_MODEL)
    reorder_quantity = quantity_field(null=True, blank=True, default=None)
    target_quantity = quantity_field(null=True, blank=True, default=None)

    categories = models.ManyToManyField(CATEGORY_MODEL, related_name='items', through='ItemCategory')
    suppliers = models.ManyToManyField(THIRD_PARTY_MODEL, related_name='items', through='ItemSupplier')

    def __unicode__(self):
        return self.number


class ItemCategory(models.Model):
    """A categorization of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    category = models.ForeignKey(CATEGORY_MODEL)

    class Meta:
        verbose_name_plural = 'Item Categories'


class ItemLocation(models.Model):
    """Location containing a certain quantity of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    location = models.ForeignKey(LOCATION_MODEL)
    uom = models.ForeignKey(UOM_MODEL)
    quantity = quantity_field(default='0')


class ItemPrice(models.Model):
    """The price expected to pay a third party for the supply of a certain quantity of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    third_party = models.ForeignKey(THIRD_PARTY_MODEL)
    uom = models.ForeignKey(UOM_MODEL)
    quantity = quantity_field(default='0')
    currency = models.ForeignKey(CURRENCY_MODEL)
    price = price_field(default='0')

    def __unicode__(self):
        return u'{0} {1}'.format(self.currency.symbol, self.price)


class ItemSupplier(models.Model):
    """A third party that supplies an item."""

    item = models.ForeignKey(ITEM_MODEL)
    third_party = models.ForeignKey(THIRD_PARTY_MODEL)
    priority = models.IntegerField(default=1)  # lower value == higher priority
    notes = models.TextField(blank=True, default='')


class Location(models.Model):
    """An area where items are kept."""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    zone = models.ForeignKey('Zone', null=True, blank=True)
    third_party = models.ForeignKey(THIRD_PARTY_MODEL, null=True, blank=True)

    def __unicode__(self):
        return self.name


class ThirdParty(models.Model):
    """The default model representing a third party."""

    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200, blank=True, default='')
    phone_number = models.CharField(max_length=50, blank=True, default='')
    fax_number = models.CharField(max_length=50, blank=True, default='')
    email_address = models.EmailField(blank=True, default='')
    website_url = models.URLField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    is_client = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_manufacturer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Third Parties'

    def __unicode__(self):
        return self.name


class UnitOfMeasure(models.Model):
    """A unit of measure, used descriptively and for conversion."""

    name = models.CharField(max_length=50)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Units of Measure'

    def __unicode__(self):
        return self.name


class Zone(models.Model):
    """A collection of locations."""

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
