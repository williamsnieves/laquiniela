# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendar'
        db.create_table('calendars_calendar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_match', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cod_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_match', self.gf('django.db.models.fields.DateField')()),
            ('city_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('team_a_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('goals_a_match', self.gf('django.db.models.fields.IntegerField')()),
            ('team_b_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('goals_b_match', self.gf('django.db.models.fields.IntegerField')()),
            ('result_match', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('calendars', ['Calendar'])


    def backwards(self, orm):
        # Deleting model 'Calendar'
        db.delete_table('calendars_calendar')


    models = {
        'calendars.calendar': {
            'Meta': {'object_name': 'Calendar'},
            'city_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cod_match': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_match': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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