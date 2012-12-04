# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShanghiGame'
        db.create_table('games_shanghigame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('n', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('games', ['ShanghiGame'])

        # Adding model 'ShanghiPlayer'
        db.create_table('games_shanghiplayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['games.ShanghiGame'])),
        ))
        db.send_create_signal('games', ['ShanghiPlayer'])


    def backwards(self, orm):
        # Deleting model 'ShanghiGame'
        db.delete_table('games_shanghigame')

        # Deleting model 'ShanghiPlayer'
        db.delete_table('games_shanghiplayer')


    models = {
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n': ('django.db.models.fields.IntegerField', [], {})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.ShanghiGame']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['games']