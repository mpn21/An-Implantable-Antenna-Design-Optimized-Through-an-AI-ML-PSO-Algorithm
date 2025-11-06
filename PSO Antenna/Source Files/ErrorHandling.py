#############################
#Author: Michael Nguyuen
#Purpose: Manage the errors and anomalies from ANSYS/HFSS 
#Note: The ErrorHandling script exports the Message from ANSYS/HFSS MessageManager into 
# the message manager folder and is stored in message.txt. 
# This section will read the message and returns which error message is discovered
#############################

class MessageManager:
    def __init__(self, MessageManager_PATH, MessageManager_FILENAME):
        self.Path = MessageManager_PATH
        self.FileName_MessageManger = MessageManager_FILENAME
        self.Keyword_Pass = 'Normal completion'
        self.Keyword_1 = 'non-conducting edge'
        self.Keyword_2 = 'Too few conductors'
        self.Keyword_3 = 'aborted by user'
        self.Keyword_4 = 'hf3d exited with code'
        self.Keyword_5 = 'MPI failed'
        self.Keyword_6 = 'did NOT converge.'
        self.Keyword_7 = 'Cannot connect to license server system'
        self.Keyword_8 = 'non-responsive'
        self.errorflag = 0

    def MessageManagerFile(self):
        MessageManager_File = self.Path + self.FileName_MessageManger
        return MessageManager_File
        
    def Find_Error(self):
        MessageFile = self.MessageManagerFile()
        Pass=self.Keyword_Pass
        Keyword1=self.Keyword_1
        Keyword2=self.Keyword_2
        Keyword3=self.Keyword_3
        Keyword4=self.Keyword_4
        Keyword5=self.Keyword_5
        Keyword6=self.Keyword_6
        Keyword7=self.Keyword_7
        Keyword8=self.Keyword_8
        flag = self.errorflag 
        
        with open(MessageFile, 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(Pass) != -1:
                    flag = False
                if line.find(Keyword1) != -1:
                    flag = -1
                if line.find(Keyword2) != -1:
                    flag = -2
                if line.find(Keyword3) != -1:
                    flag = -3
                if line.find(Keyword4) != -1:
                    flag = -4                   
                if line.find(Keyword5) != -1:
                    flag = -5                    
                if line.find(Keyword6) != -1:
                    flag = -6                    
                if line.find(Keyword7) != -1:
                    flag = -7  
                if line.find(Keyword8) != -1:
                    flag = -8                               
        return flag
    
"""
A collection of Error Messages:

Keyword1: 
Error message occurs only When the feed is in the slot. Also, occurs when the feed and shorting pin overlap each other:
['Project: Implantable WPT, Design: HFSSDesign, [error] Port refinement, process hf3d error: Terminal Feed on port 1 contains a non-conducting edge.  The terminal may need to be assigned manually.. Please contact Ansys technical support. (02:30:49 PM  Nov 01, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation completed with execution error on server: Local Machine. (02:30:51 PM  Nov 01, 2024)\r\n']

Keyword2: 
Error meesage occurs only when the feed is not within the antenna domain:
['Project: Implantable WPT, Design: HFSSDesign, [error] Port refinement, process hf3d error: Too few conductors were found on port 1.  There should be one conductor for each terminal, with one additional reference conductor.  Unintentional contact between conductors may cause this error.. Please contact Ansys technical support. (07:29:28 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation completed with execution error on server: Local Machine. (07:29:30 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Script macro error: Simulation for Implantable WPT : HFSSDesign has failed with execution error.  (07:29:31 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [warning] Report Terminal S Parameter Plot 1 has no data for export. (07:29:32 PM  Nov 05, 2024)\r\n']

Keyword3: 
Error message occurs only when user aborts:
['Project: Implantable WPT, Design: HFSSDesign, [error] Simulation was aborted by user on server: Local Machine. (02:32:40 PM  Nov 01, 2024)\r\n']

Keyword4: 
Error message occurs when HFSS wants to be dumb:
['Project: Implantable WPT, Design: HFSSDesign, [error] Solving frequencies ... (Nondomain solver), process hf3d exited with code 259. (01:48:21 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [info] An interpolating frequency sweep with 401 points has been started using HFSS - Solving Distributed. (01:48:44 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [warning] Interpolating frequency sweep did NOT converge. (01:48:44 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Sweep Sweep failed (01:48:44 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation completed with execution error on server: Local Machine. (01:48:44 PM  Nov 05, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Script macro error: Simulation for Implantable WPT : HFSSDesign has failed with execution error.  (01:48:51 PM  Nov 05, 2024)\r\n']

Keyword5: 
Error message occurs when HFSS wants to be dumb:
The attemped launch of solvers via MPI failed while connecting to communication pipes. The probable cause is failure to install the vendor MPI on one or more machines or password authentication failure for MPI during launch attempt - Simulating on machine: 

Keyword6:
['Project: Implantable WPT, Design: HFSSDesign, [info] An interpolating frequency sweep with 401 points has been started using HFSS - Solving Distributed. (06:21:45 AM  Nov 12, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation has stopped since solver is hanging (06:21:45 AM  Nov 12, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [warning] Interpolating frequency sweep did NOT converge. (06:21:45 AM  Nov 12, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Sweep Sweep failed (06:21:45 AM  Nov 12, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation completed with execution error on server: Local Machine. (06:21:47 AM  Nov 12, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Script macro error: Simulation for Implantable WPT : HFSSDesign has failed with execution error.  (06:22:06 AM  Nov 12, 2024)\r\n']

Keyword7: 
Error Message Discovered during simulation when licensing pool was unable to connect.
['Project: Implantable WPT, Design: HFSSDesign, [error] Request name elec_solve_hfss does not exist in the licensing pool. Cannot connect to license server system.  The license server manager (lmgrd) has not been started yet,  the wrong port@host or license file is being used, or the  port or hostname in the license file has been changed. Feature:       elec_solve_hfss Server name:   130.18.16.117 License path:  27000@LIC-ANSYS.ENGR.MSSTATE.EDU; FlexNet Licensing error:-15,10.  System Error: 10061 "WinSock: Connection refused" (02:36:57 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation was terminated by license error. (02:36:57 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Script macro error: Simulation for Implantable WPT : HFSSDesign has failed with execution error.  (02:36:58 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [warning] Report Terminal S Parameter Plot 1 has no data for export. (02:37:00 PM  Nov 06, 2024)\r\n']

Keyword8: 
Error Message discovered during simulation; failure due to non-responsiveness from abort. 
['Project: Implantable WPT, Design: HFSSDesign, [warning] Com Engine non-responsive since 19:04:21, November 06, 2024.    Can be due to CPU intensive processing or network problems.    If persisting for long, manually kill the com engine process and restart analysis. Retrying.....  (07:05:21 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Simulation was aborted by user on server: Local Machine. (07:06:21 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [warning] Com Engine has responded to the application at 19:06:21, November 06, 2024. (07:06:21 PM  Nov 06, 2024)\r\n', 'Project: Implantable WPT, Design: HFSSDesign, [error] Script macro error: The simulation for Implantable WPT : HFSSDesign has been stopped on user request (07:06:34 PM  Nov 06, 2024)\r\n']

"""