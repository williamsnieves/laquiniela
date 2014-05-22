# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FootballPoolUser.qnl_complete'
        db.add_column('footballpoolsusers_footballpooluser', 'qnl_complete',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FootballPoolUser.qnl_complete'
        db.delete_column('footballpoolsusers_footballpooluser', 'qnl_complete')


    models = {
        'footballpoolsusers.footballpooluser': {
            'Meta': {'object_name': 'FootballPoolUser'},
            'cod_qnl': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qnl_complete': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['footballpoolsusers']