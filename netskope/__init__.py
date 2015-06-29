#!/usr/bin/env/ python
#AUTHOR: JOSH MADELEY
#VERSION: 0.1

import httplib2
import ssl
import re
import time
import logging
import os
import json
import urllib

class netskope(object):

	def __init__(self, apikey, tenant, debug=False):
		 
		self.apikey = apikey
		self.tenant = tenant
		self.url = 'https://' + self.tenant + '.goskope.com/api/v1/'
		self.debug = debug
		 
		if self.debug == True:
			httplib2.debuglevel = 1
		 
		self.h = httplib2.Http()
########################################################################################
	def _makerequest(self, url):

		resp, content = self.h.request(url, method='GET')
		
		if resp['status'] == str(200):
			return json.loads(content)
		else:
			return False	#SHOULD RETURN AN ERROR CODE
########################################################################################			
	def events(self,query, type, **kwargs):
		#timeperiod = int (3600. 86400, 604800,2592000)
		#startend = [start, end] uniz epoch time
		#limit = int < 5000
		#skip = int 
						
		eventsurl = self.url + 'events'
		
		try: timeperiod = kwargs['timeperiod']
		except:timeperiod = None
		
		try: startend = kwargs['startend']
		except:startend = None
		
		try:limit = kwargs['limit']
		except:limit = None
		
		try:limit = kwargs['skip']
		except:limit = None
		
		if timeperiod == None and startend == None:
			raise ValueError('Must set either timeperiod or startend (as a list of unix epoch time)')
		
		if timeperiod == None:
			if isinstance(startend, list):

				params={'token':self.apikey, 'type':type, 'query':query,'starttime':startend[0],'endtime':startend[1]}
				requrl = eventsurl + "?" + urllib.urlencode(params)

			else:
				raise ValueError('startend must be a list')
		elif startend == None:				#USING TIMEPERIOD
			if isinstance(timeperiod, int):

				params={'token':self.apikey, 'type':type, 'query':query,'timeperiod':timeperiod}
				requrl = eventsurl + "?" + urllib.urlencode(params)
				
			else:
				raise ValueError('timeperiod must be an integer')
		else:
			raise ValueError('The parameters are not correct')
		
		return self._makerequest(requrl)
########################################################################################					
	def alerts(self,query, type, **kwargs):
		#timeperiod = int (3600. 86400, 604800,2592000)
		#startend = (start, end) uniz epoch time
		#limit = int < 5000
		#skip = int 
		
		alertsurl = self.url + 'alerts'
		
		try: timeperiod = kwargs['timeperiod']
		except:timeperiod = None
		
		try: startend = kwargs['startend']
		except:startend = None
		
		try:limit = kwargs['limit']
		except:limit = None
		
		try:limit = kwargs['skip']
		except:limit = None
		
		if timeperiod == None and startend == None:
			raise ValueError('Must set either timeperiod or startend (as a list)')
		
		if timeperiod == None:
			if isinstance(startend, list):
				params={'query':query, 'token':self.apikey, 'starttime':startend[0], 'endtime':startend[1]}
				requrl = alertsurl + "?" + urllib.urlencode(params)
			else:
				raise ValueError('startend must be a list with a two unix epoch times')
		
		elif startend == None:
			if isinstance(timeperiod, int):
			
				params={'token':self.apikey, 'type':type, 'query':query,'timeperiod':timeperiod}
				requrl = alertsurl + "?" + urllib.urlencode(params)
			else:
				raise ValueError('Timeperiod must be an integer with the following values 3600 | 86400 | 604800 | 2592000')
		else:
			raise ValueError('The parameters are not correct')

		return self._makerequest(requrl)
########################################################################################		
	def logstatus(self,query, type, **kwargs):
		None			
########################################################################################	
	def sendsyslog(self,msg, syslogserver, port=514, ratelimit=0.1):
		try:
			from logging.handlers import SysLogHandler
			syslogger = logging.getLogger('syslog')
			syslogger.setLevel(logging.INFO)
			syslog = SysLogHandler((syslogserver, port))
			syslogger.addHandler(syslog)
		except Exception, err:
				raise #Exception("failed to start logger")
			
		try:
			syslogger.info(msg)
	
			time.sleep(ratelimit)
			return True
		except Exception, err:
			raise #Exception('FAILED TO SEND') #SHOULD LOG SOMEWHERE
########################################################################################	
	def _inlist(self, val, lst):
		
		try:
			ret = lst.index(val)
		except ValueError:
			ret = -1
			
		if ret > -1:
			return True
		else:
			return False