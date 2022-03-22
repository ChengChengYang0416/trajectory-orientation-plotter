import tkinter as tk
from Modules.ButtonUtilityMainWin import CButtonUtilityMainWin

class CPlotterGui:
	def __init__( self ):
		self.Win = tk.Tk()
		self.InitBasicSetting()
		self.InitFrame()
		self.InitButton()

	def InitBasicSetting( self ):
		# set title
		self.Win.title( "Plotter Gui" )

		# set geometry of window ( width x height )
		self.Win.geometry( "211x215" )
		self.Win.resizable( False, False )

		# color, transparency, pin on top
		self.Win.config( background = "#C0C0C0" )
		self.Win.attributes( "-topmost", True )

	def InitFrame( self ):
		# frame for 3D plot
		self.Frame3DPlot = tk.LabelFrame( width = 200, height = 65, text = "3D Graph" )
		self.Frame3DPlot.place( x = 5, y = 5 )

		# frame for XYZABC plot
		self.FrameXYZABCPlot = tk.LabelFrame( width = 200, height = 65, text = "XYZABC Graph" )
		self.FrameXYZABCPlot.place( x = 5, y = 75 )

		# frame for joint states plot
		self.FrameJointsPlot = tk.LabelFrame( width = 200, height = 65, text = "Joint States Graph" )
		self.FrameJointsPlot.place( x = 5, y = 145 )

	def InitButton( self ):
		# button object
		self.ButtonUtilityMainWin = CButtonUtilityMainWin()

		# button pixel
		self.Pixel = tk.PhotoImage( width = 1, height = 1 )

		self.Init3DPlotWindowButton()
		self.InitXYZABCPlotWindowButton()
		self.InitJointsPlotWindowButton()

	def Init3DPlotWindowButton( self ):
		self.ButtonCreate3DPlotWindow = tk.Button( self.Frame3DPlot, text = "Plot 3D graph", image = self.Pixel, background = "#FFFFFF", width = 120, height = 20, compound = "c", command = lambda : self.ButtonUtilityMainWin.ButtonCreate3DPlotWindowClick( self.Win ) )
		self.ButtonCreate3DPlotWindow.place( x = 35, y = 5 )

	def InitXYZABCPlotWindowButton( self ):
		self.ButtonCreateXYZABCPlotWindow = tk.Button( self.FrameXYZABCPlot, text = "Plot XYZABC graph", image = self.Pixel, background = "#FFFFFF", width = 120, height = 20, compound = "c" )
		self.ButtonCreateXYZABCPlotWindow.place( x = 35, y = 5 )

	def InitJointsPlotWindowButton( self ):
		self.ButtonCreateJointsPlotWindow = tk.Button( self.FrameJointsPlot, text = "Plot Joints graph", image = self.Pixel, background = "#FFFFFF", width = 120, height = 20, compound = "c" )
		self.ButtonCreateJointsPlotWindow.place( x = 35, y = 5 )

	def GuiMainloop( self ):
		self.Win.mainloop()
