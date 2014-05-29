# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Curiosidad'
        db.create_table('curiosidades_curiosidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_mundial', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('copa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ano_mundial', self.gf('django.db.models.fields.IntegerField')()),
            ('pais_sede', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cant_equipos', self.gf('django.db.models.fields.IntegerField')()),
            ('cant_partidos', self.gf('django.db.models.fields.IntegerField')()),
            ('cant_goles', self.gf('django.db.models.fields.IntegerField')()),
            ('promedio_goles', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('campeon', self.gf('django.db.models.fields.IntegerField')()),
            ('subcampeon', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tercero', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('cuarto', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('goleadores', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('max_goles', self.gf('django.db.models.fields.IntegerField')()),
            ('balon_oro', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fairplay', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal('curiosidades', ['Curiosidad'])


    def backwards(self, orm):
        # Deleting model 'Curiosidad'
        db.delete_table('curiosidades_curiosidad')


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