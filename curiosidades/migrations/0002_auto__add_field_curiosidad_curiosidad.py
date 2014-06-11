# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Curiosidad.curiosidad'
        db.add_column('curiosidades_curiosidad', 'curiosidad',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Curiosidad.curiosidad'
        db.delete_column('curiosidades_curiosidad', 'curiosidad')


    models = {
        'curiosidades.curiosidad': {
            'Meta': {'object_name': 'Curiosidad'},
            'ano_mundial': ('django.db.models.fields.IntegerField', [], {}),
            'balon_oro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'campeon': ('django.db.models.fields.IntegerField', [], {}),
            'cant_equipos': ('django.db.models.fields.IntegerField', [], {}),
            'cant_goles': ('django.db.models.fields.IntegerField', [], {}),
            'cant_partidos': ('django.db.models.fields.IntegerField', [], {}),
            'cod_mundial': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'copa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cuarto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'curiosidad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'fairplay': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'goleadores': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_goles': ('django.db.models.fields.IntegerField', [], {}),
            'pais_sede': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'promedio_goles': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'subcampeon': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tercero': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['curiosidades']