import tkinter as tk
from Modules.PlotterGui3D import CPlotterGui3D
from Modules.PlotterGuiXYZABC import CPlotterGuiXYZABC
from Modules.PlotterGuiJoints import CPlotterGuiJoints

class CButtonUtilityMainWin:
	def ButtonCreate3DPlotWindowClick( self, Win ):
		Plot3DWindow = tk.Toplevel( Win )
		PlotterGui3D = CPlotterGui3D( Plot3DWindow )
		PlotterGui3D.GuiMainloop()

	def ButtonCreateXYZABCPlotWindowClick( self, Win ):
		PlotXYZABCWindow = tk.Toplevel( Win )
		PlotterGuiXYZABC = CPlotterGuiXYZABC( PlotXYZABCWindow )
		PlotterGuiXYZABC.GuiMainloop()

	def ButtonCreateJointsPlotWindowClick( self, Win ):
		PlotJointsWindow = tk.Toplevel( Win )
		PlotterGuiJoints = CPlotterGuiJoints( PlotJointsWindow )
		PlotterGuiJoints.GuiMainloop()
