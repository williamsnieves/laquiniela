# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'FootballPool.user_qnl' to match new field type.
        db.rename_column('footballpools_footballpool', 'user_qnl_id', 'user_qnl')
        # Changing field 'FootballPool.user_qnl'
        db.alter_column('footballpools_footballpool', 'user_qnl', self.gf('django.db.models.fields.CharField')(max_length=15))
        # Removing index on 'FootballPool', fields ['user_qnl']
        db.delete_index('footballpools_footballpool', ['user_qnl_id'])


    def backwards(self, orm):
        # Adding index on 'FootballPool', fields ['user_qnl']
        db.create_index('footballpools_footballpool', ['user_qnl_id'])


        # Renaming column for 'FootballPool.user_qnl' to match new field type.
        db.rename_column('footballpools_footballpool', 'user_qnl', 'user_qnl_id')
        # Changing field 'FootballPool.user_qnl'
        db.alter_column('footballpools_footballpool', 'user_qnl_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
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
            'user_qnl': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['footballpools']