#############################
#Author: Michael Nguyuen
#Purpose: Class to handle Saving plots and figures 
#Note: Image function call can cause the code to pause. Used other methods besides
#Matplotlib to display and save plots and images.
#############################

import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
import Constants as c

class Figure:
    def __init__(self, IMAGE_PATH, IMAGE_FILENAME, ParticleNum, Iteration, FREQ_MATRIX, S_11_MATRIX, S_11_MIN_VALUE, S_11_MIN_FREQ):
        self.Path = IMAGE_PATH
        self.FileName = IMAGE_FILENAME
        self.Freq = FREQ_MATRIX
        self.S11 = S_11_MATRIX
        self.S11_Min_Value = S_11_MIN_VALUE
        self.S11_Min_Freq = S_11_MIN_FREQ
        self.Min = "Min "
        self.Decibels = " dB, "
        self.Hertz = " GHz"
        self.S11_xaxis_min_range = 1.395
        self.S11_xaxis_max_range = 1.40
        self.ParticleNum = ParticleNum
        self.IterationNum = Iteration
                
    def ImageFile(self, FileName):
        ImageFile = self.Path + FileName
        return ImageFile

    def SavePlot_S11(self):
        S_11_Min_Value_Label = (self.Min + str(round(self.S11_Min_Value,2)) + self.Decibels)
        S_11_Min_Value_Label = (str(round(self.S11_Min_Value,2)) + self.Decibels + str(round(self.S11_Min_Freq,2)) + self.Hertz)
        fig = plt.figure()
        fig.set_tight_layout(True)
        plt.plot(self.Freq, self.S11, 'r')
        plt.plot(self.S11_Min_Freq, self.S11_Min_Value, marker='o', ms=5)
        title = "[P:" + str(self.ParticleNum) + ", " + "Iter: " + str(self.IterationNum) + "] - " + "HFSS Return Loss, S11"
        plt.title(title)
        plt.xlabel("Frequency, GHz")
        plt.xlim([self.S11_xaxis_min_range, self.S11_xaxis_max_range])
        plt.ylabel("Return Loss, dB")
        plt.legend(["S11", S_11_Min_Value_Label], loc = "upper right")
        plt.grid(linestyle='--', linewidth=1)
        # plt.show()
        SaveFile = self.ImageFile(self.FileName)
        fig.savefig(SaveFile)
        plt.close()

    def SaveDesignFigure(self, Feedx, Feedy, ShortPinx, ShortPiny):
        ParticleFigure = self.Path + c.IMAGE_FILE_PARTICLEFIGURE
        DesignFigure = self.Path + c.IMAGE_FILE_DESIGNFIGURE
        ParticleFigure = Image.open(ParticleFigure)
        fig = plt.figure()
        plt.imshow(ParticleFigure)
        plt.axis('off')
        fig.set_tight_layout(True)
        Feedx = round(Feedx, 4)
        Feedy = round(Feedy, 4)
        ShortPinx = round(ShortPinx, 4)
        ShortPiny = round(ShortPiny, 4)
        plt.title("Position: Feed (" + str(Feedx) + ", " + str(Feedy) + ")" + "  " + " ShortPin (" + str(ShortPinx) + ", " + str(ShortPiny) + ")" )
        plt.savefig(DesignFigure)
        plt.close()

    def SaveShowObjectiveFunction(self):
        #Open and resize DesignFigure using cv2
        DesignFigure = self.ImageFile(c.IMAGE_FILE_DESIGNFIGURE)
        DesignFigure = cv2.imread(DesignFigure)
        DesignFigure = cv2.resize(DesignFigure, (800, 600))
        #Open and resize S11PlotFigure using cv2
        S11PlotFigure = self.ImageFile(c.IMAGE_FILE_S11_PLOT)
        S11PlotFigure = cv2.imread(S11PlotFigure)
        S11PlotFigure = cv2.resize(S11PlotFigure, (800, 600))
        #Combine the two figures using cv2
        Row1Stack = np.hstack([DesignFigure, S11PlotFigure])
        FileName = r"\P_" + str(self.ParticleNum) +"_Iter_" + str(self.IterationNum) + "_" + c.IMAGE_FILE_OBJECTIVEFUNCTIONFIGURE 
        ObjFuncFigure =  c.IMAGE_PATH_OUTPUT_RUNLOG + FileName
        cv2.imwrite(ObjFuncFigure, Row1Stack)
        #Show the Image
        image = Image.open(ObjFuncFigure)
        image.show()
        plt.close()

    def SaveShowIterationSwarm(self, iternationnumber, pbest_objective, particles, position1_min, position1_max, position2_min, position2_max):
        fig, (ax1, ax2) = plt.subplots(2,1, figsize=(20,20), subplot_kw={"projection": "3d"})      
        fig.set_tight_layout(True)
        ax1.set_title("Feed, iteration: " + str(iternationnumber), fontsize = 24)
        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        ax1.set_zlabel("Objective Function")
        ax1.set_proj_type('ortho')  # FOV = 0 deg
        ax2.set_title("Short Pin, iteration: " + str(iternationnumber), fontsize = 24)
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')
        ax2.set_zlabel("Objective Function")
        ax2.set_proj_type('ortho')  # FOV = 0 deg
        # Set each axis limits
        ax1.set_xlim(position1_min, position1_max)
        ax1.set_ylim(position2_min, position2_max) 
        ax2.set_xlim(position1_min, position1_max)
        ax2.set_ylim(position2_min, position2_max)
        # Assign 4 DOF positional values
        particles_np = np.array(particles) 
        pbest_objective_np = np.array(pbest_objective)  
        Feed_x = particles_np[:,0]
        Feed_y = particles_np[:,1]
        ShortPin_x = particles_np[:,2]
        ShortPin_y = particles_np[:,3]
        len = np.size(pbest_objective_np)
        objectivefunction = np.reshape(pbest_objective_np, (len,1))
        objectivefunction = objectivefunction[:,0]
        # Scatter Plot the varables 
        ax1.scatter3D(Feed_x, Feed_y, objectivefunction, color="red")
        ax2.scatter3D(ShortPin_x, ShortPin_y, objectivefunction, color="blue") 
        SaveFile = self.Path + r"\Iter_" + str(iternationnumber) + self.FileName 
        #plt.show() #remove the comment to view the plot in 3D (adjusting Azimuth and Elevation for the plot)
        fig.savefig(SaveFile)
        image = Image.open(SaveFile)
        image.show()
        ax1.cla()
        ax2.cla()
        plt.close()       