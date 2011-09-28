# Create your views here.
from django.http import HttpResponse
from  django.template  import  RequestContext
from  django.shortcuts  import  render_to_response


def index(request):
    return HttpResponse("Hurray an index!")

def add(request, cmdline):
    return HttpResponse("The following job was started: " + cmdline)

def kill(request, job_id):
    return HttpResponse("Killed: " + job_id)

def status(request, job_id):
    return HttpResponse("Status: " + job_id)
