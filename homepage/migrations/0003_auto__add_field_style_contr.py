# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Style.contr'
        db.add_column(u'homepage_style', 'contr',
                      self.gf('django.db.models.fields.CharField')(default='www.boston-dynimics.com', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Style.contr'
        db.delete_column(u'homepage_style', 'contr')


    models = {
        u'homepage.item': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Item'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['homepage.Style']", 'symmetrical': 'False'})
        },
        u'homepage.style': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Style'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'contr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['homepage']