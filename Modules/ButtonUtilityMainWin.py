import tkinter as tk
from Modules.PlotterGui3D import CPlotterGui3D

class CButtonUtilityMainWin:
	def ButtonCreate3DPlotWindowClick( self, Win ):
		Plot3DWindow = tk.Toplevel( Win )
		PlotterGui3D = CPlotterGui3D( Plot3DWindow )
		PlotterGui3D.GuiMainloop()
