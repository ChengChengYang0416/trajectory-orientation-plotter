import matplotlib.pyplot as plt
from Modules import PlotterParametersLoader
from Modules import PoseDataLoader
from Modules import DataProcessor

# read parameters from XML
Parameters = PlotterParametersLoader.GetPlotterParameters()

# load the data from txt file
Pose = PoseDataLoader.GetPoseData( Parameters[ 'Filename' ] )

# convert the unit from BLU to mm
Pose /= Parameters[ 'UnitConvert' ]

# get sampled position and orientation
SampledPose = DataProcessor.GetSampledPositionAndOrientation( Pose, Parameters[ 'SamplingInterval' ] )

# create figure
fig = plt.figure()
ax = plt.axes( projection = '3d' )

# label of axis
plt.xlabel( 'X' )
plt.ylabel( 'Y' )

# set the boundary
xlim = [ Parameters[ 'XAxisLower' ], Parameters[ 'XAxisUpper' ] ]
ylim = [ Parameters[ 'YAxisLower' ], Parameters[ 'YAxisUpper' ] ]
zlim = [ Parameters[ 'ZAxisLower' ], Parameters[ 'ZAxisUpper' ] ]
ax.set_xlim3d( xlim )
ax.set_ylim3d( ylim )
ax.set_zlim3d( zlim )

# set the aspect ration of x, y, z to 1:1:1
ax.set_box_aspect( [ 1, 1, 1 ] )

# plot the orientation
ax.quiver( SampledPose[ 'X' ], SampledPose[ 'Y' ], SampledPose[ 'Z' ], SampledPose[ 'OrientationXX' ], SampledPose[ 'OrientationXY' ], SampledPose[ 'OrientationXZ' ], length = 10, normalize = True, color = 'r' )
ax.quiver( SampledPose[ 'X' ], SampledPose[ 'Y' ], SampledPose[ 'Z' ], SampledPose[ 'OrientationYX' ], SampledPose[ 'OrientationYY' ], SampledPose[ 'OrientationYZ' ], length = 10, normalize = True, color = 'g' )
ax.quiver( SampledPose[ 'X' ], SampledPose[ 'Y' ], SampledPose[ 'Z' ], SampledPose[ 'OrientationZX' ], SampledPose[ 'OrientationZY' ], SampledPose[ 'OrientationZZ' ], length = 10, normalize = True, color = 'b' )

# plot
plt.show()
