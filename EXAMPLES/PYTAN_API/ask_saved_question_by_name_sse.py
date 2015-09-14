#!/usr/bin/env python
"""
Ask a saved question by referencing the name of a saved question in a string and use Server Side Export when performing a GetResultData
"""
# import the basic python packages we need
import os
import sys
import tempfile
import pprint
import traceback

# disable python from generating a .pyc file
sys.dont_write_bytecode = True

# change me to the path of pytan if this script is not running from EXAMPLES/PYTAN_API
pytan_loc = "~/gh/pytan"
pytan_static_path = os.path.join(os.path.expanduser(pytan_loc), 'lib')

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# try to automatically determine the pytan lib directory by assuming it is in '../../lib/'
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')

# add pytan_loc and lib_dir to the PYTHONPATH variable
path_adds = [lib_dir, pytan_static_path]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

# import pytan
import pytan

# create a dictionary of arguments for the pytan handler
handler_args = {}

# establish our connection info for the Tanium Server
handler_args['username'] = "Administrator"
handler_args['password'] = "Tanium2015!"
handler_args['host'] = "10.0.1.240"
handler_args['port'] = "443"  # optional

# optional, level 0 is no output except warnings/errors
# level 1 through 12 are more and more verbose
handler_args['loglevel'] = 1

# optional, use a debug format for the logging output (uses two lines per log entry)
handler_args['debugformat'] = False

# optional, this saves all response objects to handler.session.ALL_REQUESTS_RESPONSES
# very useful for capturing the full exchange of XML requests and responses
handler_args['record_all_requests'] = True

# instantiate a handler using all of the arguments in the handler_args dictionary
print "...CALLING: pytan.handler() with args: {}".format(handler_args)
handler = pytan.Handler(**handler_args)

# print out the handler string
print "...OUTPUT: handler string: {}".format(handler)

# setup the arguments for the handler() class
kwargs = {}
kwargs["sse"] = True
kwargs["qtype"] = u'saved'
kwargs["name"] = u'Installed Applications'

print "...CALLING: handler.ask with args: {}".format(kwargs)
response = handler.ask(**kwargs)

print "...OUTPUT: Type of response: ", type(response)

print "...OUTPUT: Pretty print of response:"
print pprint.pformat(response)

print "...OUTPUT: Equivalent Question if it were to be asked in the Tanium Console: "
print response['question_object'].query_text

if response['question_results']:
    # call the export_obj() method to convert response to CSV and store it in out
    export_kwargs = {}
    export_kwargs['obj'] = response['question_results']
    export_kwargs['export_format'] = 'csv'

    print "...CALLING: handler.export_obj() with args {}".format(export_kwargs)
    out = handler.export_obj(**export_kwargs)

    # trim the output if it is more than 15 lines long
    if len(out.splitlines()) > 15:
        out = out.splitlines()[0:15]
        out.append('..trimmed for brevity..')
        out = '\n'.join(out)

    print "...OUTPUT: CSV Results of response: "
    print out

'''STDOUT from running this:
...CALLING: pytan.handler() with args: {'username': 'Administrator', 'record_all_requests': True, 'loglevel': 1, 'debugformat': False, 'host': '10.0.1.240', 'password': 'Tanium2015!', 'port': '443'}
...OUTPUT: handler string: PyTan v2.1.4 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
...CALLING: handler.ask with args: {'sse': True, 'qtype': u'saved', 'name': u'Installed Applications'}
2015-09-14 20:15:16,326 INFO     pytan.pollers.SSEPoller: ID '1/495576890344.xml': Server Side Export Completed: 'Completed. 1004 rows written.'
...OUTPUT: Type of response:  <type 'dict'>
...OUTPUT: Pretty print of response:
{'poller_object': None,
 'poller_success': None,
 'question_object': <taniumpy.object_types.question.Question object at 0x106b8aa50>,
 'question_results': <taniumpy.object_types.result_set.ResultSet object at 0x10c6128d0>,
 'saved_question_object': <taniumpy.object_types.saved_question.SavedQuestion object at 0x106b8afd0>}
...OUTPUT: Equivalent Question if it were to be asked in the Tanium Console: 
Get Installed Applications from all machines
...CALLING: handler.export_obj() with args {'export_format': 'csv', 'obj': <taniumpy.object_types.result_set.ResultSet object at 0x10c6128d0>}
...OUTPUT: CSV Results of response: 
Count,Installed Applications,Installed Applications,Installed Applications,Installed Applications
755,[too many results],[too many results],[too many results],[too many results]
1,libminiupnpc8,libminiupnpc8,libminiupnpc8,libminiupnpc8
1,iso-codes,iso-codes,iso-codes,iso-codes
1,libexttextcat-2.0-0,libexttextcat-2.0-0,libexttextcat-2.0-0,libexttextcat-2.0-0
1,growisofs,growisofs,growisofs,growisofs
1,libxml2:i386,libxml2:i386,libxml2:i386,libxml2:i386
1,libsm6:i386,libsm6:i386,libsm6:i386,libsm6:i386
1,findutils,findutils,findutils,findutils
1,libgcr-base-3-1:i386,libgcr-base-3-1:i386,libgcr-base-3-1:i386,libgcr-base-3-1:i386
1,thunderbird-locale-en,thunderbird-locale-en,thunderbird-locale-en,thunderbird-locale-en
1,usb-modeswitch,usb-modeswitch,usb-modeswitch,usb-modeswitch
1,gstreamer1.0-alsa:i386,gstreamer1.0-alsa:i386,gstreamer1.0-alsa:i386,gstreamer1.0-alsa:i386
1,libcomerr2:i386,libcomerr2:i386,libcomerr2:i386,libcomerr2:i386
1,libqt5sensors5:i386,libqt5sensors5:i386,libqt5sensors5:i386,libqt5sensors5:i386
..trimmed for brevity..

'''

'''STDERR from running this:

'''
