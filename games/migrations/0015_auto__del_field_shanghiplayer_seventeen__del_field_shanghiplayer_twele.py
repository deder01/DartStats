# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ShanghiPlayer.seventeen'
        db.delete_column('games_shanghiplayer', 'seventeen')

        # Deleting field 'ShanghiPlayer.tweleve'
        db.delete_column('games_shanghiplayer', 'tweleve')

        # Deleting field 'ShanghiPlayer.ten'
        db.delete_column('games_shanghiplayer', 'ten')

        # Deleting field 'ShanghiPlayer.nineteen'
        db.delete_column('games_shanghiplayer', 'nineteen')

        # Deleting field 'ShanghiPlayer.eighteen'
        db.delete_column('games_shanghiplayer', 'eighteen')

        # Deleting field 'ShanghiPlayer.twenty'
        db.delete_column('games_shanghiplayer', 'twenty')

        # Deleting field 'ShanghiPlayer.fourteen'
        db.delete_column('games_shanghiplayer', 'fourteen')

        # Deleting field 'ShanghiPlayer.eleven'
        db.delete_column('games_shanghiplayer', 'eleven')

        # Deleting field 'ShanghiPlayer.thirteen'
        db.delete_column('games_shanghiplayer', 'thirteen')

        # Deleting field 'ShanghiPlayer.bull'
        db.delete_column('games_shanghiplayer', 'bull')

        # Deleting field 'ShanghiPlayer.sixteen'
        db.delete_column('games_shanghiplayer', 'sixteen')

        # Deleting field 'ShanghiPlayer.fifteen'
        db.delete_column('games_shanghiplayer', 'fifteen')

        # Adding field 'ShanghiPlayer.scores'
        db.add_column('games_shanghiplayer', 'scores',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default='(0,0,0,0,0,0,0,0,0,0,0,0)', max_length=12),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ShanghiPlayer.seventeen'
        db.add_column('games_shanghiplayer', 'seventeen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.tweleve'
        db.add_column('games_shanghiplayer', 'tweleve',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.ten'
        db.add_column('games_shanghiplayer', 'ten',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.nineteen'
        db.add_column('games_shanghiplayer', 'nineteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.eighteen'
        db.add_column('games_shanghiplayer', 'eighteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.twenty'
        db.add_column('games_shanghiplayer', 'twenty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.fourteen'
        db.add_column('games_shanghiplayer', 'fourteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.eleven'
        db.add_column('games_shanghiplayer', 'eleven',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.thirteen'
        db.add_column('games_shanghiplayer', 'thirteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.bull'
        db.add_column('games_shanghiplayer', 'bull',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.sixteen'
        db.add_column('games_shanghiplayer', 'sixteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ShanghiPlayer.fifteen'
        db.add_column('games_shanghiplayer', 'fifteen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'ShanghiPlayer.scores'
        db.delete_column('games_shanghiplayer', 'scores')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'games.shanghigame': {
            'Meta': {'object_name': 'ShanghiGame'},
            'current_player': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'current_round': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_players': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['games.ShanghiGame']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shangi_games'", 'to': "orm['auth.User']"}),
            'player_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'scores': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['games']