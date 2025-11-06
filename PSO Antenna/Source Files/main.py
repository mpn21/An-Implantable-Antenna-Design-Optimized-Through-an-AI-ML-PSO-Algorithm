#############################
#Author: Michael Nguyuen
#Purpose: File used to store Directory, Constants and Filenames 
#Note: Main Python Execution file Below is the CMD line to run the PSO externally

#Default Method:
#Windows CMD Code to open HFSS and run Script
#Open CMD, Paste and execute cmd line: 

#"C:\Program Files\AnsysEM\Ansys Student\v222\Win64\ansysedtsv.exe" -RunScript "D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Scripts\Multi_Script.py"

#"C:\Program Files\AnsysEM\v232\Win64\ansysedt.exe" -RunScript "D:\ANSYS Working Folder\PSO\PSO Antenna\HFSS_PSO\Source Files\HFSS Project\Scripts\Multi_Script.py"

#############################

#Library Packages
    #Windows OS Python Classes
import os
import numpy as np
    #Random Number Generator
import random
    #Custom Classes
import CSVIntegrator as csv
import ScriptEditor as Edit
import SimIntegrator_HFSS as HFSS
import Constants as c
import Figure as EditFig
import ErrorHandling as Err

def fitness_function(x1,x2, x3, x4, ParticleNum, iterationnumber):
    
    Feedx = x1
    Feedy = x2
    ShortPinx = x3
    ShortPiny = x4
        
    # Update Scripts for Feed/ShortPin Position, Exporting Design into Paint, Update Script for ErrorHandling
    Particle = Edit.Script(c.SEG_SCRIPT_PATH_ROOT, c.SCRIPT_FILE_DynamicVariables, Feedx, Feedy, ShortPinx, ShortPiny, 
                        c.SCRIPT_FILE_ExportDesignFigure, c.IMAGE_PATH_OUTPUT, c.IMAGE_FILE_PARTICLEFIGURE, 
                        c.SCRIPT_FILE_ErrorHandling, c.ErrorHandling_Script_Path_OUTPUT, c.ErrorHandling_Script_Path_OUTPUT_FileName) 
    
    Particle.UpdateScriptPosition()
    Particle.UpdateScriptCreateFigure()
    Particle.UpdateScriptErrorHanlding()   

    #Run HFSS Simulation
    Particle_Obj_Function = HFSS.SimIntegrator_HFSS(c.ANSYS_PATH, license=1)
    Particle_Obj_Function.HFSSrunWithScript(c.PYTHON_SCRIPT_PATH_Multi_Script)

    #Check for Errors
    Error = Err.MessageManager(c.ErrorHandling_Path, c.ErrorHandling_FileName)
    Error_Flag = Error.Find_Error()
  
    #Auto Error Handling     
    while(Error_Flag <= -1):
        #No Solution Error - Feed in slot
        if Error_Flag == -1:
                ErrorHandlingCSV = csv.CSVIntegerator(c.CSV_Path, c.CSV_ErrorFileName)
                ErrorCSV_Freq, ErrorCSV_S11, ErrorCSV_S11_Min_Value, ErrorCSV_S11_Min_Freq = ErrorHandlingCSV.S_11_Min_NoSolution()
                z = int(ErrorCSV_S11_Min_Value)
                ErrorParticle_Plot = EditFig.Figure(c.IMAGE_PATH_OUTPUT, c.IMAGE_FILE_S11_PLOT, ParticleNum, iterationnumber,
                                            ErrorCSV_Freq, ErrorCSV_S11, ErrorCSV_S11_Min_Value, ErrorCSV_S11_Min_Freq)
                ErrorParticle_Plot.SavePlot_S11() #Part and iter shows on title
                ErrorParticle_Plot.SaveDesignFigure(Feedx, Feedy, ShortPinx, ShortPiny) 
                ErrorParticle_Plot.SaveShowObjectiveFunction()
                break
        #No Solution Error - Feed outside of antenna search domain
        if Error_Flag == -2:
                ErrorHandlingCSV = csv.CSVIntegerator(c.CSV_Path, c.CSV_ErrorFileName)
                ErrorCSV_Freq, ErrorCSV_S11, ErrorCSV_S11_Min_Value, ErrorCSV_S11_Min_Freq = ErrorHandlingCSV.S_11_Min_NoSolution()
                z = int(ErrorCSV_S11_Min_Value)
                ErrorParticle_Plot = EditFig.Figure(c.IMAGE_PATH_OUTPUT, c.IMAGE_FILE_S11_PLOT, ParticleNum, iterationnumber,
                                            ErrorCSV_Freq, ErrorCSV_S11, ErrorCSV_S11_Min_Value, ErrorCSV_S11_Min_Freq)
                ErrorParticle_Plot.SavePlot_S11() #Part and iter shows on title
                ErrorParticle_Plot.SaveDesignFigure(Feedx, Feedy, ShortPinx, ShortPiny) 
                ErrorParticle_Plot.SaveShowObjectiveFunction()
                break
        #Abort by user
        if Error_Flag == -3:
            print('Abort Error Occurred: Manually open HFSS Project file to unlock the file, save then close ANSYS/HFSS')
            print('System is paused:')
            os.system('PAUSE')
        #hf3d Error
        if Error_Flag == -4:
            print('hf3d error, Restarting Simulation')
        #MPI Error
        if Error_Flag == -5:
            print('MPI Error, Restarting Simulation')
        #Converge Error
        if Error_Flag == -6:
            print('Simulation Hanging, did NOT converge error, Restarting Simulation')    
        #Licensing Pool Error
        if Error_Flag == -7:
            print('No connection to licensing pool error: Manually open HFSS Project file to verify connection with licensing pool, save then close ANSYS/HFSS')
            print('System is paused:')
            os.system('PAUSE')
        #NonResponsive Error, this error was discovered when user selects abort and HFSS will not respond resulting in a alt+tab+del kill tasks
        if Error_Flag == -8:
            print('Non Resposnive error, Restarting Simulation')
        
        #Rerun Simulation and check for error
        Particle_Obj_Function = HFSS.SimIntegrator_HFSS(c.ANSYS_PATH, license=1)
        Particle_Obj_Function.HFSSrunWithScript(c.PYTHON_SCRIPT_PATH_Multi_Script)      
        #Check for Errors
        Error = Err.MessageManager(c.ErrorHandling_Path, c.ErrorHandling_FileName)
        Error_Flag = Error.Find_Error()

    #Plot DesignFigure and S11_Figure then continue
    if Error_Flag == False:
        #Obtain Objective Function Value
        Objective_Function = csv.CSVIntegerator(c.CSV_Path, c.CSV_FileName)
        Freq, S_11, S_11_Min_Value, S11_Min_Freq = Objective_Function.S_11_Min()
        #z = f(x1,y1, x2,y2)
        z = S_11_Min_Value
        
        Particle_Plot = EditFig.Figure(c.IMAGE_PATH_OUTPUT, c.IMAGE_FILE_S11_PLOT, ParticleNum, iterationnumber,
                                    Freq, S_11, S_11_Min_Value, S11_Min_Freq)
        Particle_Plot.SavePlot_S11() #Part and iter shows on title
        Particle_Plot.SaveDesignFigure(Feedx, Feedy, ShortPinx, ShortPiny) 
        Particle_Plot.SaveShowObjectiveFunction()
    
    #optimizing for global maxima
    z = (z)*-1
    
    return z

def update_velocity(particle, velocity, pbest, gbest, w_min=0.5, max=1.0, c=0.1):
    # Initialise new velocity array
    num_particle = len(particle)
    new_velocity = np.array([0.0 for i in range(num_particle)])
    # Randomly generate r1, r2 and inertia weight from normal distribution
    r1 = random.uniform(0,max)
    r2 = random.uniform(0,max)
    w = random.uniform(w_min,max)
    c1 = c
    c2 = c
    # Calculate new velocity
    for i in range(num_particle):
        new_velocity[i] = w*velocity[i] + c1*r1*(pbest[i]-particle[i])+c2*r2*(gbest[i]-particle[i])
        #new_velocity[i] = w*velocity[i] + i*c1*r1*(pbest[i]-particle[i])+ i*c2*r2*(gbest[i]-particle[i])
    return new_velocity

def update_position(particle, velocity):
    # Move particles by adding velocity
    new_particle = particle + velocity
    return new_particle

def pso_4d(population, dimension, position1_min, position1_max, position2_min, position2_max, DECIMAL_PRECISION, iteration, fitness_criterion):
# Initialisation
    
    # Population
    particles = []
    for i in range (0, population):
        Feedx = round(random.uniform(position1_min, position1_max), DECIMAL_PRECISION) #Range is between -5 to 5, steps 0.1
        Feedy = round(random.uniform(position2_min, position2_max), DECIMAL_PRECISION) #Range is between -8 to 8, steps 0.1
        ShortPinx = round(random.uniform(position1_min, position1_max), DECIMAL_PRECISION) #Range is between -5 to 5, steps 0.1
        ShortPiny = round(random.uniform(position2_min, position2_max), DECIMAL_PRECISION) #Range is between -8 to 8, steps 0.1
        particles.append([Feedx, Feedy, ShortPinx, ShortPiny])
        
    # Particle's best position
    pbest_position = particles
    
    # Fitness
    iterationnumber=0
    pbest_objective = []
    for i in range(0, population): 
        particle_row = [particles[i]] #store row
        pbest_objective_list = fitness_function(particle_row[0][0], particle_row[0][1], particle_row[0][2], particle_row[0][3], i, iterationnumber)
        pbest_objective.append([pbest_objective_list])
    #Save initial iternation/population objective data and positions to CSV File 
    CSV_ObjFunction = csv.CSVIntegerator(c.CSV_Path_RunLog, c.CSV_FILENAME_OBJECT_FUNCTION)
    CSV_ObjFunction.SavetoCSV(iterationnumber, pbest_objective, particles)

    # Index of the best particle
    gbest_index = np.argmax(pbest_objective)
    
    # Global best particle position
    gbest_position = pbest_position[gbest_index]
    
    # Velocity (starting from 0 speed)
    velocity = [[0.0 for j in range(dimension)] for i in range(population)]

    #Plot Iteration Swarm
    Iteration_Plot = EditFig.Figure(c.IMAGE_PATH_OUTPUT_RUNLOG, c.IMAGE_FILENAME_ITERATION, 0, 0, 0, 0, 0, 0)
    Iteration_Plot.SaveShowIterationSwarm(iterationnumber, pbest_objective, particles, position1_min, position1_max, position2_min, position2_max)

    # Loop for the number of iteration
    for t in range(iteration):
        # Stop if the average fitness value reached a predefined success criterion
        if np.average(pbest_objective) >= fitness_criterion:
            print("fitness critera reached")
            break
        else:
            for n in range(population):
                # Update the velocity of each particle
                velocity[n] = update_velocity(particles[n], velocity[n], pbest_position[n], gbest_position)
                # Move the particles to new position
                particles[n] = update_position(particles[n], velocity[n])

        # Calculate the fitness value
        iterationnumber=t+1
        pbest_objective = []
        for i in range(0, population): 
            particle_row = [particles[i]] #store row
            pbest_objective_list = fitness_function(particle_row[0][0], particle_row[0][1], particle_row[0][2], particle_row[0][3], i, iterationnumber)
            pbest_objective.append([pbest_objective_list])
    
        #Save initial iternation/population objective data and positions to CSV File 
        CSV_ObjFunction.SavetoCSV(iterationnumber, pbest_objective, particles)
        
        # Find the index of the best particle
        gbest_index = np.argmax(pbest_objective)
        
        # Update the position of the best particle
        gbest_position = pbest_position[gbest_index]

        #Plot Iteration Swarm
        Iteration_Plot.SaveShowIterationSwarm(iterationnumber, pbest_objective, particles, position1_min, position1_max, position2_min, position2_max)

    #end for loop

    # Print the results
    print('Global Best Position: ', gbest_position)
    print('Best Fitness Value: ', max(pbest_objective))
    print('Average Particle Best Fitness Value: ', np.average(pbest_objective))
    print('Number of iteration: ', t+1)

population = 25
dimension = 4
position1_min = -5.0
position1_max = 5.0
position2_min = -8.0
position2_max = 8.0
DECIMAL_PRECISION = 1
iteration = 30
fitness_criterion = 30

####                                                                                        ####
##                                                                                            ##
#            !!!MAKE SURE TO LOG INTO MSU VPN TO RUN HFSS FULL LICENSE SOFTWARE!!!             #
##                                                                                            ##      
####                                                                                        ####    

pso_4d(population, dimension, position1_min, position1_max, position2_min, position2_max, DECIMAL_PRECISION, iteration, fitness_criterion)

os.system("PAUSE")