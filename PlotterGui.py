from calendar import c
import tkinter as tk
from Modules import ButtonUtility

# build main window
Win = tk.Tk()

#------------------- basic setting -------------------#
# set title
Win.title( "Plotter Gui" )

# set geometry of window ( width x height )
Win.geometry( "400x300" )
Win.minsize( width = 400, height = 300 )
Win.maxsize( width = 800, height = 600 )
Win.resizable( True, True )

# color, transparency, pin on top
Win.config( background = "#C0C0C0" )
Win.attributes( "-topmost", True )
#------------------- end of basic setting -------------------#

StringFilePath = tk.StringVar()
EntryOpenFile = tk.Entry( textvariable = StringFilePath )
EntryOpenFile.place( x = 105, y = 9, width = 200, height = 28 )

# button for open filedialog
Pixel = tk.PhotoImage( width = 1, height = 1 )
ButtonOpenFile = tk.Button( text = "Open File", image = Pixel, background = "#FFFFFF", width = 80, height = 20, compound = "c", command = lambda : ButtonUtility.ButtonOpenClick( EntryOpenFile ) )
ButtonOpenFile.place( x = 10, y = 10 )

# button for starting to plot
ButtonPlot = tk.Button( text = "Plot", image = Pixel, background = "#FFFFFF", width = 80, height = 20, compound = "c", command = lambda : ButtonUtility.ButtonPlot( StringFilePath.get() ) )
ButtonPlot.place( x = 10, y = 50 )

Win.mainloop()
