#############################
#Author: Michael Nguyuen
#Purpose: Class to handle CSV files
#Note: This class is to save the data points for every iteration
#############################

import pandas as pd
import numpy as np
import Constants as c

class CSVIntegerator:
    def __init__(self, CSV_Path, CSV_File):
        self.Path = CSV_Path
        self.FileName = CSV_File

    def CSVFile(self):
        CSV_File = self.Path + self.FileName
        return CSV_File
    
    def CSVRead(self):
        FileName = self.CSVFile()
        data = pd.read_csv(FileName)
        Freq = data.iloc[:,0]
        S_11 = data.iloc[:,1]
        return Freq, S_11

    def S_11_Min(self):
        Freq, S_11 = self.CSVRead()
        S_11_Min_Value = np.min(S_11)
        S_11_Min_Idx = np.argmin(S_11)
        S_11_Min_Freq = Freq[S_11_Min_Idx]
        return Freq, S_11, S_11_Min_Value, S_11_Min_Freq 
    
    def S_11_Min_NoSolution(self):
        Freq, S_11 = self.CSVRead()
        S_11_Min_Value = np.min(S_11)
        S_11_Min_Idx = np.argmin(S_11)
        S_11_Min_Freq = Freq[S_11_Min_Idx]
        return Freq, S_11, S_11_Min_Value, S_11_Min_Freq 

    def SavetoCSV(self, iterationnumber, pbest_objective, particles):
        IterNum = iterationnumber
        pBest_Obj  = np.array(pbest_objective)
        Particles = np.array(particles)
        row, col = np.shape(Particles)
        Data = np.zeros([(row), col+1])

        Data[:,0] = pBest_Obj[:,0]

        for i in range (0, col):
            Data[:,[i+1]] = Particles[:,[i]]

        Filename = self.Path + "\iter_" + str(IterNum) + "_" + self.FileName
        np.savetxt(Filename, Data, delimiter=',') 
