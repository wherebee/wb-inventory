# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('wbinventory_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('wbinventory', ['Category'])

        # Adding model 'Currency'
        db.create_table('wbinventory_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('wbinventory', ['Currency'])

        # Adding model 'Item'
        db.create_table('wbinventory_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('default_uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.UnitOfMeasure'])),
            ('default_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Location'])),
            ('reorder_quantity', self.gf('django.db.models.fields.DecimalField')(default='', null=True, max_digits=16, decimal_places=6, blank=True)),
            ('target_quantity', self.gf('django.db.models.fields.DecimalField')(default='', null=True, max_digits=16, decimal_places=6, blank=True)),
        ))
        db.send_create_signal('wbinventory', ['Item'])

        # Adding model 'ItemCategory'
        db.create_table('wbinventory_itemcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Category'])),
        ))
        db.send_create_signal('wbinventory', ['ItemCategory'])

        # Adding model 'ItemLocation'
        db.create_table('wbinventory_itemlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Location'])),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.UnitOfMeasure'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=6)),
        ))
        db.send_create_signal('wbinventory', ['ItemLocation'])

        # Adding model 'ItemPrice'
        db.create_table('wbinventory_itemprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
            ('third_party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.ThirdParty'])),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.UnitOfMeasure'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=6)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Currency'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=4)),
        ))
        db.send_create_signal('wbinventory', ['ItemPrice'])

        # Adding model 'ItemSupplier'
        db.create_table('wbinventory_itemsupplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
            ('third_party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.ThirdParty'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('wbinventory', ['ItemSupplier'])

        # Adding model 'Location'
        db.create_table('wbinventory_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Zone'], null=True, blank=True)),
            ('third_party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.ThirdParty'], null=True, blank=True)),
        ))
        db.send_create_signal('wbinventory', ['Location'])

        # Adding model 'ThirdParty'
        db.create_table('wbinventory_thirdparty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('fax_number', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True)),
            ('website_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('is_client', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_supplier', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_manufacturer', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('wbinventory', ['ThirdParty'])

        # Adding model 'UnitOfMeasure'
        db.create_table('wbinventory_unitofmeasure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('wbinventory', ['UnitOfMeasure'])

        # Adding model 'Zone'
        db.create_table('wbinventory_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('wbinventory', ['Zone'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('wbinventory_category')

        # Deleting model 'Currency'
        db.delete_table('wbinventory_currency')

        # Deleting model 'Item'
        db.delete_table('wbinventory_item')

        # Deleting model 'ItemCategory'
        db.delete_table('wbinventory_itemcategory')

        # Deleting model 'ItemLocation'
        db.delete_table('wbinventory_itemlocation')

        # Deleting model 'ItemPrice'
        db.delete_table('wbinventory_itemprice')

        # Deleting model 'ItemSupplier'
        db.delete_table('wbinventory_itemsupplier')

        # Deleting model 'Location'
        db.delete_table('wbinventory_location')

        # Deleting model 'ThirdParty'
        db.delete_table('wbinventory_thirdparty')

        # Deleting model 'UnitOfMeasure'
        db.delete_table('wbinventory_unitofmeasure')

        # Deleting model 'Zone'
        db.delete_table('wbinventory_zone')


    models = {
        'wbinventory.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wbinventory.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'wbinventory.item': {
            'Meta': {'object_name': 'Item'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'items'", 'symmetrical': 'False', 'through': "orm['wbinventory.ItemCategory']", 'to': "orm['wbinventory.Category']"}),
            'default_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Location']"}),
            'default_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reorder_quantity': ('django.db.models.fields.DecimalField', [], {'default': "''", 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'}),
            'suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'items'", 'symmetrical': 'False', 'through': "orm['wbinventory.ItemSupplier']", 'to': "orm['wbinventory.ThirdParty']"}),
            'target_quantity': ('django.db.models.fields.DecimalField', [], {'default': "''", 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'})
        },
        'wbinventory.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"})
        },
        'wbinventory.itemlocation': {
            'Meta': {'object_name': 'ItemLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Location']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '6'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.itemprice': {
            'Meta': {'object_name': 'ItemPrice'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '4'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '6'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.ThirdParty']"}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.itemsupplier': {
            'Meta': {'object_name': 'ItemSupplier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.ThirdParty']"})
        },
        'wbinventory.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.ThirdParty']", 'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Zone']", 'null': 'True', 'blank': 'True'})
        },
        'wbinventory.thirdparty': {
            'Meta': {'object_name': 'ThirdParty'},
            'contact_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'fax_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_client': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_manufacturer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_supplier': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'wbinventory.unitofmeasure': {
            'Meta': {'object_name': 'UnitOfMeasure'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'wbinventory.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['wbinventory']
