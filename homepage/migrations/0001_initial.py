# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Style'
        db.create_table(u'homepage_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('contr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lolfield', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'homepage', ['Style'])

        # Adding model 'Item'
        db.create_table(u'homepage_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'homepage', ['Item'])

        # Adding M2M table for field type1 on 'Item'
        m2m_table_name = db.shorten_name(u'homepage_item_type1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'homepage.item'], null=False)),
            ('style', models.ForeignKey(orm[u'homepage.style'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'style_id'])


    def backwards(self, orm):
        # Deleting model 'Style'
        db.delete_table(u'homepage_style')

        # Deleting model 'Item'
        db.delete_table(u'homepage_item')

        # Removing M2M table for field type1 on 'Item'
        db.delete_table(db.shorten_name(u'homepage_item_type1'))


    models = {
        u'homepage.item': {
            'Meta': {'ordering': "['name']", 'object_name': 'Item'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type1': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['homepage.Style']", 'symmetrical': 'False'})
        },
        u'homepage.style': {
            'Meta': {'ordering': "['-name']", 'object_name': 'Style'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'contr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lolfield': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['homepage']