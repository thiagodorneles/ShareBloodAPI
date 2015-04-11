# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FavoriteBloodTypes'
        db.create_table(u'donation_favoritebloodtypes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blood_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('donation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donation.Donation'])),
        ))
        db.send_create_signal(u'donation', ['FavoriteBloodTypes'])


    def backwards(self, orm):
        # Deleting model 'FavoriteBloodTypes'
        db.delete_table(u'donation_favoritebloodtypes')


    models = {
        u'donation.donation': {
            'Meta': {'object_name': 'Donation'},
            'donated': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'favored': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'donation.favoritebloodtypes': {
            'Meta': {'object_name': 'FavoriteBloodTypes'},
            'blood_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'donation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donation.Donation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['donation']