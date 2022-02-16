import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from Modules import PlotterParametersLoader
from Modules import PoseDataLoader
from Modules import DataProcessor

def ButtonOpenClick( EntryOpenFile ):
    Filename = filedialog.askopenfile( title = "Select a file", filetypes = ( ( "txt file", "*.txt" ), ( "all file", "*.*" ) ) )
    EntryOpenFile.delete( 0, 'end' )
    EntryOpenFile.insert( 0, Filename.name )

def ButtonLoadParamClick( EntryLoadParam, EntryXAxisLower, EntryXAxisUpper, EntryYAxisLower, EntryYAxisUpper, EntryZAxisLower, EntryZAxisUpper, EntryConvertUnit, EntrySampleInterval ):
	# read parameter xml file path
	Filename = filedialog.askopenfile( title = "Select a file", filetypes = ( ( "xml file", "*.xml" ), ( "all file", "*.*" ) ) )
	EntryLoadParam.delete( 0, 'end' )
	EntryLoadParam.insert( 0, Filename.name )

	# read parameters from XML
	ParametersFilePath = 'Data\\Parameters.xml'
	Parameters = PlotterParametersLoader.GetPlotterParameters( ParametersFilePath )

	# fill entry with xml parameters
	EntryXAxisLower.delete( 0, 'end' )
	EntryXAxisLower.insert( 0, Parameters[ 'XAxisLower' ] )
	EntryXAxisUpper.delete( 0, 'end' )
	EntryXAxisUpper.insert( 0, Parameters[ 'XAxisUpper' ] )
	EntryYAxisLower.delete( 0, 'end' )
	EntryYAxisLower.insert( 0, Parameters[ 'YAxisLower' ] )
	EntryYAxisUpper.delete( 0, 'end' )
	EntryYAxisUpper.insert( 0, Parameters[ 'YAxisUpper' ] )
	EntryZAxisLower.delete( 0, 'end' )
	EntryZAxisLower.insert( 0, Parameters[ 'ZAxisLower' ] )
	EntryZAxisUpper.delete( 0, 'end' )
	EntryZAxisUpper.insert( 0, Parameters[ 'ZAxisUpper' ] )
	EntryConvertUnit.delete( 0, 'end' )
	EntryConvertUnit.insert( 0, Parameters[ 'UnitConvert' ] )
	EntrySampleInterval.delete( 0, 'end' )
	EntrySampleInterval.insert( 0, Parameters[ 'SamplingInterval' ] )

def ButtonPlot( FilePath ):
    # read parameters from XML
    ParametersFilePath = 'Data\\Parameters.xml'
    Parameters = PlotterParametersLoader.GetPlotterParameters( ParametersFilePath )

    # load the data from txt file
    Pose = PoseDataLoader.GetPoseData( FilePath )

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
