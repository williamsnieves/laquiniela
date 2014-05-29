# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invitation'
        db.create_table('invitations_invitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('invitacion', self.gf('django.db.models.fields.CharField')(default='', max_length=4)),
        ))
        db.send_create_signal('invitations', ['Invitation'])


    def backwards(self, orm):
        # Deleting model 'Invitation'
        db.delete_table('invitations_invitation')


    models = {
        'invitations.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitacion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['invitations']