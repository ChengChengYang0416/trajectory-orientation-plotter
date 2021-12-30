import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
from scipy.spatial.transform import Rotation as R

# read parameters from XML
tree = ET.parse( 'Parameters.xml' )
root = tree.getroot()
for child in root:
    if child.tag == 'Filename':
        Filename = child.text
    
    if child.tag == 'UnitConvert':
        UnitConvert = int( child.text )

    if child.tag == 'SamplingInterval':
        SamplingInterval = int( child.text )

    if child.tag == 'XAxisLower':
        XAxisLower = int( child.text )

    if child.tag == 'XAxisUpper':
        XAxisUpper = int( child.text )

    if child.tag == 'YAxisLower':
        YAxisLower = int( child.text )

    if child.tag == 'YAxisUpper':
        YAxisUpper = int( child.text )

    if child.tag == 'ZAxisLower':
        ZAxisLower = int( child.text )

    if child.tag == 'ZAxisUpper':
        ZAxisUpper = int( child.text )

# load the data from txt file
Pose = np.loadtxt( Filename, delimiter =' ', usecols = ( 0, 1, 2, 3, 4, 5 ), unpack = True )

# convert the unit from BLU to mm
Pose /= UnitConvert

# list for trajectory and orientation
X = []
Y = []
Z = []
OrientationXX = []
OrientationXY = []
OrientationXZ = []
OrientationYX = []
OrientationYY = []
OrientationYZ = []
OrientationZX = []
OrientationZY = []
OrientationZZ = []

# get orientation by rotation matrix
for i in range( 0, len( Pose[ 0 ] ), SamplingInterval ):
    r = R.from_euler( 'zyx', [ Pose[ 3 ][ i ], Pose[ 4 ][ i ], Pose[ 5 ][ i ] ], degrees = True )
    OrientationXX.append( r.as_matrix()[ 0 ][ 0 ] )
    OrientationXY.append( r.as_matrix()[ 1 ][ 0 ] )
    OrientationXZ.append( r.as_matrix()[ 2 ][ 0 ] )
    OrientationYX.append( r.as_matrix()[ 0 ][ 1 ] )
    OrientationYY.append( r.as_matrix()[ 1 ][ 1 ] )
    OrientationYZ.append( r.as_matrix()[ 2 ][ 1 ] )
    OrientationZX.append( r.as_matrix()[ 0 ][ 2 ] )
    OrientationZY.append( r.as_matrix()[ 1 ][ 2 ] )
    OrientationZZ.append( r.as_matrix()[ 2 ][ 2 ] )
    X.append( Pose[ 0 ][ i ] )
    Y.append( Pose[ 1 ][ i ] )
    Z.append( Pose[ 2 ][ i ] )

# create figure
fig = plt.figure()
ax = plt.axes( projection = '3d' )

# label of axis
plt.xlabel( 'X' )
plt.ylabel( 'Y' )

# set the boundary
xlim = [ XAxisLower, XAxisUpper ]
ylim = [ YAxisLower, YAxisUpper ]
zlim = [ ZAxisLower, ZAxisUpper ]
ax.set_xlim3d( xlim )
ax.set_ylim3d( ylim )
ax.set_zlim3d( zlim )

# set the aspect ration of x, y, z to 1:1:1
ax.set_box_aspect( [ 1, 1, 1 ] )

# plot the orientation
ax.quiver( X, Y, Z, OrientationXX, OrientationXY, OrientationXZ, length = 10, normalize = True, color = 'r' )
ax.quiver( X, Y, Z, OrientationYX, OrientationYY, OrientationYZ, length = 10, normalize = True, color = 'g' )
ax.quiver( X, Y, Z, OrientationZX, OrientationZY, OrientationZZ, length = 10, normalize = True, color = 'b' )

# plot
plt.show()
