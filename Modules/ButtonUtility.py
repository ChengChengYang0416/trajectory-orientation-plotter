from tkinter import filedialog
import matplotlib.pyplot as plt
from Modules.PlotterParametersLoader import CPlotterParametersLoader
from Modules.PoseDataLoader import CPoseDataLoader
from Modules.DataProcessor import CDataProcessor
from Modules.TrajPlotter import CTrajPlotter

class CButtonUtility:
	def ButtonOpenClick( self, EntryOpenFile ):
		Filename = filedialog.askopenfile( title = "Select a file", filetypes = ( ( "txt file", "*.txt" ), ( "all file", "*.*" ) ) )
		if Filename is None:
			return

		EntryOpenFile.delete( 0, 'end' )
		EntryOpenFile.insert( 0, Filename.name )

	def ButtonLoadParamClick( self, EntryLoadParam, EntryXAxisLower, EntryXAxisUpper, EntryYAxisLower, EntryYAxisUpper, EntryZAxisLower, EntryZAxisUpper, EntryConvertUnit, EntrySampleInterval ):
		# read parameter xml file path
		Filename = filedialog.askopenfile( title = "Select a file", filetypes = ( ( "xml file", "*.xml" ), ( "all file", "*.*" ) ) )
		if Filename is None:
			return

		EntryLoadParam.delete( 0, 'end' )
		EntryLoadParam.insert( 0, Filename.name )

		# read parameters from XML
		ParametersFilePath = Filename.name
		PlotterParametersLoader = CPlotterParametersLoader()
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

	def ButtonPlot( self, FilePath, XAxisLower, XAxisUpper, YAxisLower, YAxisUpper, ZAxisLower, ZAxisUpper, ConvertUnit, SampleInterval ):
		# load the data from txt file
		PoseDataLoader = CPoseDataLoader()
		Pose = PoseDataLoader.GetPoseData( FilePath )

		# convert the unit from BLU to mm
		Pose /= ConvertUnit

		# get sampled position and orientation
		DataProcessor = CDataProcessor()
		SampledPose = DataProcessor.GetSampledPositionAndOrientation( Pose, SampleInterval )

		# plot trajectory and orientation
		TrajPlotter = CTrajPlotter()
		TrajPlotter.PlotTrajectory( SampledPose, XAxisLower, XAxisUpper, YAxisLower, YAxisUpper, ZAxisLower, ZAxisUpper )

	def Button2DStatesPlot( self, FilePath, ConvertUnit, SampleInterval ):
		# load the data from txt file
		PoseDataLoader = CPoseDataLoader()
		Pose = PoseDataLoader.GetPoseData( FilePath )

		# convert the unit from BLU to mm
		Pose /= ConvertUnit

		# get sampled position and orientation
		DataProcessor = CDataProcessor()
		SampledPose = DataProcessor.GetSampledJointStates( Pose, SampleInterval )

		# plot trajectory and orientation
		TrajPlotter = CTrajPlotter()
		TrajPlotter.Plot2DStates( SampledPose )

	def ButtonXYZABCStatesPlot( self, FilePath, ConvertUnit, SampleInterval ):
		# load the data from txt file
		PoseDataLoader = CPoseDataLoader()
		Pose = PoseDataLoader.GetPoseData( FilePath )

		# convert the unit from BLU to mm
		Pose /= ConvertUnit

		# get sampled position and orientation
		DataProcessor = CDataProcessor()
		SampledPose = DataProcessor.GetSampledXYZABCStates( Pose, SampleInterval )

		# plot trajectory and orientation
		TrajPlotter = CTrajPlotter()
		TrajPlotter.PlotXYZABCStates( SampledPose )

	def ButtonCloseAllFigues( self ):
		plt.close( "all" )
