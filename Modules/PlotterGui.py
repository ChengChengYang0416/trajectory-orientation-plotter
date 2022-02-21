import tkinter as tk
from Modules.ButtonUtility import CButtonUtility

class CPlotterGui:
	def __init__( self ):
		self.Win = tk.Tk()
		self.InitBasicSetting()
		self.InitFrameForLabelEntry()
		self.InitLabel()
		self.InitEntry()
		self.InitButton()

	def InitBasicSetting( self ):
		# set title
		self.Win.title( "Plotter Gui" )

		# set geometry of window ( width x height )
		self.Win.geometry( "430x277" )
		self.Win.resizable( False, False )

		# color, transparency, pin on top
		self.Win.config( background = "#C0C0C0" )
		self.Win.attributes( "-topmost", True )

	def InitFrameForLabelEntry( self ):
		self.FrameParam = tk.LabelFrame( width = 410, height = 150, text = "parameters" )
		self.FrameParam.place( x = 10, y = 80 )

	def InitLabel( self ):
		# X axis lower bound label
		self.LabelXAxisLower = tk.Label( self.FrameParam, text = "XAxisLower" )
		self.LabelXAxisLower.place( x = 0, y = 0, width = 95, height = 28 )

		# X axis upper bound label
		self.LabelXAxisUpper = tk.Label( self.FrameParam, text = "XAxisUpper" )
		self.LabelXAxisUpper.place( x = 200, y = 0, width = 95, height = 28 )

		# Y axis lower bound label
		self.LabelYAxisLower = tk.Label( self.FrameParam, text = "YAxisLower" )
		self.LabelYAxisLower.place( x = 0, y = 32, width = 95, height = 28 )

		# Y axis upper bound label
		self.LabelYAxisUpper = tk.Label( self.FrameParam, text = "YAxisUpper" )
		self.LabelYAxisUpper.place( x = 200, y = 32, width = 95, height = 28 )

		# Z axis lower bound label
		self.LabelZAxisLower = tk.Label( self.FrameParam, text = "ZAxisLower" )
		self.LabelZAxisLower.place( x = 0, y = 64, width = 95, height = 28 )

		# Z axis upper bound label
		self.LabelZAxisUpper = tk.Label( self.FrameParam, text = "ZAxisUpper" )
		self.LabelZAxisUpper.place( x = 200, y = 64, width = 95, height = 28 )

		# convert unit label
		self.LabelConvertUnit = tk.Label( self.FrameParam, text = "ConvertUnit" )
		self.LabelConvertUnit.place( x = 0, y = 96, width = 95, height = 28 )

		# sample interval label
		self.LabelSampleInterval = tk.Label( self.FrameParam, text = "SampleInterval" )
		self.LabelSampleInterval.place( x = 200, y = 96, width = 95, height = 28 )

	def InitEntry( self ):
		# txt file path entry
		self.StringFilePath = tk.StringVar()
		self.EntryOpenFile = tk.Entry( textvariable = self.StringFilePath )
		self.EntryOpenFile.place( x = 110, y = 9, width = 310, height = 28 )

		# xml parameter file path entry
		self.StringLoadParam = tk.StringVar()
		self.EntryLoadParam = tk.Entry( textvariable = self.StringLoadParam )
		self.EntryLoadParam.place( x = 110, y = 45, width = 310, height = 28 )

		# X axis lower bound entry
		self.StringXAxisLower = tk.StringVar()
		self.EntryXAxisLower = tk.Entry( self.FrameParam, textvariable = self.StringXAxisLower )
		self.EntryXAxisLower.place( x = 97, y = 0, width = 100, height = 28 )

		# X axis upper bouond entry
		self.StringXAxisUpper = tk.StringVar()
		self.EntryXAxisUpper = tk.Entry( self.FrameParam, textvariable = self.StringXAxisUpper )
		self.EntryXAxisUpper.place( x = 300, y = 0, width = 100, height = 28 )

		# Y axis lower bound entry
		self.StringYAxisLower = tk.StringVar()
		self.EntryYAxisLower = tk.Entry( self.FrameParam, textvariable = self.StringYAxisLower )
		self.EntryYAxisLower.place( x = 97, y = 32, width = 100, height = 28 )

		# Y axis upper bouond entry
		self.StringYAxisUpper = tk.StringVar()
		self.EntryYAxisUpper = tk.Entry( self.FrameParam, textvariable = self.StringYAxisUpper )
		self.EntryYAxisUpper.place( x = 300, y = 32, width = 100, height = 28 )

		# Z axis lower bound entry
		self.StringZAxisLower = tk.StringVar()
		self.EntryZAxisLower = tk.Entry( self.FrameParam, textvariable = self.StringZAxisLower )
		self.EntryZAxisLower.place( x = 97, y = 64, width = 100, height = 28 )

		# X axis upper bound entry
		self.StringZAxisUpper = tk.StringVar()
		self.EntryZAxisUpper = tk.Entry( self.FrameParam, textvariable = self.StringZAxisUpper )
		self.EntryZAxisUpper.place( x = 300, y = 64, width = 100, height = 28 )

		# convert unit entry
		self.StringConvertUnit = tk.StringVar()
		self.EntryConvertUnit = tk.Entry( self.FrameParam, textvariable = self.StringConvertUnit )
		self.EntryConvertUnit.place( x = 97, y = 96, width = 100, height = 28 )

		# sample interval entry
		self.StringSampleInterval = tk.StringVar()
		self.EntrySampleInterval = tk.Entry( self.FrameParam, textvariable = self.StringSampleInterval )
		self.EntrySampleInterval.place( x = 300, y = 96, width = 100, height = 28 )

	def InitButton( self ):
		# button object
		self.ButtonUtility = CButtonUtility()

		# button for open filedialog
		self.Pixel = tk.PhotoImage( width = 1, height = 1 )
		self.ButtonOpenFile = tk.Button( text = "Open File", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : self.ButtonUtility.ButtonOpenClick( self.EntryOpenFile ) )
		self.ButtonOpenFile.place( x = 10, y = 10 )

		# button for loading parameters
		self.ButtonLoadParam = tk.Button( text = "Load Param", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c" )
		self.ButtonLoadParam.config( command = lambda : self.ButtonUtility.ButtonLoadParamClick( self.EntryLoadParam, self.EntryXAxisLower, self.EntryXAxisUpper, self.EntryYAxisLower, self.EntryYAxisUpper, self.EntryZAxisLower, self.EntryZAxisUpper, self.EntryConvertUnit, self.EntrySampleInterval ) )
		self.ButtonLoadParam.place( x = 10, y = 45 )

		# button for starting to plot
		self.ButtonPlot = tk.Button( text = "Plot", image = self.Pixel, background = "#FFFFFF", width = 405, height = 20, compound = "c" )
		self.ButtonPlot.config( command = lambda : self.ButtonUtility.ButtonPlot( self.StringFilePath.get(), int( self.StringXAxisLower.get() ), int( self.StringXAxisUpper.get() ), int( self.StringYAxisLower.get() ), int( self.StringYAxisUpper.get() ), int( self.StringZAxisLower.get() ), int( self.StringZAxisUpper.get() ), int( self.StringConvertUnit.get() ), int( self.StringSampleInterval.get() ) ) )
		self.ButtonPlot.place( x = 10, y = 238 )

	def GuiMainloop( self ):
		self.Win.mainloop()
