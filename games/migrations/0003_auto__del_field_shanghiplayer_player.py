# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShanghiPlayer.player'
        db.delete_column('games_shanghiplayer', 'player_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ShanghiPlayer.player'
        raise RuntimeError("Cannot reverse this migration. 'ShanghiPlayer.player' and its values cannot be restored.")

    models = {
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'current_player': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'current_round': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'done': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_players': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'accuracy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '4'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['games.ShanghiGame']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'games.shanghiround': {
            'Meta': {'object_name': 'ShanghiRound'},
            'doubles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'round_number': ('django.db.models.fields.IntegerField', [], {}),
            'shanghiplayer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rounds'", 'to': "orm['games.ShanghiPlayer']"}),
            'singles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'triples': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['games']