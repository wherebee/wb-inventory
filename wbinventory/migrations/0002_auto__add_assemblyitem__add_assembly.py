# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AssemblyItem'
        db.create_table('wbinventory_assemblyitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assembly', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Assembly'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=16, decimal_places=6)),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.UnitOfMeasure'])),
        ))
        db.send_create_signal('wbinventory', ['AssemblyItem'])

        # Adding model 'Assembly'
        db.create_table('wbinventory_assembly', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wbinventory.Item'])),
        ))
        db.send_create_signal('wbinventory', ['Assembly'])


    def backwards(self, orm):
        
        # Deleting model 'AssemblyItem'
        db.delete_table('wbinventory_assemblyitem')

        # Deleting model 'Assembly'
        db.delete_table('wbinventory_assembly')


    models = {
        'wbinventory.assembly': {
            'Meta': {'object_name': 'Assembly'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wbinventory.Item']"}),
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
            'reorder_quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'}),
            'suppliers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'items'", 'symmetrical': 'False', 'through': "orm['wbinventory.ItemSupplier']", 'to': "orm['wbinventory.ThirdParty']"}),
            'target_quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '6', 'blank': 'True'})
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
