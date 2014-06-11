# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Semifinal'
        db.create_table('semifinal_semifinal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_qnl', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cod_juego', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cod_equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('goles', self.gf('django.db.models.fields.IntegerField')()),
            ('clasificado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('puntuacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('progress_semis', self.gf('django.db.models.fields.CharField')(default='', max_length=6)),
        ))
        db.send_create_signal('semifinal', ['Semifinal'])


    def backwards(self, orm):
        # Deleting model 'Semifinal'
        db.delete_table('semifinal_semifinal')


    models = {
        'semifinal.semifinal': {
            'Meta': {'object_name': 'Semifinal'},
            'clasificado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cod_equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_juego': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'goles': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress_semis': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6'}),
            'puntuacion': ('django.db.models.fields.IntegerField', [], {}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['semifinal']