# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShanghiGame.d'
        db.delete_column('games_shanghigame', 'd')

        # Adding field 'ShanghiGame.name'
        db.add_column('games_shanghigame', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Test', max_length=100),
                      keep_default=False)

        # Adding field 'ShanghiGame.num_players'
        db.add_column('games_shanghigame', 'num_players',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ShanghiGame.d'
        db.add_column('games_shanghigame', 'd',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'ShanghiGame.name'
        db.delete_column('games_shanghigame', 'name')

        # Deleting field 'ShanghiGame.num_players'
        db.delete_column('games_shanghigame', 'num_players')


    models = {
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_players': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.ShanghiGame']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['games']