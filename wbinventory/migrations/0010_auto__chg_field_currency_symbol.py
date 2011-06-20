# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Currency.symbol'
        db.alter_column('wbinventory_currency', 'symbol', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))


    def backwards(self, orm):
        
        # Changing field 'Currency.symbol'
        db.alter_column('wbinventory_currency', 'symbol', self.gf('django.db.models.fields.CharField')(default=' ', max_length=10))


    models = {
        'wbinventory.assembly': {
            'Meta': {'object_name': 'Assembly'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']", 'unique': 'True'}),
            'subitems': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'through': "orm['wbinventory.AssemblyItem']", 'to': "orm['wbinventory.Item']"})
        },
        'wbinventory.assemblyitem': {
            'Meta': {'object_name': 'AssemblyItem'},
            'assembly': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Assembly']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '6'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'wbinventory.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'wbinventory.item': {
            'Meta': {'object_name': 'Item'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'items'", 'symmetrical': 'False', 'through': "orm['wbinventory.ItemCategory']", 'to': "orm['wbinventory.Category']"}),
            'default_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Location']", 'null': 'True', 'blank': 'True'}),
            'default_uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'reorder_quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'}),
            'suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'items'", 'symmetrical': 'False', 'through': "orm['wbinventory.ItemSupplier']", 'to': "orm['wbinventory.ThirdParty']"}),
            'target_quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'})
        },
        'wbinventory.itemcategory': {
            'Meta': {'unique_together': "(('item', 'category'),)", 'object_name': 'ItemCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"})
        },
        'wbinventory.itemlocation': {
            'Meta': {'unique_together': "(('item', 'location', 'uom'),)", 'object_name': 'ItemLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Location']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '6'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.itemprice': {
            'Meta': {'unique_together': "(('item', 'third_party', 'quantity', 'uom', 'currency'),)", 'object_name': 'ItemPrice'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '4'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '16', 'decimal_places': '6'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.ThirdParty']"}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.itemsupplier': {
            'Meta': {'unique_together': "(('item', 'third_party', 'number'),)", 'object_name': 'ItemSupplier'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.ThirdParty']"})
        },
        'wbinventory.itemtransaction': {
            'Meta': {'object_name': 'ItemTransaction'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['wbinventory.Location']"}),
            'from_quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'}),
            'from_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['wbinventory.UnitOfMeasure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'to_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['wbinventory.Location']"}),
            'to_quantity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'}),
            'to_uom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['wbinventory.UnitOfMeasure']"})
        },
        'wbinventory.itemunitofmeasureconversion': {
            'Meta': {'unique_together': "(('from_quantity', 'from_uom'),)", 'object_name': 'ItemUnitOfMeasureConversion'},
            'from_quantity': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '16', 'decimal_places': '6'}),
            'from_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['wbinventory.UnitOfMeasure']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
            'to_quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '6'}),
            'to_uom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['wbinventory.UnitOfMeasure']"})
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'wbinventory.unitofmeasure': {
            'Meta': {'object_name': 'UnitOfMeasure'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'wbinventory.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['wbinventory']
