# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Student Version 2022.2.0
# 14:34:16  May 02, 2023
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Implantable WPT")
oDesign = oProject.SetActiveDesign("HFSSDesign")
oEditor = oDesign.SetActiveEditor("3D Modeler")

Figure = 'D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\Output\Figures\ParticleFigure.png'

oEditor.ExportModelImageToFile(Figure, 973, 573,
	[
		"NAME:SaveImageParams",
		"ShowAxis:="		, "False",
		"ShowGrid:="		, "False",
		"ShowRuler:="		, "True",
		"ShowRegion:="		, "Default",
		"Selections:="		, "",
		"FieldPlotSelections:="	, "",
		"FitToSelections:="	, "",
		"FitToFieldPlotSelections:=", "",
		"Orientation:="		, ""
	])
