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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('done', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_players', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('current_round', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('current_player', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal('games', ['ShanghiGame'])

        # Adding model 'ShanghiPlayer'
        db.create_table('games_shanghiplayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_num', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['games.ShanghiGame'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shangi_games', to=orm['auth.User'])),
            ('total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('accuracy', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=4)),
        ))
        db.send_create_signal('games', ['ShanghiPlayer'])

        # Adding model 'ShanghiRound'
        db.create_table('games_shanghiround', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('round_number', self.gf('django.db.models.fields.IntegerField')()),
            ('singles', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('doubles', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('triples', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('shanghiplayer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rounds', to=orm['games.ShanghiPlayer'])),
        ))
        db.send_create_signal('games', ['ShanghiRound'])


    def backwards(self, orm):
        # Deleting model 'ShanghiGame'
        db.delete_table('games_shanghigame')

        # Deleting model 'ShanghiPlayer'
        db.delete_table('games_shanghiplayer')

        # Deleting model 'ShanghiRound'
        db.delete_table('games_shanghiround')


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
            'done': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_players': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        'games.shanghiplayer': {
            'Meta': {'object_name': 'ShanghiPlayer'},
            'accuracy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '4'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['games.ShanghiGame']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shangi_games'", 'to': "orm['auth.User']"}),
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