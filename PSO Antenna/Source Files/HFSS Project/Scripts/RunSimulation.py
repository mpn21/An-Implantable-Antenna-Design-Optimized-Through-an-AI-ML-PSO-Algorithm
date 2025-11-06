import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oDesktop.OpenProject("D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Implantable WPT.aedt")

oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")
oDesign.AnalyzeAll()
