# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShanghiPlayer.headline'
        db.delete_column('games_shanghiplayer', 'headline')

        # Adding field 'ShanghiPlayer.name'
        db.add_column('games_shanghiplayer', 'name',
                      self.gf('django.db.models.fields.CharField')(default='player', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ShanghiPlayer.headline'
        db.add_column('games_shanghiplayer', 'headline',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=100),
                      keep_default=False)

        # Deleting field 'ShanghiPlayer.name'
        db.delete_column('games_shanghiplayer', 'name')


    models = {
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_players': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'bull': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eighteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eleven': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fifteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fourteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['games.ShanghiGame']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nineteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'seventeen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sixteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ten': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thirteen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tweleve': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twenty': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['games']