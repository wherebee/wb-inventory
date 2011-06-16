from decimal import Decimal
from django.db import transaction
from django.db.utils import IntegrityError
from wbinventory.models import Item, Location, UnitOfMeasure, ItemTransaction, ItemLocation
from wbinventory.tests.base import BaseTest


class ModelsItemTransactionTest(BaseTest):

    fixtures = [
        'wbinventory_test_models_itemtransaction.json',
    ]

    def setUp(self):
        super(ModelsItemTransactionTest, self).setUp()
        self.item1 = Item.objects.get(number='ITEM1')
        self.location1 = Location.objects.get(name='Location 1')
        self.location2 = Location.objects.get(name='Location 2')
        self.ea = UnitOfMeasure.objects.get(name='ea')
        self.dozen = UnitOfMeasure.objects.get(name='dozen')

    def test_add_item(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='1',
            to_uom=self.ea,
        ).save()
        item_location = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.ea,
        )
        self.assertEqual(Decimal('1'), item_location.quantity)

    def test_add_remove_item(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='5',
            to_uom=self.ea,
        ).save()
        ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='2',
            from_uom=self.ea,
        ).save()
        item_location = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.ea,
        )
        self.assertEqual(Decimal('3'), item_location.quantity)

    def test_add_move_item(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='5',
            to_uom=self.ea,
        ).save()
        ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='2',
            from_uom=self.ea,
            to_location=self.location2,
            to_quantity='2',
            to_uom=self.ea,
        ).save()
        item_location1 = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.ea,
        )
        self.assertEqual(Decimal('3'), item_location1.quantity)
        item_location2 = ItemLocation.objects.get(
            item=self.item1,
            location=self.location2,
            uom=self.ea,
        )
        self.assertEqual(Decimal('2'), item_location2.quantity)

    def test_add_move_item_integrityerror(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='5',
            to_uom=self.ea,
        ).save()
        self.assertRaises(IntegrityError, ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='3',
            from_uom=self.ea,
            to_location=self.location2,
            to_quantity='2',
            to_uom=self.ea,
        ).save)
        self.assertEqual(1, ItemTransaction.objects.count())
        self.assertRaises(IntegrityError, ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='12',
            from_uom=self.ea,
            to_location=self.location2,
            to_quantity='1',
            to_uom=self.dozen,
        ).save)
        self.assertEqual(1, ItemTransaction.objects.count())

    def test_update_move_item_integrityerror(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='5',
            to_uom=self.ea,
        ).save()
        item_transaction = ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='2',
            from_uom=self.ea,
            to_location=self.location2,
            to_quantity='2',
            to_uom=self.ea,
        )
        item_transaction.save()
        # Now try to update the item transaction, check that it is disallowed.
        try:
            with transaction.commit_on_success():
                item_transaction.from_quantity = '3'
                item_transaction.to_quantity = '3'
                item_transaction.save()
        except IntegrityError:
            pass
        else:
            raise self.fail('IntegrityError not raised.')
        # Check to see that nothing changed.
        item_location1 = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.ea,
        )
        self.assertEqual(Decimal('3'), item_location1.quantity)
        item_transaction = ItemTransaction.objects.get(pk=item_transaction.pk)
        self.assertEqual(Decimal('2'), item_transaction.from_quantity)
        self.assertEqual(Decimal('2'), item_transaction.to_quantity)

    def test_convert_item(self):
        ItemTransaction(
            item=self.item1,
            to_location=self.location1,
            to_quantity='2',
            to_uom=self.dozen,
        ).save()
        ItemTransaction(
            item=self.item1,
            from_location=self.location1,
            from_quantity='1',
            from_uom=self.dozen,
            to_location=self.location1,
            to_quantity='12',
            to_uom=self.ea,
        ).save()
        item_location1_dozen = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.dozen,
        )
        item_location1_ea = ItemLocation.objects.get(
            item=self.item1,
            location=self.location1,
            uom=self.ea,
        )
        self.assertEqual(Decimal('1'), item_location1_dozen.quantity)
        self.assertEqual(Decimal('12'), item_location1_ea.quantity)
