import tkinter as tk
from Modules.ButtonUtility import CButtonUtility

class CPlotterGui:
	def __init__( self ):
		self.Win = tk.Tk()
		self.InitBasicSetting()
		self.InitFrame()
		self.InitLabel()
		self.InitEntry()
		self.InitButton()

	def InitBasicSetting( self ):
		# set title
		self.Win.title( "Plotter Gui" )

		# set geometry of window ( width x height )
		self.Win.geometry( "855x279" )
		self.Win.resizable( False, False )

		# color, transparency, pin on top
		self.Win.config( background = "#C0C0C0" )
		self.Win.attributes( "-topmost", True )

	def InitFrame( self ):
		# frame for 3D plot
		self.Frame3DPlot = tk.LabelFrame( width = 420, height = 269, text = "3D Plot" )
		self.Frame3DPlot.place( x = 5, y = 5 )

		# frame for 2D states plot
		self.Frame2DStatesPlot = tk.LabelFrame( width = 420, height = 172, text = "2D States Plot" )
		self.Frame2DStatesPlot.place( x = 430, y = 5 )

		# frame for parameters of 3D plot
		self.Frame3DPlotParam = tk.LabelFrame( self.Frame3DPlot, width = 410, height = 150, text = "parameters" )
		self.Frame3DPlotParam.place( x = 3, y = 65 )

		# frame for 2D states plot
		self.Frame2DStatesParam = tk.LabelFrame( self.Frame2DStatesPlot, width = 410, height = 53, text = "parameters" )
		self.Frame2DStatesParam.place( x = 3, y = 65 )

	def InitLabel( self ):
		self.Init3DPlotLabel()
		self.Init2DStatesPlotLabel()

	def InitEntry( self ):
		self.Init3DPlotEntry()
		self.Init2DStatesPlotEntry()

	def InitButton( self ):
		# button object
		self.ButtonUtility = CButtonUtility()

		self.Init3DPlotButton()
		self.Init2DStatesPlotButton()

	def Init3DPlotLabel( self ):
		# X axis lower bound label
		self.LabelXAxisLower = tk.Label( self.Frame3DPlotParam, text = "XAxisLower" )
		self.LabelXAxisLower.place( x = 0, y = 0, width = 95, height = 28 )

		# X axis upper bound label
		self.LabelXAxisUpper = tk.Label( self.Frame3DPlotParam, text = "XAxisUpper" )
		self.LabelXAxisUpper.place( x = 200, y = 0, width = 95, height = 28 )

		# Y axis lower bound label
		self.LabelYAxisLower = tk.Label( self.Frame3DPlotParam, text = "YAxisLower" )
		self.LabelYAxisLower.place( x = 0, y = 32, width = 95, height = 28 )

		# Y axis upper bound label
		self.LabelYAxisUpper = tk.Label( self.Frame3DPlotParam, text = "YAxisUpper" )
		self.LabelYAxisUpper.place( x = 200, y = 32, width = 95, height = 28 )

		# Z axis lower bound label
		self.LabelZAxisLower = tk.Label( self.Frame3DPlotParam, text = "ZAxisLower" )
		self.LabelZAxisLower.place( x = 0, y = 64, width = 95, height = 28 )

		# Z axis upper bound label
		self.LabelZAxisUpper = tk.Label( self.Frame3DPlotParam, text = "ZAxisUpper" )
		self.LabelZAxisUpper.place( x = 200, y = 64, width = 95, height = 28 )

		# convert unit label
		self.LabelConvertUnit = tk.Label( self.Frame3DPlotParam, text = "ConvertUnit" )
		self.LabelConvertUnit.place( x = 0, y = 96, width = 95, height = 28 )

		# sample interval label
		self.LabelSampleInterval = tk.Label( self.Frame3DPlotParam, text = "SampleInterval" )
		self.LabelSampleInterval.place( x = 200, y = 96, width = 95, height = 28 )

	def Init2DStatesPlotLabel( self ):
		# X axis lower bound label
		self.Label2DStatesConvertUnit = tk.Label( self.Frame2DStatesParam, text = "ConvertUnit" )
		self.Label2DStatesConvertUnit.place( x = 0, y = 0, width = 95, height = 28 )

		# X axis upper bound label
		self.Label2DStatesSampleInterval = tk.Label( self.Frame2DStatesParam, text = "SampleInterval" )
		self.Label2DStatesSampleInterval.place( x = 200, y = 0, width = 95, height = 28 )

	def Init3DPlotEntry( self ):
		# txt file path entry
		self.StringFilePath = tk.StringVar()
		self.EntryOpenFile = tk.Entry( self.Frame3DPlot, textvariable = self.StringFilePath )
		self.EntryOpenFile.place( x = 102, y = 2, width = 310, height = 28 )

		# xml parameter file path entry
		self.StringLoadParam = tk.StringVar()
		self.EntryLoadParam = tk.Entry( self.Frame3DPlot, textvariable = self.StringLoadParam )
		self.EntryLoadParam.place( x = 102, y = 35, width = 310, height = 28 )

		# X axis lower bound entry
		self.StringXAxisLower = tk.StringVar()
		self.EntryXAxisLower = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringXAxisLower )
		self.EntryXAxisLower.place( x = 97, y = 0, width = 100, height = 28 )

		# X axis upper bouond entry
		self.StringXAxisUpper = tk.StringVar()
		self.EntryXAxisUpper = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringXAxisUpper )
		self.EntryXAxisUpper.place( x = 300, y = 0, width = 100, height = 28 )

		# Y axis lower bound entry
		self.StringYAxisLower = tk.StringVar()
		self.EntryYAxisLower = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringYAxisLower )
		self.EntryYAxisLower.place( x = 97, y = 32, width = 100, height = 28 )

		# Y axis upper bouond entry
		self.StringYAxisUpper = tk.StringVar()
		self.EntryYAxisUpper = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringYAxisUpper )
		self.EntryYAxisUpper.place( x = 300, y = 32, width = 100, height = 28 )

		# Z axis lower bound entry
		self.StringZAxisLower = tk.StringVar()
		self.EntryZAxisLower = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringZAxisLower )
		self.EntryZAxisLower.place( x = 97, y = 64, width = 100, height = 28 )

		# X axis upper bound entry
		self.StringZAxisUpper = tk.StringVar()
		self.EntryZAxisUpper = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringZAxisUpper )
		self.EntryZAxisUpper.place( x = 300, y = 64, width = 100, height = 28 )

		# convert unit entry
		self.StringConvertUnit = tk.StringVar()
		self.EntryConvertUnit = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringConvertUnit )
		self.EntryConvertUnit.place( x = 97, y = 96, width = 100, height = 28 )

		# sample interval entry
		self.StringSampleInterval = tk.StringVar()
		self.EntrySampleInterval = tk.Entry( self.Frame3DPlotParam, textvariable = self.StringSampleInterval )
		self.EntrySampleInterval.place( x = 300, y = 96, width = 100, height = 28 )

	def Init2DStatesPlotEntry( self ):
		# joint states txt file path entry
		self.StringJointStatesFilePath = tk.StringVar()
		self.EntryJointStatesOpenFile = tk.Entry( self.Frame2DStatesPlot, textvariable = self.StringJointStatesFilePath )
		self.EntryJointStatesOpenFile.place( x = 102, y = 2, width = 310, height = 28 )

		# xml parameter file path entry
		self.String2DStatesPlotLoadParam = tk.StringVar()
		self.Entry2DStatesPlotLoadParam = tk.Entry( self.Frame2DStatesPlot, textvariable = self.String2DStatesPlotLoadParam )
		self.Entry2DStatesPlotLoadParam.place( x = 102, y = 34, width = 310, height = 28 )

		# convert unit entry
		self.String2DStatesPlotConvertUnit = tk.StringVar()
		self.Entry2DStatesPlotConvertUnit = tk.Entry( self.Frame2DStatesParam, textvariable = self.String2DStatesPlotConvertUnit )
		self.Entry2DStatesPlotConvertUnit.place( x = 97, y = 0, width = 100, height = 28 )

		# sample interval entry
		self.String2DStatesPlotSampleInterval = tk.StringVar()
		self.Entry2DStatesPlotSampleInterval = tk.Entry( self.Frame2DStatesParam, textvariable = self.String2DStatesPlotSampleInterval )
		self.Entry2DStatesPlotSampleInterval.place( x = 300, y = 0, width = 100, height = 28 )

	def Init3DPlotButton( self ):
		# button for open filedialog
		self.Pixel = tk.PhotoImage( width = 1, height = 1 )
		self.ButtonOpenFile = tk.Button( self.Frame3DPlot, text = "Open File", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : self.ButtonUtility.ButtonOpenClick( self.EntryOpenFile ) )
		self.ButtonOpenFile.place( x = 2, y = 2 )

		# button for loading parameters
		self.ButtonLoadParam = tk.Button( self.Frame3DPlot, text = "Load Param", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c" )
		self.ButtonLoadParam.config( command = lambda : self.ButtonUtility.ButtonLoadParamClick( self.EntryLoadParam, self.EntryXAxisLower, self.EntryXAxisUpper, self.EntryYAxisLower, self.EntryYAxisUpper, self.EntryZAxisLower, self.EntryZAxisUpper, self.EntryConvertUnit, self.EntrySampleInterval ) )
		self.ButtonLoadParam.place( x = 2, y = 34 )

		# button for starting to plot
		self.ButtonPlot = tk.Button( self.Frame3DPlot, text = "Plot", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonPlot.config( command = lambda : self.ButtonUtility.ButtonPlot( self.StringFilePath.get(), int( self.StringXAxisLower.get() ), int( self.StringXAxisUpper.get() ), int( self.StringYAxisLower.get() ), int( self.StringYAxisUpper.get() ), int( self.StringZAxisLower.get() ), int( self.StringZAxisUpper.get() ), int( self.StringConvertUnit.get() ), int( self.StringSampleInterval.get() ) ) )
		self.ButtonPlot.place( x = 2, y = 218 )

		# button for closing all figures
		self.ButtonCloseAllFigues = tk.Button( self.Frame3DPlot, text = "Close All Figs", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonCloseAllFigues.config( command = lambda : self.ButtonUtility.ButtonCloseAllFigues() )
		self.ButtonCloseAllFigues.place( x = 210, y = 218 )

	def Init2DStatesPlotButton( self ):
		# button for open filedialog
		self.ButtonJointStatesOpenFile = tk.Button( self.Frame2DStatesPlot, text = "Open Joints", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : self.ButtonUtility.ButtonOpenClick( self.EntryJointStatesOpenFile ) )
		self.ButtonJointStatesOpenFile.place( x = 2, y = 2 )

		# button for loading parameters
		self.Button2DStatesPlotLoadParam = tk.Button( self.Frame2DStatesPlot, text = "Load Param", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c" )
		self.Button2DStatesPlotLoadParam.config( command = lambda : self.ButtonUtility.Button2DStatesPlotLoadParamClick( self.Entry2DStatesPlotLoadParam, self.Entry2DStatesPlotConvertUnit, self.Entry2DStatesPlotSampleInterval ) )
		self.Button2DStatesPlotLoadParam.place( x = 2, y = 34 )

		# button for starting to plot
		self.Button2DStatesPlotPlot = tk.Button( self.Frame2DStatesPlot, text = "Plot", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.Button2DStatesPlotPlot.config( command = lambda : self.ButtonUtility.Button2DStatesPlot( self.StringJointStatesFilePath.get(), int( self.String2DStatesPlotConvertUnit.get() ), int( self.String2DStatesPlotSampleInterval.get() ) ) )
		self.Button2DStatesPlotPlot.place( x = 2, y = 121 )

		# button for closing all figures
		self.Button2DStatesPlotCloseAllFigues = tk.Button( self.Frame2DStatesPlot, text = "Close All Figs", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.Button2DStatesPlotCloseAllFigues.config( command = lambda : self.ButtonUtility.ButtonCloseAllFigues() )
		self.Button2DStatesPlotCloseAllFigues.place( x = 210, y = 121 )

	def GuiMainloop( self ):
		self.Win.mainloop()
