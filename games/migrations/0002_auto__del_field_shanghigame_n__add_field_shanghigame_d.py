# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShanghiGame.n'
        db.delete_column('games_shanghigame', 'n')

        # Adding field 'ShanghiGame.d'
        db.add_column('games_shanghigame', 'd',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ShanghiGame.n'
        db.add_column('games_shanghigame', 'n',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'ShanghiGame.d'
        db.delete_column('games_shanghigame', 'd')


    models = {
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'd': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.ShanghiGame']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['games']