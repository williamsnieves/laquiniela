# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quarter'
        db.create_table('quarter_quarter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_qnl', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cod_juego', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('cod_equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('equipo', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('goles', self.gf('django.db.models.fields.IntegerField')()),
            ('clasificado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('puntuacion', self.gf('django.db.models.fields.IntegerField')()),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('quarter', ['Quarter'])


    def backwards(self, orm):
        # Deleting model 'Quarter'
        db.delete_table('quarter_quarter')


    models = {
        'quarter.quarter': {
            'Meta': {'object_name': 'Quarter'},
            'clasificado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cod_equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_juego': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'goles': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntuacion': ('django.db.models.fields.IntegerField', [], {}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['quarter']