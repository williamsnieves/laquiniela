# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FootballPool.progress_qnl'
        db.alter_column('footballpools_footballpool', 'progress_qnl', self.gf('django.db.models.fields.CharField')(max_length=6))

    def backwards(self, orm):

        # Changing field 'FootballPool.progress_qnl'
        db.alter_column('footballpools_footballpool', 'progress_qnl', self.gf('django.db.models.fields.BooleanField')())

    models = {
        'footballpools.footballpool': {
            'Meta': {'object_name': 'FootballPool'},
            'city_match': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_qnl': ('django.db.models.fields.DateField', [], {}),
            'flag_a_qnl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'flag_b_qnl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'goals_a_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'goals_b_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'group_qnl': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_qnl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order_qnl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'progress_qnl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6'}),
            'result_qnl': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'team_a_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team_b_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['footballpools']