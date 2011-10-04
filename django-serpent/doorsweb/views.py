import subprocess
import os
import tempfile
import re
import mimetypes
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str
from django.conf import settings
from xml.etree.ElementTree import ElementTree

# Create your views here.

def index(request):
     #First open DOORS and run DXL to start DXLServer:
     #   evalTop_ "initDXLServer server 5093"
     #Now the code below will work
     #DOORS_COMMAND = "C:/Program Files/Telelogic/DOORS 9.1/bin/dxlips.exe"
     #PARAMETERS = r'ack \"Hello World!\"'
     #popen(r'"call "%s" "%s"' %(DOORS_COMMAND, PARAMETERS))
     #
     #dxlipf.exe can be used to read a file
     #dxlips.exe can be used to read a string
     
     DOORS_COMMAND = "C:/Program Files/IBM/Rational/DOORS/bin/dxlips.exe"
     PARAMETERS = r'ack \"Hello World!\"'
     os.popen(r'call "%s" "%s"' %(DOORS_COMMAND, PARAMETERS) )
     return render_to_response('status.html', {})