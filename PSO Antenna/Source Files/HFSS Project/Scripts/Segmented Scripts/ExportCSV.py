import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Terminal S Parameter Plot 1", "D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\S11 Report Files\Terminal S Parameter Plot 1.csv", False)
