# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Calendar.flag_a_match'
        db.add_column('calendars_calendar', 'flag_a_match',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=200),
                      keep_default=False)

        # Adding field 'Calendar.flag_b_match'
        db.add_column('calendars_calendar', 'flag_b_match',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Calendar.flag_a_match'
        db.delete_column('calendars_calendar', 'flag_a_match')

        # Deleting field 'Calendar.flag_b_match'
        db.delete_column('calendars_calendar', 'flag_b_match')


    models = {
        'calendars.calendar': {
            'Meta': {'object_name': 'Calendar'},
            'city_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cod_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_match': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'flag_a_match': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '200'}),
            'flag_b_match': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '200'}),
            'goals_a_match': ('django.db.models.fields.IntegerField', [], {}),
            'goals_b_match': ('django.db.models.fields.IntegerField', [], {}),
            'group_match': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'result_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team_a_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team_b_match': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['calendars']