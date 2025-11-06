import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")
oDesign.AnalyzeAll()