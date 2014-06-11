# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ranking'
        db.create_table('ranking_ranking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_qnl', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pts_goala', self.gf('django.db.models.fields.IntegerField')()),
            ('pts_goalb', self.gf('django.db.models.fields.IntegerField')()),
            ('pts_results', self.gf('django.db.models.fields.IntegerField')()),
            ('pts_winner', self.gf('django.db.models.fields.IntegerField')()),
            ('points_total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ranking', ['Ranking'])


    def backwards(self, orm):
        # Deleting model 'Ranking'
        db.delete_table('ranking_ranking')


    models = {
        'ranking.ranking': {
            'Meta': {'object_name': 'Ranking'},
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points_total': ('django.db.models.fields.IntegerField', [], {}),
            'pts_goala': ('django.db.models.fields.IntegerField', [], {}),
            'pts_goalb': ('django.db.models.fields.IntegerField', [], {}),
            'pts_results': ('django.db.models.fields.IntegerField', [], {}),
            'pts_winner': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ranking']