import codecs
from nose.tools import *
import os
import netskope
import ConfigParser
import pprint
import csv
import json
import time
import datetime

def test_events():
	pass
	config = ConfigParser.ConfigParser()
	config.read('../configs/netskope.cfg')
	
	apikey = config.get('netskope', 'apikey')
	tenant = config.get('netskope', 'tenant')
	eventtype = 'application'
	timeperiod = 3600
	
	sometime = time.mktime(time.gmtime())
	timerange = [ int(sometime -10000000), int(sometime) ]
	limit = 5000
	skip = 0
	netsk = netskope.netskope(apikey, tenant, debug=False)
	
	#eventsjson = netsk.events('', eventtype, startend=timerange)
		
	while True:
		eventsjson = netsk.events('', eventtype, startend=timerange, limit=limit, skip=skip)
		print len(eventsjson['data'])
		if len(eventsjson['data']) == limit:
			skip = skip + limit
		else:
			break
			
	
	print eventsjson['status']
	
#	for x in eventsjson['data']:
#		None	
		
		#msg = "%s netskope type='%s'" % (str(time.strftime('%Y-%m-%dT%H:%M:%SZ')), eventtype)
		#for k,v in x.iteritems():
		#	msg = "%s %s='%s'" % (msg.strip(), k, v)
		#print msg


'''		
def test_alerts():
	config = ConfigParser.ConfigParser()
	config.read('../configs/netskope.cfg')
	
	apikey = config.get('netskope', 'apikey')
	tenant = config.get('netskope', 'tenant')
	type = 'dlp'
	timeperiod = 604800
	
	sometime = time.mktime(time.gmtime())
	timerange = [ int(sometime -100000), int(sometime) ]
	
	netsk = netskope.netskope(apikey, tenant, debug=False)
	
	#alertsjson = netsk.alerts('', type, startend=timerange)
	alertsjson = netsk.alerts('', type, timeperiod=timeperiod)
	
	for x in alertsjson['data']:
		msg = "%s netskope type='%s'" % (str(time.strftime('%Y-%m-%dT%H:%M:%SZ')), type)
		for k,v in x.iteritems():
			msg = "%s %s='%s'" % (msg.strip(), k, v)
		print msg
		'''