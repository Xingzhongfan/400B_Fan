import numpy as np
import astropy.units as u

# Function aim to read the .txt file

def Read(filename):
    # Inputs:
    #    filename is file's name eg: 'MW_000.txt'
    # Returns:
    #    time is the units of Myr (equivalent to SnapNumber*10/0.7)
    #    TotalNumber is total number of particlers
    #    data is a list include the file infomation
    
    
    # open the file
    file = open(filename,'r') 
    # read the first line
    line1 = file.readline()
    # split the time lable and time value
    lable1, value1 = line1.split()
    # add time units to Myr
    time = float(value1)*u.Myr
    # read the second line
    line2 = file.readline()
    # split the total particle lable and number of total particler
    lable2, value2 = line2.split()
    TotalNumber = value2
    # read the data, line split with white space, skipping first 3 lines,
    # store data with right labels
    data = np.genfromtxt(filename, dtype = None, names = True, skip_header=3)
    return time,TotalNumber,data