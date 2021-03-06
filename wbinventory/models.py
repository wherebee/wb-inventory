from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.expressions import F
from django.db.models.signals import post_save
from django.db.utils import IntegrityError
from django.dispatch.dispatcher import receiver

from wbinventory.settings import (
    ASSEMBLY_MODEL,
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


class Assembly(models.Model):
    """An item representing an assembly that consists of multiple sub-items.

    A sub-item may be capable of being an assembly itself.
    """

    item = models.ForeignKey(ITEM_MODEL, unique=True)
    subitems = models.ManyToManyField(ITEM_MODEL, related_name='+', through='AssemblyItem')

    class Meta:
        verbose_name_plural = 'Assemblies'

    def __unicode__(self):
        return unicode(self.item)


class AssemblyItem(models.Model):
    """A quantity of an item in an assembly."""

    assembly = models.ForeignKey(ASSEMBLY_MODEL)
    item = models.ForeignKey(ITEM_MODEL)
    quantity = quantity_field(default='0')
    uom = models.ForeignKey(UOM_MODEL)

    def __unicode__(self):
        return u'{0}: {1}, {2} {3}'.format(
            self.assembly,
            self.item,
            self.quantity,
            self.uom,
        )


class Category(models.Model):
    """A categorization of items."""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Currency(models.Model):
    """A type of currency used in the purchase or sale of items."""

    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __unicode__(self):
        return self.code


class Item(models.Model):
    """A type of item being controlled."""

    number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=250, blank=True, default='')
    description = models.TextField(blank=True, default='')
    default_uom = models.ForeignKey(UOM_MODEL, null=True, blank=True, verbose_name='Default unit of measure')
    default_location = models.ForeignKey(LOCATION_MODEL, null=True, blank=True)
    reorder_quantity = quantity_field(null=True, blank=True, default=None)
    target_quantity = quantity_field(null=True, blank=True, default=None)
    notes = models.TextField(blank=True, default='')

    categories = models.ManyToManyField(CATEGORY_MODEL, related_name='items', through='ItemCategory')
    suppliers = models.ManyToManyField(THIRD_PARTY_MODEL, related_name='items', through='ItemSupplier')

    def __unicode__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('wbinventory_item_detail', kwargs=dict(pk=self.pk))


class ItemCategory(models.Model):
    """A categorization of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    category = models.ForeignKey(CATEGORY_MODEL)

    class Meta:
        verbose_name_plural = 'Item Categories'
        unique_together = (
            ('item', 'category'),
        )

    def __unicode__(self):
        return u'{0} ({1})'.format(
            self.item,
            self.category,
        )


class ItemLocation(models.Model):
    """Location containing a certain quantity of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    location = models.ForeignKey(LOCATION_MODEL)
    quantity = quantity_field(default='0')
    uom = models.ForeignKey(UOM_MODEL)

    class Meta:
        unique_together = (
            ('item', 'location', 'uom'),
        )

    def __unicode__(self):
        return u'{0} @ {1}: {2} {3}'.format(
            self.item,
            self.location,
            self.quantity,
            self.uom,
        )


class ItemPrice(models.Model):
    """The price expected to pay a third party for the supply of a certain quantity of an item."""

    item = models.ForeignKey(ITEM_MODEL)
    third_party = models.ForeignKey(THIRD_PARTY_MODEL)
    quantity = quantity_field(default='0')
    uom = models.ForeignKey(UOM_MODEL)
    currency = models.ForeignKey(CURRENCY_MODEL)
    price = price_field(default='0')

    class Meta:
        unique_together = (
            ('item', 'third_party', 'quantity', 'uom', 'currency'),
        )

    def __unicode__(self):
        return u'{0} {1}'.format(self.currency.symbol, self.price)


class ItemSupplier(models.Model):
    """A third party that supplies an item."""

    item = models.ForeignKey(ITEM_MODEL)
    third_party = models.ForeignKey(THIRD_PARTY_MODEL)
    number = models.CharField(max_length=100, blank=True, default='')
    priority = models.IntegerField(default=1)  # lower value == higher priority
    notes = models.TextField(blank=True, default='')

    class Meta:
        unique_together = (
            ('item', 'third_party', 'number'),
        )

    def __unicode__(self):
        if self.number:
            return u'{0}, supplied by {1} ({2})'.format(
                self.item,
                self.third_party,
                self.number,
            )
        else:
            return u'{0}, supplied by {1}'.format(
                self.item,
                self.third_party,
            )


class ItemTransaction(models.Model):
    """A movement of an item between locations or units of measure."""

    item = models.ForeignKey(ITEM_MODEL)
    from_location = models.ForeignKey(LOCATION_MODEL, blank=True, null=True, related_name='+')
    from_quantity = quantity_field(blank=True, null=True)
    from_uom = models.ForeignKey(UOM_MODEL, blank=True, null=True, related_name='+')
    to_location = models.ForeignKey(LOCATION_MODEL, blank=True, null=True, related_name='+')
    to_quantity = quantity_field(blank=True, null=True)
    to_uom = models.ForeignKey(UOM_MODEL, blank=True, null=True, related_name='+')
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None):
        if self.is_add():
            if (
                self.from_quantity is not None
                or self.from_uom is not None
                or self.to_quantity is None
                or self.to_uom is None
            ):
                raise IntegrityError('Add item transaction requires all "to" information and no "from" information.')
            else:
                pass
        elif self.is_remove():
            if (
                self.from_quantity is None
                or self.from_uom is None
                or self.to_quantity is not None
                or self.to_uom is not None
            ):
                raise IntegrityError('Remove item transaction requires all "from" information and no "to" information.')
            else:
                pass
        elif self.is_move():
            if (
                self.from_quantity is None
                or self.from_uom is None
                or (self.to_uom is not None and self.from_uom != self.to_uom)
                or (self.to_quantity is not None and self.from_quantity != self.to_quantity)
            ):
                raise IntegrityError('Move item transaction requires all "from" information, all "to" information, and matching quantity and unit of measure.')
            else:
                # to_uom and to_quantity are either None or matching.
                # We want them to match for certain.
                self.to_uom = self.from_uom
                self.to_quantity = self.from_quantity
        elif self.is_convert():
            if (
                self.from_quantity is None
                or self.from_uom is None
                or self.to_quantity is None
                or self.to_uom is None
            ):
                raise IntegrityError('Convert item transaction requires all "from" information and all "to" information.')
            else:
                # to_location may be empty.
                # Make sure it matches from_location.
                self.to_location = self.from_location
        else:
            raise IntegrityError('Unknown item transaction.')
        # One of the four transaction types was detected, and the transaction
        # was deemed valid; continue saving.
        super(ItemTransaction, self).save(force_insert, force_update, using)

    def is_add(self):
        return self.from_location is None and self.to_location is not None

    def is_remove(self):
        return (
            self.from_location is not None
            and self.to_location is None
            and self.to_quantity is None
            and self.to_uom is None
        )

    def is_move(self):
        return (
            self.to_location is not None
            and self.from_location != self.to_location
        )

    def is_convert(self):
        return (
            self.from_location == self.to_location
            or (
                self.from_location is not None
                and self.to_location is None
                and self.from_quantity is not None
                and self.from_uom is not None
                and self.to_quantity is not None
                and self.to_uom is not None
            )
        )

    def __unicode__(self):
        if self.is_add():
            return u'+ {0} {1} {2} @ {3}'.format(
                self.to_quantity,
                self.to_uom,
                self.item,
                self.to_location,
            )
        elif self.is_remove():
            return u'- {0} {1} {2} @ {3}'.format(
                self.from_quantity,
                self.from_uom,
                self.item,
                self.from_location,
            )
        elif self.is_move():
            return u'> {0} {1} {2} @ {3} to {4}'.format(
                self.from_quantity,
                self.from_uom,
                self.item,
                self.from_location,
                self.to_location,
            )
        elif self.is_convert():
            return u'C {0} {1} to {2} {3} {4} @ {5}'.format(
                self.from_quantity,
                self.from_uom,
                self.to_quantity,
                self.to_uom,
                self.item,
                self.from_location,
            )
        else:
            return u'(Invalid transaction)'


@receiver(post_save, sender=ItemTransaction)
def on_ItemTransaction_save(sender, instance, created, **kwargs):
    """
    Update ItemLocation(s) based on a newly-created ItemTransaction.
    """
    if not created:
        raise IntegrityError('Cannot update ItemTransaction instances.')
    if instance.from_location:
        updated = ItemLocation.objects.filter(
            item=instance.item,
            location=instance.from_location,
            uom=instance.from_uom,
        ).update(
            quantity=F('quantity') - instance.from_quantity,
        )
        if not updated:
            ItemLocation(
                item=instance.item,
                location=instance.from_location,
                quantity=instance.from_quantity,
                uom=instance.from_uom,
            ).save()
        else:
            # Already updated.
            pass
    else:
        # ItemTransaction has no From location.
        pass
    if instance.to_location:
        updated = ItemLocation.objects.filter(
            item=instance.item,
            location=instance.to_location,
            uom=instance.to_uom,
        ).update(
            quantity=F('quantity') + instance.to_quantity,
        )
        if not updated:
            ItemLocation(
                item=instance.item,
                location=instance.to_location,
                quantity=instance.to_quantity,
                uom=instance.to_uom,
            ).save()
        else:
            # Already updated.
            pass
    else:
        # ItemTransaction has no To location.
        pass


class ItemUnitOfMeasureConversion(models.Model):
    """Describes a possible conversion of one unit of measure to another."""

    item = models.ForeignKey(ITEM_MODEL)
    from_quantity = quantity_field(default='1')
    from_uom = models.ForeignKey(UOM_MODEL, related_name='+')
    to_quantity = quantity_field()
    to_uom = models.ForeignKey(UOM_MODEL, related_name='+')

    class Meta:
        unique_together = (
            ('from_quantity', 'from_uom'),
        )

    def __unicode__(self):
        return u'{0}: {1} {2} -> {3} {4}'.format(
            self.item,
            self.from_quantity,
            self.from_uom,
            self.to_quantity,
            self.to_uom,
        )


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
    """The default model representing a third party to the organization managing inventory."""

    name = models.CharField(max_length=200, unique=True)
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

    name = models.CharField(max_length=50, unique=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Units of Measure'

    def __unicode__(self):
        return self.name


class Zone(models.Model):
    """A collection of locations within the organization managing inventory."""

    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name
