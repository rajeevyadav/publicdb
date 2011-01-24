from pyamf.remoting.gateway.django import DjangoGateway
from models import *
from django.core.exceptions import ObjectDoesNotExist
from django_publicdb.inforecords.models import *

import datetime
from math import exp

options_timehistogram = ['event time']
options_1dhistogram = ['pulse heights', 'pulse integrals']

import logging
logging.basicConfig(level=logging.INFO, filename='/tmp/test.log')
logger = logging.getLogger('test')

def get_services(request, arg1, arg2):
    logger.info('%r, %r' % (arg1, arg2))
    return services.keys()

def get_timehistogram_options(request):
    return options_timehistogram

def get_timehistogram(request, station_id, date, type):
    options = options_timehistogram
    
    if type == options[0]:
        histogram = get_histogram(station_id, date, 'eventtime')
        data = ['Event time distribution', 'counts per hour']
    else:
        histogram = None

    if histogram:
        data += [histogram.bins, histogram.values]
    else:
        data = None

    return data

def get_1dhistogram_options(request):
    return options_1dhistogram

def get_1dhistogram(request, station_id, date, type):
    options = options_1dhistogram

    if type == options[0]:
        histogram = get_histogram(station_id, date, 'pulseheight')
        data = ['Pulse integral', 'ADC values']
    elif type == options[1]:
        histogram = get_histogram(station_id, date, 'pulseintegral')
        data = ['Pulse integral', 'ADC values * sample']
    else:
        histogram = None

    if histogram:
        data += [histogram.bins, histogram.values]
    else:
        data = None

    return data

def get_histogram(station_id, date, type):
    try:
        summary = Summary.objects.get(station__number=station_id,
                                      date=date)
        histtype = HistogramType.objects.get(slug=type)
        histogram = DailyHistogram.objects.get(source=summary, type=histtype)
    except ObjectDoesNotExist:
        return None
    else:
        return histogram

def get_stations(request):
    """Get HiSPARC stations locations and status

    This function returns an array of dictionaries containing clusters,
    stations and their coordinates as well as status information

    """

    data = get_cluster_station_list(parent=None)

    return data

def get_cluster_station_list(parent):
    if parent:
        clusters = Cluster.objects.filter(parent=parent)
    else:
        clusters = Cluster.objects.filter(parent__isnull=True)

    data = []
    for cluster in clusters:
        c = {}
        c['name'] = cluster.name
        c['status'] = 1.0
        c['contents'] = get_cluster_station_list(parent=cluster)

        for station in Station.objects.filter(cluster=cluster):
            s = {}
            try:
                detector = (DetectorHisparc.objects
                                           .filter(station=station)
                                           .latest('startdate'))
            except ObjectDoesNotExist:
                continue
            s['number'] = station.number
            s['name'] = station.name
            if detector.latitude:
                s['latitude'] = detector.latitude
            else:
                continue
            if detector.longitude:
                s['longitude'] = detector.longitude
            else:
                continue
            try:
                last_data = (Summary.objects
                                    .filter(station=station,
                                            date__lte=datetime.date.today(),
                                            num_events__gt=0)
                                    .latest('date'))
            except Summary.DoesNotExist:
                continue
            days_since_last_data = (datetime.date.today() -
                                    last_data.date).days
            if days_since_last_data <= 1:
                status = 1.
            else:
                # Just some nice exponentially decreasing function
                status = 1 / exp(days_since_last_data / 2.)
            s['status'] = status

            c['contents'].append(s)

        data.append(c)

    return data

def get_station_info(request, station_id):
    """Retrieve a station info page"""

    html = Station.objects.get(number=station_id).info_page
    return "<body>" + html + "</body>"

services = {
    'hisparc.get_services': get_services,
    'hisparc.get_timehistogram_options': get_timehistogram_options,
    'hisparc.get_timehistogram': get_timehistogram,
    'hisparc.get_1dhistogram_options': get_1dhistogram_options,
    'hisparc.get_1dhistogram': get_1dhistogram,
    'hisparc.get_stations': get_stations,
    'hisparc.get_station_info': get_station_info,
}

publicgateway = DjangoGateway(services)
