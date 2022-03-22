import tkinter as tk
from Modules.ButtonUtility import CButtonUtility

class CPlotterGuiJoints:
	def __init__( self, Plot3DWindow ):
		self.Win = Plot3DWindow
		self.InitBasicSetting()
		self.InitFrame()
		self.InitLabel()
		self.InitEntry()
		self.InitButton()

	def InitBasicSetting( self ):
		# set title
		self.Win.title( "Plotter Gui Joints" )

		# set geometry of window ( width x height )
		self.Win.geometry( "430x143" )
		self.Win.resizable( False, False )

		# color, transparency, pin on top
		self.Win.config( background = "#C0C0C0" )
		self.Win.attributes( "-topmost", True )

	def InitFrame( self ):
		# frame for joint states plot
		self.FrameJointStatesPlot = tk.LabelFrame( self.Win, width = 420, height = 133, text = "Joint States Plot" )
		self.FrameJointStatesPlot.place( x = 5, y = 5 )

		# frame for parameters of joint states plot
		self.FrameJointStatesParam = tk.LabelFrame( self.FrameJointStatesPlot, width = 410, height = 53, text = "Parameters" )
		self.FrameJointStatesParam.place( x = 3, y = 28 )

	def InitLabel( self ):
		self.InitJointStatesPlotLabel()

	def InitEntry( self ):
		self.InitJointStatesPlotEntry()

	def InitButton( self ):
		# button object
		self.ButtonUtility = CButtonUtility()

		# button pixel
		self.Pixel = tk.PhotoImage( width = 1, height = 1 )

		self.InitJointStatesPlotButton()

	def InitJointStatesPlotLabel( self ):
		# convert unit label
		self.LabelJointStatesConvertUnit = tk.Label( self.FrameJointStatesParam, text = "ConvertUnit" )
		self.LabelJointStatesConvertUnit.place( x = 0, y = 0, width = 95, height = 28 )

		# sample interval label
		self.LabelJointStatesSampleInterval = tk.Label( self.FrameJointStatesParam, text = "SampleInterval" )
		self.LabelJointStatesSampleInterval.place( x = 200, y = 0, width = 95, height = 28 )

	def InitJointStatesPlotEntry( self ):
		# joint states txt file path entry
		self.StringJointStatesFilePath = tk.StringVar()
		self.EntryJointStatesOpenFile = tk.Entry( self.FrameJointStatesPlot, textvariable = self.StringJointStatesFilePath )
		self.EntryJointStatesOpenFile.place( x = 102, y = 2, width = 310, height = 28 )

		# convert unit entry
		self.StringJointStatesPlotConvertUnit = tk.StringVar()
		self.EntryJointStatesPlotConvertUnit = tk.Entry( self.FrameJointStatesParam, textvariable = self.StringJointStatesPlotConvertUnit )
		self.EntryJointStatesPlotConvertUnit.place( x = 97, y = 0, width = 100, height = 28 )

		# sample interval entry
		self.StringJointStatesPlotSampleInterval = tk.StringVar()
		self.EntryJointStatesPlotSampleInterval = tk.Entry( self.FrameJointStatesParam, textvariable = self.StringJointStatesPlotSampleInterval )
		self.EntryJointStatesPlotSampleInterval.place( x = 300, y = 0, width = 100, height = 28 )

	def InitJointStatesPlotButton( self ):
		# button for open filedialog
		self.ButtonJointStatesOpenFile = tk.Button( self.FrameJointStatesPlot, text = "Open Joints", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : self.ButtonUtility.ButtonOpenClick( self.EntryJointStatesOpenFile ) )
		self.ButtonJointStatesOpenFile.place( x = 2, y = 2 )

		# button for starting to plot
		self.ButtonJointStatesPlotPlot = tk.Button( self.FrameJointStatesPlot, text = "Plot", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonJointStatesPlotPlot.config( command = lambda : self.ButtonUtility.ButtonJointStatesPlot( self.StringJointStatesFilePath.get(), int( self.StringJointStatesPlotConvertUnit.get() ), int( self.StringJointStatesPlotSampleInterval.get() ) ) )
		self.ButtonJointStatesPlotPlot.place( x = 2, y = 83 )

		# button for closing all figures
		self.ButtonJointStatesPlotCloseAllFigues = tk.Button( self.FrameJointStatesPlot, text = "Close All Figs", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonJointStatesPlotCloseAllFigues.config( command = lambda : self.ButtonUtility.ButtonCloseAllFigues() )
		self.ButtonJointStatesPlotCloseAllFigues.place( x = 210, y = 83 )

	def GuiMainloop( self ):
		self.Win.mainloop()
