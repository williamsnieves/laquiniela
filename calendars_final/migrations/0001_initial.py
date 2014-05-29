# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CalendarFinal'
        db.create_table('calendars_final_calendarfinal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_juego', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cod_equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('goles', self.gf('django.db.models.fields.IntegerField')()),
            ('clasificado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('calendars_final', ['CalendarFinal'])


    def backwards(self, orm):
        # Deleting model 'CalendarFinal'
        db.delete_table('calendars_final_calendarfinal')


    models = {
        'calendars_final.calendarfinal': {
            'Meta': {'object_name': 'CalendarFinal'},
            'clasificado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cod_equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_juego': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'goles': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['calendars_final']