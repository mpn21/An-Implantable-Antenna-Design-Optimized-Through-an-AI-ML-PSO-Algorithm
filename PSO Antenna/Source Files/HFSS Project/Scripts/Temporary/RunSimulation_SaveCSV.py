# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2022.2.0
# 18:23:03  Apr 30, 2023
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Implantable WPT")
oProject.Save()
oDesign = oProject.SetActiveDesign("HFSSDesign")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Terminal S Parameter Plot 1", "C:/Users/mpn21/Documents/HFSS_PSO/Source Files/Output/S11 Report Files/Terminal S Parameter Plot 1.csv", False)
