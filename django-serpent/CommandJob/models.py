from django.db import models
from src import subprocess
import threading

class CmdJobThread: 
    def execute(self):
        # open DOORS batch process for code 
        self.process = subprocess.Popen(self.cmd, shell=False, bufsize = 1,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.output = ""

        while ( self.process.poll() < 0):
            pollresult = self.process.asyncread(timeout=0.25)
            if (pollresult): self.output += pollresult 
        
        # make sure the process has ended
        self.status = self.process.wait() 
        # read std err ...
        self.stderr = ""
        if self.process.stderr: self.stderr = self.process.stderr.read()

        
    def __init__(self, command):
        # create temporary file for DXL code 
        self.cmd = command
        self.status = ""
        self.thread = threading.Thread(target = lambda: self.execute() )
        self.thread.start() 

class  CmdJob(models.Model):
    STATUS_CHOICES = ( ('R', 'Running'), 
                       ('F', 'Finished'))
    
    code    =  models.TextField()
    output  =  models.TextField()
    status  =  models.CharField(max_length = 1, choices = STATUS_CHOICES) 
    
    def  __unicode__(self):
        return  self.questionye



