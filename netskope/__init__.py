#!/usr/bin/env/ python
#AUTHOR: JOSH MADELEY
#VERSION: 0.1

import httplib2
import time
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
			try:
				return resp['status']
			except:
				raise ValueError('something bad hapepned making the request to ' + url)
				return False
########################################################################################			
	def events(self,query, type, **kwargs):
		#timeperiod = int (3600. 86400, 604800,2592000)
		#startend = [start, end] uniz epoch time
		#limit = int < 5000
		#skip = int 
		
		allowedtypes = ['connection', 'application', 'audit']
		if self._inlist(type, allowedtypes) != True:
			raise ValueError('Type must be a string with one of the following values [connection, application, audit]')
		
		eventsurl = self.url + 'events'
		
		try: timeperiod = kwargs['timeperiod']
		except:timeperiod = None
		
		try: startend = kwargs['startend']
		except:startend = None
		
		try:limit = kwargs['limit']
		except:limit = 5000
		
		try:skip = kwargs['skip']
		except:skip = 0
		
		if timeperiod == None and startend == None:
			raise ValueError('Must set either timeperiod or startend (as a list of unix epoch time)')
		
		if timeperiod == None:
			if isinstance(startend, list):

				params={'token':self.apikey, 'type':type, 'query':query,'starttime':startend[0],'endtime':startend[1], 'limit':limit, 'skip':skip}
				requrl = eventsurl + "?" + urllib.urlencode(params)
				print requrl

			else:
				raise ValueError('startend must be a list')
		elif startend == None:				#USING TIMEPERIOD
			if isinstance(timeperiod, int):

				params={'token':self.apikey, 'type':type, 'query':query,'timeperiod':timeperiod, 'limit':limit, 'skip':skip}
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
	def report(self, query, type, **kwargs):
		None
########################################################################################	
	def userconfig(self,email, configtype):
		None
########################################################################################	
	def quarentine(self, op, **kwargs):
		None
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