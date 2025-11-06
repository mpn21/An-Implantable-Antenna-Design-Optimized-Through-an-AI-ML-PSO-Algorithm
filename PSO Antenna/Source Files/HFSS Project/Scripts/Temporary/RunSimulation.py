# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2022.2.0
# 17:57:27  Apr 30, 2023
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")
oDesign.AnalyzeAll()
