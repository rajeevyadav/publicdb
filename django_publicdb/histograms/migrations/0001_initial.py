# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Summary'
        db.create_table('histograms_summary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inforecords.Station'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('num_events', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_config', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_errors', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_weather', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('needs_update', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_update_events', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_update_config', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_update_errors', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_update_weather', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('histograms', ['Summary'])

        # Adding unique constraint on 'Summary', fields ['station', 'date']
        db.create_unique('histograms_summary', ['station_id', 'date'])

        # Adding model 'Configuration'
        db.create_table('histograms_configuration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['histograms.Summary'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('gps_latitude', self.gf('django.db.models.fields.FloatField')()),
            ('gps_longitude', self.gf('django.db.models.fields.FloatField')()),
            ('gps_altitude', self.gf('django.db.models.fields.FloatField')()),
            ('mas_version', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('slv_version', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('trig_low_signals', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('trig_high_signals', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('trig_external', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('trig_and_or', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('precoinctime', self.gf('django.db.models.fields.FloatField')()),
            ('coinctime', self.gf('django.db.models.fields.FloatField')()),
            ('postcoinctime', self.gf('django.db.models.fields.FloatField')()),
            ('detnum', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('spare_bytes', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('use_filter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('use_filter_threshold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reduce_data', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('startmode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('delay_screen', self.gf('django.db.models.fields.FloatField')()),
            ('delay_check', self.gf('django.db.models.fields.FloatField')()),
            ('delay_error', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_inttime', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_inttime', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_current', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_current', self.gf('django.db.models.fields.FloatField')()),
            ('mas_comp_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('mas_comp_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('mas_max_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('mas_reset', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mas_ch1_gain_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch1_gain_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch2_gain_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch2_gain_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch1_offset_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch1_offset_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch2_offset_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch2_offset_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_common_offset', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_internal_voltage', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mas_ch1_adc_gain', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_adc_offset', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_adc_gain', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_adc_offset', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_comp_gain', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch1_comp_offset', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_comp_gain', self.gf('django.db.models.fields.FloatField')()),
            ('mas_ch2_comp_offset', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_inttime', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_inttime', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_current', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_current', self.gf('django.db.models.fields.FloatField')()),
            ('slv_comp_thres_low', self.gf('django.db.models.fields.FloatField')()),
            ('slv_comp_thres_high', self.gf('django.db.models.fields.FloatField')()),
            ('slv_max_voltage', self.gf('django.db.models.fields.FloatField')()),
            ('slv_reset', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slv_ch1_gain_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch1_gain_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch2_gain_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch2_gain_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch1_offset_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch1_offset_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch2_offset_pos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch2_offset_neg', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_common_offset', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_internal_voltage', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slv_ch1_adc_gain', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_adc_offset', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_adc_gain', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_adc_offset', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_comp_gain', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch1_comp_offset', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_comp_gain', self.gf('django.db.models.fields.FloatField')()),
            ('slv_ch2_comp_offset', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('histograms', ['Configuration'])

        # Adding model 'DailyHistogram'
        db.create_table('histograms_dailyhistogram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['histograms.Summary'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['histograms.HistogramType'])),
            ('bins', self.gf('django_publicdb.histograms.models.SerializedDataField')()),
            ('values', self.gf('django_publicdb.histograms.models.SerializedDataField')()),
        ))
        db.send_create_signal('histograms', ['DailyHistogram'])

        # Adding unique constraint on 'DailyHistogram', fields ['source', 'type']
        db.create_unique('histograms_dailyhistogram', ['source_id', 'type_id'])

        # Adding model 'DailyDataset'
        db.create_table('histograms_dailydataset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['histograms.Summary'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['histograms.DatasetType'])),
            ('x', self.gf('django_publicdb.histograms.models.SerializedDataField')()),
            ('y', self.gf('django_publicdb.histograms.models.SerializedDataField')()),
        ))
        db.send_create_signal('histograms', ['DailyDataset'])

        # Adding unique constraint on 'DailyDataset', fields ['source', 'type']
        db.create_unique('histograms_dailydataset', ['source_id', 'type_id'])

        # Adding model 'HistogramType'
        db.create_table('histograms_histogramtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('has_multiple_datasets', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bin_axis_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('value_axis_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('histograms', ['HistogramType'])

        # Adding model 'DatasetType'
        db.create_table('histograms_datasettype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('x_axis_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('y_axis_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('histograms', ['DatasetType'])

        # Adding model 'GeneratorState'
        db.create_table('histograms_generatorstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('check_last_run', self.gf('django.db.models.fields.DateTimeField')()),
            ('check_is_running', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('update_last_run', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_is_running', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('histograms', ['GeneratorState'])


    def backwards(self, orm):
        # Removing unique constraint on 'DailyDataset', fields ['source', 'type']
        db.delete_unique('histograms_dailydataset', ['source_id', 'type_id'])

        # Removing unique constraint on 'DailyHistogram', fields ['source', 'type']
        db.delete_unique('histograms_dailyhistogram', ['source_id', 'type_id'])

        # Removing unique constraint on 'Summary', fields ['station', 'date']
        db.delete_unique('histograms_summary', ['station_id', 'date'])

        # Deleting model 'Summary'
        db.delete_table('histograms_summary')

        # Deleting model 'Configuration'
        db.delete_table('histograms_configuration')

        # Deleting model 'DailyHistogram'
        db.delete_table('histograms_dailyhistogram')

        # Deleting model 'DailyDataset'
        db.delete_table('histograms_dailydataset')

        # Deleting model 'HistogramType'
        db.delete_table('histograms_histogramtype')

        # Deleting model 'DatasetType'
        db.delete_table('histograms_datasettype')

        # Deleting model 'GeneratorState'
        db.delete_table('histograms_generatorstate')


    models = {
        'histograms.configuration': {
            'Meta': {'object_name': 'Configuration'},
            'coinctime': ('django.db.models.fields.FloatField', [], {}),
            'delay_check': ('django.db.models.fields.FloatField', [], {}),
            'delay_error': ('django.db.models.fields.FloatField', [], {}),
            'delay_screen': ('django.db.models.fields.FloatField', [], {}),
            'detnum': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gps_altitude': ('django.db.models.fields.FloatField', [], {}),
            'gps_latitude': ('django.db.models.fields.FloatField', [], {}),
            'gps_longitude': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas_ch1_adc_gain': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_adc_offset': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_comp_gain': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_comp_offset': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_current': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_gain_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch1_gain_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch1_inttime': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_offset_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch1_offset_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch1_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch1_voltage': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_adc_gain': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_adc_offset': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_comp_gain': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_comp_offset': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_current': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_gain_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch2_gain_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch2_inttime': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_offset_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch2_offset_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_ch2_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'mas_ch2_voltage': ('django.db.models.fields.FloatField', [], {}),
            'mas_common_offset': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_comp_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'mas_comp_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'mas_internal_voltage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'mas_max_voltage': ('django.db.models.fields.FloatField', [], {}),
            'mas_reset': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mas_version': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'postcoinctime': ('django.db.models.fields.FloatField', [], {}),
            'precoinctime': ('django.db.models.fields.FloatField', [], {}),
            'reduce_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slv_ch1_adc_gain': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_adc_offset': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_comp_gain': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_comp_offset': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_current': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_gain_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch1_gain_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch1_inttime': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_offset_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch1_offset_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch1_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch1_voltage': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_adc_gain': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_adc_offset': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_comp_gain': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_comp_offset': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_current': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_gain_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch2_gain_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch2_inttime': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_offset_neg': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch2_offset_pos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_ch2_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'slv_ch2_voltage': ('django.db.models.fields.FloatField', [], {}),
            'slv_common_offset': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_comp_thres_high': ('django.db.models.fields.FloatField', [], {}),
            'slv_comp_thres_low': ('django.db.models.fields.FloatField', [], {}),
            'slv_internal_voltage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slv_max_voltage': ('django.db.models.fields.FloatField', [], {}),
            'slv_reset': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slv_version': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['histograms.Summary']"}),
            'spare_bytes': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'startmode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'trig_and_or': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trig_external': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'trig_high_signals': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'trig_low_signals': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'use_filter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_filter_threshold': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'histograms.dailydataset': {
            'Meta': {'ordering': "('source', 'type')", 'unique_together': "(('source', 'type'),)", 'object_name': 'DailyDataset'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['histograms.Summary']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['histograms.DatasetType']"}),
            'x': ('django_publicdb.histograms.models.SerializedDataField', [], {}),
            'y': ('django_publicdb.histograms.models.SerializedDataField', [], {})
        },
        'histograms.dailyhistogram': {
            'Meta': {'ordering': "('source', 'type')", 'unique_together': "(('source', 'type'),)", 'object_name': 'DailyHistogram'},
            'bins': ('django_publicdb.histograms.models.SerializedDataField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['histograms.Summary']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['histograms.HistogramType']"}),
            'values': ('django_publicdb.histograms.models.SerializedDataField', [], {})
        },
        'histograms.datasettype': {
            'Meta': {'object_name': 'DatasetType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'x_axis_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'y_axis_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'histograms.generatorstate': {
            'Meta': {'object_name': 'GeneratorState'},
            'check_is_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'check_last_run': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'update_is_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'update_last_run': ('django.db.models.fields.DateTimeField', [], {})
        },
        'histograms.histogramtype': {
            'Meta': {'object_name': 'HistogramType'},
            'bin_axis_title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_multiple_datasets': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'value_axis_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'histograms.summary': {
            'Meta': {'ordering': "('date', 'station')", 'unique_together': "(('station', 'date'),)", 'object_name': 'Summary'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_update': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_update_config': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_update_errors': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_update_events': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'needs_update_weather': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_config': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_errors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_events': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_weather': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inforecords.Station']"})
        },
        'inforecords.cluster': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Cluster'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clusters'", 'to': "orm['inforecords.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['inforecords.Cluster']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'inforecords.contact': {
            'Meta': {'ordering': "('surname', 'first_name')", 'unique_together': "[('first_name', 'prefix_surname', 'surname')]", 'object_name': 'Contact'},
            'contactinformation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['inforecords.ContactInformation']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix_surname': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'profession': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inforecords.Profession']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'inforecords.contactinformation': {
            'Meta': {'ordering': "['city', 'street_1', 'email_work']", 'object_name': 'ContactInformation'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'email_private': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_work': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pobox': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pobox_city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'pobox_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'inforecords.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        'inforecords.profession': {
            'Meta': {'object_name': 'Profession'},
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'inforecords.station': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Station'},
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': "orm['inforecords.Cluster']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations_contact'", 'null': 'True', 'to': "orm['inforecords.Contact']"}),
            'contactinformation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations'", 'to': "orm['inforecords.ContactInformation']"}),
            'ict_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stations_ict_contact'", 'null': 'True', 'to': "orm['inforecords.Contact']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_page': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['histograms']