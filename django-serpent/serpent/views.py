import subprocess
import os
import tempfile
import re
import mimetypes
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str
from django.conf import settings
from xml.etree.ElementTree import ElementTree

# Create your views here.

def index(request):
    if request.method == "GET":
        return render_to_response('status.html',{'request_method' : "GET"})
    else:
        return render_to_response('status.html',{'module_id' : request.POST['module_id'],
                                                 'request_method' : "POST"})

def createRPEJob(request, module_id):
    
    #RPE wants RPE_HOME set
    os.putenv("RPE_HOME", settings.PATH_TO_RPE_HOME)

    if request.method == "POST":
        t = tempfile.NamedTemporaryFile(suffix='.dsx', delete=False)
        rgx = re.compile(".*\\\\([^\\\\]+).dsx$")
        m = rgx.match(t.name)
        rawfilename = m.group(1) #this gives us just the tempname without the path and .dsx info
        #read and update default DSX
        tree = ElementTree()
        tree.parse(settings.RPE_DEFAULT_DSX)
        dsxFeature = tree.findall("feature") #returns 2 items
        for elem in dsxFeature:
            propertyXML = list(elem.getiterator("property"))
            for attribute in propertyXML:
                thedict = attribute.attrib
                if thedict.has_key('name'):
                    if thedict['name'] == 'module_id':
                        attribute.set('value', module_id)
                    if thedict['name'] == 'path' and thedict['value']=='THISWILLBEREPLACED.doc':
                        attribute.set('value', tempfile.gettempdir() + "\\" + rawfilename + '.doc')
                        
        #now write to temporary DSX file
        tree.write(t.name)

        #submit job to RPE - this doesn't work on Apache2 for some reason
        os.system( settings.PATH_TO_RPE_LAUNCHER + t.name)

        to_return = {'filename' : rawfilename, 'msg' : settings.PATH_TO_RPE_LAUNCHER + rawfilename + '.dsx'}
        serialized = simplejson.dumps(to_return)
        return HttpResponse(serialized, mimetype='application/javascript')
    else:
        if module_id != "":
            return render_to_response('module_redirect.html', { 'module_id' : module_id })
        else:
            return render_to_response('status.html', {})

def download(request, filename):
    if (filename!=None):
        filename = "c:\\temp\\" + filename + ".doc"
        try:
            file = open(filename,"rb")
        except IOError:
            return HttpResponse("ERROR. The file " + filename + " could not be found on the server")
        mimetype = mimetypes.guess_type(filename)[0]
        if not mimetype: mimetype = "application/octet-stream"
        response = HttpResponse(file.read(), mimetype=mimetype)
        response["Content-Disposition"]= "attachment; filename=%s" % os.path.split(filename)[1]
        return response
    else:
        return HttpResponse("What are you trying to do anyway?")

