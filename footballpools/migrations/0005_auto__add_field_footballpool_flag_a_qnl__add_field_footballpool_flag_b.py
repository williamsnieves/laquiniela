# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FootballPool.flag_a_qnl'
        db.add_column('footballpools_footballpool', 'flag_a_qnl',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)

        # Adding field 'FootballPool.flag_b_qnl'
        db.add_column('footballpools_footballpool', 'flag_b_qnl',
                      self.gf('django.db.models.fields.CharField')(max_length=200, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FootballPool.flag_a_qnl'
        db.delete_column('footballpools_footballpool', 'flag_a_qnl')

        # Deleting field 'FootballPool.flag_b_qnl'
        db.delete_column('footballpools_footballpool', 'flag_b_qnl')


    models = {
        'footballpools.footballpool': {
            'Meta': {'object_name': 'FootballPool'},
            'city_match': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_qnl': ('django.db.models.fields.DateField', [], {}),
            'flag_a_qnl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'flag_b_qnl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'goals_a_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'goals_b_qnl': ('django.db.models.fields.IntegerField', [], {}),
            'group_qnl': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_qnl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'result_qnl': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'team_a_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'team_b_qnl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['footballpools']