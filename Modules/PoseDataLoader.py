import numpy as np

def GetPoseData( Filename ):
    # load the data from txt file
    Pose = np.loadtxt( Filename, delimiter =' ', usecols = ( 0, 1, 2, 3, 4, 5 ), unpack = True )

    return Pose
