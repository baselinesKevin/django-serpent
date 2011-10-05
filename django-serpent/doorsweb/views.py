import os
from classes.DXLRunner import DXLRunner, DXLServerRunner
from django.shortcuts import render_to_response


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
     
     d = DXLRunner()
     dx = DXLServerRunner()
     dx.run_dxl(r'ack \"Hello World!\"')
     return render_to_response('status.html', {})