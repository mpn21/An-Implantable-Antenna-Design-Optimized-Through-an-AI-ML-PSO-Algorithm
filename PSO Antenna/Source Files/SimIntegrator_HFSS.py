#############################
#Author: Michael Nguyuen
#Purpose: Class to handle HFSS Simulation Script 
#Recognition: Lauren Linkous, linkouslc@vcu.edu 
#Note: Class modulator below uses subprocess to manage HFSS 
#############################

import subprocess 

# Class Constructor 
class SimIntegrator_HFSS:
    def __init__(self, simPath, license=1):
        self.numSimsRunning = 0
        self.simulationSoftwarePath = simPath
        self.numLicense = license
        self.p = -1 #return code for polling

        self.AT = None
        self.ST = None

        self.projDir=None

    ##########################################################
    # HFSS software integration functions
    ###########################################################

    def HFSSrunWithScript(self, sim, newSession=True):
        cmds = [self.simulationSoftwarePath, "-RunScript", sim]
        self.HFSSrunProcess(cmds, newSession)
        self.HFSSwaitUntilComplete()

    def HFSSrunProcess(self, cmds, newSession):
        proc = self.HFSScheckRunningProcess()
        if proc == -1:
            self.p = subprocess.Popen(cmds, start_new_session=newSession, )
        else: 
            self.HFSSwaitUntilComplete()
            #dlg = MessageDialog(None, "A simulation thread is currently running. Do you want to stop it and start another?",'Stop simulation?', YES_NO| ICON_QUESTION)
            #result = dlg.ShowModal()
            #if result == ID_YES:
                #self.p.kill()
                #self.p.terminate()
                #self.p = None
                #self.p = subprocess.Popen(cmds, start_new_session=newSession)
                #self.p.wait()

    def HFSScheckRunningProcess(self):
        try:
            stat = self.p.poll()
            if stat == 0:
                self.HFSSmarkProcessFinished()
            return stat
        except:
            return -1

    def HFSSmarkProcessFinished(self):
        self.p = -1

    def HFSSwaitUntilComplete(self):
        poll = self.p.wait()
        #While loop below is no longer required, but may be required if subProcess.Popen acts up
        #print(poll) poll = zero when running; NONE when closed
        #while(poll == 0):
            #print(seconds)
            #time.sleep(1)
            #seconds=seconds+1
            #poll = self.p.wait()


