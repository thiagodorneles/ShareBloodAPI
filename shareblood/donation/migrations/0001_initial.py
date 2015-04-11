# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donation'
        db.create_table(u'donation_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('favored', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('needed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('donated', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'donation', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Donation'
        db.delete_table(u'donation_donation')


    models = {
        u'donation.donation': {
            'Meta': {'object_name': 'Donation'},
            'donated': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'favored': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['donation']