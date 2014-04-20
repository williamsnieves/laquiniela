# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FootballPoolUser'
        db.create_table('footballpoolsusers_footballpooluser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod_qnl', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('footballpoolsusers', ['FootballPoolUser'])


    def backwards(self, orm):
        # Deleting model 'FootballPoolUser'
        db.delete_table('footballpoolsusers_footballpooluser')


    models = {
        'footballpoolsusers.footballpooluser': {
            'Meta': {'object_name': 'FootballPoolUser'},
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['footballpoolsusers']