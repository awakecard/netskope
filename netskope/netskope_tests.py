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

def test_basicquery():
	
	config = ConfigParser.ConfigParser()
	config.read('../configs/netskope.cfg')
	
	apikey = config.get('netskope', 'apikey')
	tenant = config.get('netskope', 'tenant')
	eventtype = 'application'
	timeperiod = 3600
	
	sometime = time.mktime(time.gmtime())
	timerange = [ int(sometime -100000), int(sometime) ]

	netsk = netskope.netskope(apikey, tenant, debug=False)
	
	somejson = netsk.events('', eventtype, startend=timerange)
	#somejson = netsk.events('', eventtype, timeperiod=3600)
	
	
	print somejson['status']
	for x in somejson['data']:
		msg = "%s netskope type='%s'" % (str(time.strftime('%Y-%m-%dT%H:%M:%SZ')), eventtype)
		for k,v in x.iteritems():
			msg = "%s %s='%s'" % (msg, k, v)
		print msg
		#netsk.sendsyslog(msg.strip(), '192.168.149.141') 