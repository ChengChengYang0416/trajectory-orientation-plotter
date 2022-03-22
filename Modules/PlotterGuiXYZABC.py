import tkinter as tk
from Modules.ButtonUtility import CButtonUtility

class CPlotterGuiXYZABC:
	def __init__( self, PlotXYZABCWindow ):
		self.Win = PlotXYZABCWindow
		self.InitBasicSetting()
		self.InitFrame()
		self.InitLabel()
		self.InitEntry()
		self.InitButton()

	def InitBasicSetting( self ):
		# set title
		self.Win.title( "Plotter Gui XYZABC" )

		# set geometry of window ( width x height )
		self.Win.geometry( "430x143" )
		self.Win.resizable( False, False )

		# color, transparency, pin on top
		self.Win.config( background = "#C0C0C0" )
		self.Win.attributes( "-topmost", True )

	def InitFrame( self ):
		# frame for XYZABC states plot
		self.FrameXYZABCStatesPlot = tk.LabelFrame( self.Win, width = 420, height = 133, text = "XYZABC States Plot" )
		self.FrameXYZABCStatesPlot.place( x = 5, y = 5 )

		# frame for parameters of XYZABC states plot
		self.FrameXYZABCStatesParam = tk.LabelFrame( self.FrameXYZABCStatesPlot, width = 410, height = 53, text = "Parameters" )
		self.FrameXYZABCStatesParam.place( x = 3, y = 28 )

	def InitLabel( self ):
		self.InitXYZABCStatesPlotLabel()

	def InitEntry( self ):
		self.InitXYZABCStatesPlotEntry()

	def InitButton( self ):
		# button object
		self.ButtonUtility = CButtonUtility()

		# button pixel
		self.Pixel = tk.PhotoImage( width = 1, height = 1 )

		self.InitXYZABCStatesPlotButton()

	def InitXYZABCStatesPlotLabel( self ):
		# convert unit label
		self.LabelXYZABCStatesConvertUnit = tk.Label( self.FrameXYZABCStatesParam, text = "ConvertUnit" )
		self.LabelXYZABCStatesConvertUnit.place( x = 0, y = 0, width = 95, height = 28 )

		# sample interval label
		self.LabelXYZABCStatesSampleInterval = tk.Label( self.FrameXYZABCStatesParam, text = "SampleInterval" )
		self.LabelXYZABCStatesSampleInterval.place( x = 200, y = 0, width = 95, height = 28 )

	def InitXYZABCStatesPlotEntry( self ):
		# XYZABC states txt file path entry
		self.StringXYZABCStatesFilePath = tk.StringVar()
		self.EntryXYZABCStatesOpenFile = tk.Entry( self.FrameXYZABCStatesPlot, textvariable = self.StringXYZABCStatesFilePath )
		self.EntryXYZABCStatesOpenFile.place( x = 102, y = 2, width = 310, height = 28 )

		# convert unit entry
		self.StringXYZABCStatesPlotConvertUnit = tk.StringVar()
		self.EntryXYZABCStatesPlotConvertUnit = tk.Entry( self.FrameXYZABCStatesParam, textvariable = self.StringXYZABCStatesPlotConvertUnit )
		self.EntryXYZABCStatesPlotConvertUnit.place( x = 97, y = 0, width = 100, height = 28 )

		# sample interval entry
		self.StringXYZABCStatesPlotSampleInterval = tk.StringVar()
		self.EntryXYZABCStatesPlotSampleInterval = tk.Entry( self.FrameXYZABCStatesParam, textvariable = self.StringXYZABCStatesPlotSampleInterval )
		self.EntryXYZABCStatesPlotSampleInterval.place( x = 300, y = 0, width = 100, height = 28 )

	def InitXYZABCStatesPlotButton( self ):
		# button for open filedialog
		self.ButtonXYZABCStatesOpenFile = tk.Button( self.FrameXYZABCStatesPlot, text = "Open XYZABC", image = self.Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : self.ButtonUtility.ButtonOpenClick( self.EntryXYZABCStatesOpenFile ) )
		self.ButtonXYZABCStatesOpenFile.place( x = 2, y = 2 )

		# button for starting to plot
		self.ButtonXYZABCStatesPlotPlot = tk.Button( self.FrameXYZABCStatesPlot, text = "Plot", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonXYZABCStatesPlotPlot.config( command = lambda : self.ButtonUtility.ButtonXYZABCStatesPlot( self.StringXYZABCStatesFilePath.get(), int( self.StringXYZABCStatesPlotConvertUnit.get() ), int( self.StringXYZABCStatesPlotSampleInterval.get() ) ) )
		self.ButtonXYZABCStatesPlotPlot.place( x = 2, y = 83 )

		# button for closing all figures
		self.ButtonXYZABCStatesPlotCloseAllFigues = tk.Button( self.FrameXYZABCStatesPlot, text = "Close All Figs", image = self.Pixel, background = "#FFFFFF", width = 194, height = 20, compound = "c" )
		self.ButtonXYZABCStatesPlotCloseAllFigues.config( command = lambda : self.ButtonUtility.ButtonCloseAllFigues() )
		self.ButtonXYZABCStatesPlotCloseAllFigues.place( x = 210, y = 83 )

	def GuiMainloop( self ):
		self.Win.mainloop()
