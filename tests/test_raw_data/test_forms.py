import datetime

from os.path import abspath, dirname, join

from django.test import Client, TestCase, override_settings
from django.urls import reverse

from publicdb.raw_data.forms import CoincidenceDownloadForm, DataDownloadForm

from ..factories import histograms_factories, inforecords_factories


class TestDataDownloadForm(TestCase):

    def setUp(self):
        # Required models
        cluster = inforecords_factories.ClusterFactory(name='Amsterdam', number=0, country__number=0)
        self.station = inforecords_factories.StationFactory(name='Nikhef', number=501, cluster=cluster)
        self.summary = histograms_factories.SummaryFactory(
            station=self.station, date=datetime.date(2017, 1, 1),
            needs_update_events=False, num_events=168,
            needs_update_weather=False, num_weather=60,
            needs_update_config=False, num_config=1,
            needs_update_singles=False, num_singles=301,
            needs_update=False,
        )

    def test_clean_valid(self):
        valid_form_data = [
            {'data_type': 'events', 'station_events': self.station.id, 'start': '2017-1-1', 'end': '2017-1-2'},
            {'data_type': 'weather', 'station_weather': self.station.id, 'start': '2017-1-1', 'end': '2017-1-2'},
            {'data_type': 'singles', 'station_singles': self.station.id, 'start': '2017-1-1', 'end': '2017-1-2'},
            {'data_type': 'lightning', 'lightning_type': 0, 'start': '2014-10-1', 'end': '2014-11-4'},
        ]
        for data in valid_form_data:
            form = DataDownloadForm(data)
            self.assertTrue(form.is_valid(), form.errors.as_json())

    def test_clean_invalid(self):
        invalid_form_data = [
            {'data_type': 'events', 'station_weather': self.station.id, 'start': '2017-1-1', 'end': '2017-1-2'},
            {'data_type': 'weather', 'station_events': self.station.id, 'start': '2017-1-1', 'end': '2017-1-2'},
            {'data_type': 'lightning', 'lightning_type': 10, 'start': '2014-10-1', 'end': '2014-11-4'},
            {'data_type': 'events', 'station_events': self.station.id},
        ]
        for data in invalid_form_data:
            form = DataDownloadForm(data)
            self.assertFalse(form.is_valid())


class TestCoincidenceDownloadForm(TestCase):

    def setUp(self):
        # Required models
        cluster = inforecords_factories.ClusterFactory(name='Amsterdam', number=0, country__number=0)
        self.station = inforecords_factories.StationFactory(name='Nikhef', number=501, cluster=cluster)
        self.summary = histograms_factories.SummaryFactory(
            station=self.station, date=datetime.date(2017, 1, 1),
            needs_update_events=False, num_events=168,
            needs_update_weather=False, num_weather=60,
            needs_update_config=False, num_config=1,
            needs_update_singles=False, num_singles=301,
            needs_update=False,
        )

    def test_clean_valid(self):
        valid_form_data = [
            {'filter_by': 'network', 'start': '2017-1-1', 'end': '2017-1-2', 'n': 2},
        ]
        for data in valid_form_data:
            form = CoincidenceDownloadForm(data)
            self.assertTrue(form.is_valid(), form.errors.as_json())

    def test_clean_invalid(self):
        invalid_form_data = [
            {'filter_by': 'cluster', 'start': '2017-1-1', 'end': '2017-1-2', 'n': 2},
        ]
        for data in invalid_form_data:
            form = CoincidenceDownloadForm(data)
            self.assertFalse(form.is_valid())
