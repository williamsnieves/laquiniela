# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table('teams_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_team', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country_team', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('confed_team', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('group_team', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('cant_titles', self.gf('django.db.models.fields.IntegerField')()),
            ('mundiales', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('teams', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table('teams_team')


    models = {
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'cant_titles': ('django.db.models.fields.IntegerField', [], {}),
            'confed_team': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country_team': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'group_team': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mundiales': ('django.db.models.fields.IntegerField', [], {}),
            'name_team': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['teams']