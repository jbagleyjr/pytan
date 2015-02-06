
"""
Get a sensor by id
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}
kwargs["objtype"] = u'sensor'
kwargs["id"] = 1

# call the handler with the get method, passing in kwargs for arguments
response = handler.get(**kwargs)

print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "length of response (number of objects returned): "
print len(response)

print ""
print "print the first object returned in JSON format:"
out = response.to_json(response[0])
if len(out.splitlines()) > 15:
    out = out.splitlines()[0:15]
    out.append('..trimmed for brevity..')
    out = '\n'.join(out)

print out



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258

Type of response:  <class 'taniumpy.object_types.sensor_list.SensorList'>

print of response:
SensorList, len: 1

length of response (number of objects returned): 
1

print the first object returned in JSON format:
{
  "_type": "sensor", 
  "category": "Reserved", 
  "description": "The recorded state of each action a client has taken recently in the form of id:status.\nExample: 1:Completed", 
  "exclude_from_parse_flag": 1, 
  "hash": 1792443391, 
  "hidden_flag": 0, 
  "id": 1, 
  "ignore_case_flag": 1, 
  "max_age_seconds": 3600, 
  "name": "Action Statuses", 
  "queries": {
    "_type": "queries", 
    "query": [
      {
..trimmed for brevity..

'''