import os

#SETTINGS
DOORS_COMMAND = "C:/Program Files/IBM/Rational/DOORS/bin/dxlips.exe"

# interface and base class
class DXLRunner:
    def __init__(self):
        pass

    def run_dxl_and_get_some_output (self, sFilename):
        pass

# special implementation for DXL Server connection
class DXLServerRunner(DXLRunner):
    def __init__(self):
        self.gDXL_server_started = False

    def run_dxl_and_get_some_output (self, sFilename):
        if not self. gDXL_server_started:
            self.start_dxl_server()
    
    def run_dxl(self, dxlString):
        os.popen(r'call "%s" "%s"' %(DOORS_COMMAND, dxlString) )
        

# special implementation for DXL batch jobs (as RPE does it)
class DXLBatchRunner(DXLRunner):
    def __init__(self):
        pass

    def run_dxl_and_get_some_outout(self, sFilename):
        os.popen("doors.exe -b " + sFilename ) 