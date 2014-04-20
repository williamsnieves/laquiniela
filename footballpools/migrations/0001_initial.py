# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FootballPool'
        db.create_table('footballpools_footballpool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_qnl', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('user_qnl', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quinielas', to=orm['auth.User'])),
            ('group_qnl', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('date_qnl', self.gf('django.db.models.fields.DateField')()),
            ('name_qnl', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('team_a_qnl', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('goals_a_qnl', self.gf('django.db.models.fields.IntegerField')()),
            ('team_b_qnl', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('goals_b_qnl', self.gf('django.db.models.fields.IntegerField')()),
            ('result_qnl', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('footballpools', ['FootballPool'])


    def backwards(self, orm):
        # Deleting model 'FootballPool'
        db.delete_table('footballpools_footballpool')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'footballpools.footballpool': {
            'Meta': {'object_name': 'FootballPool'},
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date_qnl': ('django.db.models.fields.DateField', [], {}),
            'goals_a_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'goals_b_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'group_qnl': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_qnl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'result_qnl': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'team_a_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team_b_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_qnl': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quinielas'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['footballpools']