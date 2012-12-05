# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ShanghiPlayer.ten'
        db.add_column('games_shanghiplayer', 'ten',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.eleven'
        db.add_column('games_shanghiplayer', 'eleven',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.tweleve'
        db.add_column('games_shanghiplayer', 'tweleve',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.thirteen'
        db.add_column('games_shanghiplayer', 'thirteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.fourteen'
        db.add_column('games_shanghiplayer', 'fourteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.fifteen'
        db.add_column('games_shanghiplayer', 'fifteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.sixteen'
        db.add_column('games_shanghiplayer', 'sixteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.seventeen'
        db.add_column('games_shanghiplayer', 'seventeen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.eighteen'
        db.add_column('games_shanghiplayer', 'eighteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.nineteen'
        db.add_column('games_shanghiplayer', 'nineteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.twenty'
        db.add_column('games_shanghiplayer', 'twenty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.bull'
        db.add_column('games_shanghiplayer', 'bull',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ShanghiPlayer.ten'
        db.delete_column('games_shanghiplayer', 'ten')

        # Deleting field 'ShanghiPlayer.eleven'
        db.delete_column('games_shanghiplayer', 'eleven')

        # Deleting field 'ShanghiPlayer.tweleve'
        db.delete_column('games_shanghiplayer', 'tweleve')

        # Deleting field 'ShanghiPlayer.thirteen'
        db.delete_column('games_shanghiplayer', 'thirteen')

        # Deleting field 'ShanghiPlayer.fourteen'
        db.delete_column('games_shanghiplayer', 'fourteen')

        # Deleting field 'ShanghiPlayer.fifteen'
        db.delete_column('games_shanghiplayer', 'fifteen')

        # Deleting field 'ShanghiPlayer.sixteen'
        db.delete_column('games_shanghiplayer', 'sixteen')

        # Deleting field 'ShanghiPlayer.seventeen'
        db.delete_column('games_shanghiplayer', 'seventeen')

        # Deleting field 'ShanghiPlayer.eighteen'
        db.delete_column('games_shanghiplayer', 'eighteen')

        # Deleting field 'ShanghiPlayer.nineteen'
        db.delete_column('games_shanghiplayer', 'nineteen')

        # Deleting field 'ShanghiPlayer.twenty'
        db.delete_column('games_shanghiplayer', 'twenty')

        # Deleting field 'ShanghiPlayer.bull'
        db.delete_column('games_shanghiplayer', 'bull')


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
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['games.ShanghiGame']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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