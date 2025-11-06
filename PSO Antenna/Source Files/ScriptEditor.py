#############################
#Author: Michael Nguyuen
#Purpose: Class to handle display/save antenna design image (S11 and position displacement) 
#Note: Class modulator is dedicated to change the script 
#############################

class Script:
    def __init__(self, SCRIPT_PATH, SCRIPT_FILE_POSITION, 
                 FEED_X, FEED_Y, SHORTPIN_X, SHORTPIN_Y,
                 SCRIPT_FILE_FIGURE, FIGURE_PATH_OUT, FIGURE_FileName, 
                 SCRIPT_FILE_ErrorHandling, ERRORHANDLING_PATH_OUTPUT, ERRORHANDLING_FileName):
        
        #Class Construct for Script 
        self.Path = SCRIPT_PATH
        self.FileName_Pos = SCRIPT_FILE_POSITION
        self.Feed_x = FEED_X
        self.Feed_y = FEED_Y
        self.ShortPin_x = SHORTPIN_X
        self.ShortPin_y = SHORTPIN_Y
        self.Feed_x_Script =  "feed_x = "
        self.Feed_y_Script = "feed_y = "
        self.ShortPin_x_Script = "shortpin_x = "
        self.ShortPin_y_Script = "shortpin_y = "
        self.MilliMeter = "mm"
        #Class Construct for Images/Figures
        self.ScriptFileName = SCRIPT_FILE_FIGURE
        self.Figure_PathOut = FIGURE_PATH_OUT
        self.Figure_FileName = FIGURE_FileName
        self.Figure_Variable = "Figure = "
        self.Figure_Command = "oEditor.ExportModelImageToFile(Figure, "
        self.pixel_x = 973
        self.pixel_y = 573
        #Class Construct for ErrorHandling
        self.Script_ErrorHandling_FileName = SCRIPT_FILE_ErrorHandling
        self.ErrorHandling_Path_out= ERRORHANDLING_PATH_OUTPUT
        self.ErrorHandling_FileName_Out = ERRORHANDLING_FileName
        self.ErrorHandling_Variable = (r"targetFileName = r")

    ######################
    # Below are functions to handle the update of scripts
    # to generate figures
    ######################

    def ScriptFile(self):
        ScriptFile = self.Path + self.FileName_Pos
        return ScriptFile

    def ReadScriptFile(self):
        ScriptFile = self.ScriptFile()
        with open(ScriptFile, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data

    def UpdateParticlePosition(self):
        Feed_x_Script = self.Feed_x_Script + str(self.Feed_x) + "\n"
        Feed_y_Script = self.Feed_y_Script + "'" + str(self.Feed_y) + self.MilliMeter + "'" + "\n"
        ShortPin_x_Script = self.ShortPin_x_Script + str(self.ShortPin_x) + "\n"
        ShortPin_y_Script = self.ShortPin_y_Script + str(self.ShortPin_y) + "\n"    
        return Feed_x_Script, Feed_y_Script, ShortPin_x_Script, ShortPin_y_Script

    def WriteScriptFile_UpdatePosition(self):
        ScriptFile = self.ScriptFile()
        data = self.ReadScriptFile()
        Feed_x_Script, Feed_y_Script, ShortPin_x_Script, ShortPin_y_Script = self.UpdateParticlePosition()
        
        #lines starts from the 0th element
        #variables for feed (x,y) are located in lines 10-11
        #variables for shortpin (x,y) are located in lines 12-13
        data[10] = Feed_x_Script
        data[11] = Feed_y_Script
        data[12] = ShortPin_x_Script
        data[13] = ShortPin_y_Script

        with open(ScriptFile, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def UpdateScriptPosition(self):
        self.WriteScriptFile_UpdatePosition()

    ######################
    # Below are functions to handle the update of scripts
    # to generate figures
    ######################

    def ScriptFile_Figure(self):
        ScriptFile = self.Path + self.ScriptFileName
        return ScriptFile

    def ReadScriptFile_Figure(self):
        ScriptFile = self.ScriptFile_Figure()
        with open(ScriptFile, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data

    def UpdateParticleFigure(self):
        FigurePathFileName = "'" + self.Figure_PathOut + self.Figure_FileName + "'" + "\n"
        FigureVariable = self.Figure_Variable + FigurePathFileName 
        UpdateCommand = self.Figure_Command + str(self.pixel_x) + ", " + str(self.pixel_y) + "," + "\n"
        return FigureVariable, UpdateCommand

    def WriteScriptFile_UpdateFigure(self):
        ScriptFile = self.ScriptFile_Figure()
        data = self.ReadScriptFile_Figure()
        FigureVariable, UpdateCommand = self.UpdateParticleFigure()
        
        #lines starts from the 0th element
        #variables for feed (x,y) are located in lines 10-11
        #variables for shortpin (x,y) are located in lines 12-13
        data[11] = FigureVariable
        data[13] = UpdateCommand

        with open(ScriptFile, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def UpdateScriptCreateFigure(self):
        self.WriteScriptFile_UpdateFigure()


    ######################
    # Below are functions to update the error handling script
    # to update the targetFileName
    ######################

    def Script_ErrorHandling(self):
        ScriptFile = self.Path + self.Script_ErrorHandling_FileName
        return ScriptFile
    
    def UpdateErrorHandlingFileName(self):
        targetFileName = self.ErrorHandling_Variable + self.ErrorHandling_Path_out + self.ErrorHandling_FileName_Out + "\n"
        return targetFileName

    def ReadScriptFile_ErrorHandling(self):
        ScriptFile = self.Script_ErrorHandling()
        with open(ScriptFile, 'r', encoding='utf-8') as file:
            data = file.readlines()
        return data
    
    def WriteScriptFile_UpdateErrorHandling(self):
        ScriptFile = self.Script_ErrorHandling()
        data = self.ReadScriptFile_ErrorHandling()
        targetFileName = self.UpdateErrorHandlingFileName()
        
        #lines starts from the 0th element
        #variables for targetFileName (Directory+Filename) is located in lines 13
        data[13] = targetFileName

        with open(ScriptFile, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def UpdateScriptErrorHanlding(self):
        self.WriteScriptFile_UpdateErrorHandling()