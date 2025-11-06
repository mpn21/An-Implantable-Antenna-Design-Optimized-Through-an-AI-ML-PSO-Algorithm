# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2023.2.0
# 16:32:38  Oct 30, 2024
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")

MessageManager = oDesktop.GetMessages("Implantable WPT", "HFSSDesign", 0)
oDesign.EditNotes(str(MessageManager))

targetFileName = r'D:\\ANSYS Working Folder\\PSO\\PSO Antenna\\HFSS_PSO\\Source Files\\HFSS Project\\Message Manager\\MessageManager.txt'
SavetoFile = open(targetFileName, 'w')
SavetoFile.write(str(MessageManager))
SavetoFile.close()

