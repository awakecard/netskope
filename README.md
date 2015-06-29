# netskope
This library will provide an interface to the netskope REST API. Once this is complete, each message that is collected can be forward to a SIEM using syslog. The syslog interface will likely come direct from the Python Standard Library and just be configured here.

###Requirements
httplib2 0.9.1

###Development Status
https://<tenant>.goskope.com/api/v1/  
	events - partially working  (pagination added - no error checking)  
	alerts - partially working (pagination added - no error checking)  
	logstatus - not started  
	report - not started  
	userconfig - not started  
	quarentine - not started  
