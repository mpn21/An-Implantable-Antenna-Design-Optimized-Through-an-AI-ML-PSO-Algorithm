#############################
#Author: Michael Nguyuen
#Purpose: File used to store Directory, Constants and Filenames 
#Note: The directory below can be changed to match another person's file structure 
# The program is in its early stages; therefore, file structure handler will be implemented
# in later revisions.
#############################

#HFSS Directory
#ANSYS_PATH = (r"C:\Program Files\AnsysEM\Ansys Student\v222\Win64\ansysedtsv.exe") #Student Version
#ANSYS_PATH = (r"C:\Program Files\AnsysEM\v232\Win64\ansysedt.exe") 
ANSYS_PATH = (r"C:\Program Files\AnsysEM\v241\Win64\ansysedt.exe") 

#HFSS Script Directory
SCRIPT_PATH_ROOT = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Scripts")
PYTHON_SCRIPT_PATH_Multi_Script = SCRIPT_PATH_ROOT + "\Multi_Script.py"
PYTHON_SCRIPT_PATH_Open_File = SCRIPT_PATH_ROOT + "\OpenFile.py"
PYTHON_SCRIPT_PATH_Run_Simulation = SCRIPT_PATH_ROOT + "\RunSimulation.py"
PYTHON_SCRIPT_PATH_Run_Simu_SaveCSV = SCRIPT_PATH_ROOT + "\RunSimulation_SaveCSV.py"

SEG_SCRIPT_PATH_ROOT = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Scripts\Segmented Scripts")
SCRIPT_FILE_DynamicVariables = "\DynamicVariables.py"
SCRIPT_FILE_ExportDesignFigure = "\ExportDesignFigure.py"
SCRIPT_FILE_ErrorHandling = "\ErrorHandling.py"

#CSV Directory
CSV_Path = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\S11 Report Files")
CSV_FileName = "\Terminal S Parameter Plot 1.csv"
CSV_ErrorFileName = "\Terminal S Parameter No Solution.csv"

CSV_Path_RunLog = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\CSV\RunLog")
CSV_FILENAME_OBJECT_FUNCTION = (r"ObjectiveFunction.csv")

#Plot Directory
IMAGE_PATH_MISC = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Misc Source")
IMAGE_FILE_NO_SOLUTION = (r"\No Solution.png")

IMAGE_PATH_OUTPUT = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\Figures")
IMAGE_FILE_PARTICLEFIGURE = (r"\ParticleFigure.png")
IMAGE_FILE_S11_PLOT = (r"\S11Plot.png")
IMAGE_FILE_DESIGNFIGURE = (r"\DesignFigure.png")

IMAGE_PATH_OUTPUT_RUNLOG = (r"D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\Figures") 
IMAGE_FILE_OBJECTIVEFUNCTIONFIGURE = (r"ObjFunct.png")
IMAGE_FILENAME_ITERATION = (r"PopulationSwarm.png")

#Error Handling Path
    #IronPython unique format (double "\\")
ErrorHandling_Script_Path_OUTPUT = (r"'D:\\ANSYS Working Folder\\PSO\\PSO Antenna\\HFSS_PSO\\Source Files\\HFSS Project\\Message Manager\\")
ErrorHandling_Script_Path_OUTPUT_FileName = (r"MessageManager.txt'")

ErrorHandling_Path = (r'D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Message Manager')
ErrorHandling_FileName = (r'\MessageManager.txt')