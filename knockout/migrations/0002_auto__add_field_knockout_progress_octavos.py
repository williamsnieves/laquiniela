# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knockout.progress_octavos'
        db.add_column('knockout_knockout', 'progress_octavos',
                      self.gf('django.db.models.fields.CharField')(max_length=6, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knockout.progress_octavos'
        db.delete_column('knockout_knockout', 'progress_octavos')


    models = {
        'knockout.knockout': {
            'Meta': {'object_name': 'Knockout'},
            'clasificado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cod_equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_juego': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'equipo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'goles': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress_octavos': ('django.db.models.fields.CharField', [], {'max_length': '6', 'default': "''"}),
            'puntuacion': ('django.db.models.fields.IntegerField', [], {}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['knockout']