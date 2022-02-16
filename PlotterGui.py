from calendar import c
import tkinter as tk
from Modules import ButtonUtility

# build main window
Win = tk.Tk()

#------------------- basic setting -------------------#
# set title
Win.title( "Plotter Gui" )

# set geometry of window ( width x height )
Win.geometry( "430x300" )
Win.minsize( width = 400, height = 300 )
Win.maxsize( width = 800, height = 600 )
Win.resizable( True, True )

# color, transparency, pin on top
Win.config( background = "#C0C0C0" )
Win.attributes( "-topmost", True )
#------------------- end of basic setting -------------------#

# label
LabelXAxisLower = tk.Label( text = "XAxisLower" )
LabelXAxisLower.place( x = 10, y = 60, width = 95, height = 28 )

LabelXAxisUpper = tk.Label( text = "XAxisUpper" )
LabelXAxisUpper.place( x = 220, y = 60, width = 95, height = 28 )

LabelYAxisLower = tk.Label( text = "YAxisLower" )
LabelYAxisLower.place( x = 10, y = 100, width = 95, height = 28 )

LabelYAxisUpper = tk.Label( text = "YAxisUpper" )
LabelYAxisUpper.place( x = 220, y = 100, width = 95, height = 28 )

LabelZAxisLower = tk.Label( text = "ZAxisLower" )
LabelZAxisLower.place( x = 10, y = 140, width = 95, height = 28 )

LabelZAxisUpper = tk.Label( text = "ZAxisUpper" )
LabelZAxisUpper.place( x = 220, y = 140, width = 95, height = 28 )

LabelConvertUnit = tk.Label( text = "ConvertUnit" )
LabelConvertUnit.place( x = 10, y = 180, width = 95, height = 28 )

LabelSampleInterval = tk.Label( text = "SampleInterval" )
LabelSampleInterval.place( x = 220, y = 180, width = 95, height = 28 )

# entry
StringFilePath = tk.StringVar()
EntryOpenFile = tk.Entry( textvariable = StringFilePath )
EntryOpenFile.place( x = 110, y = 9, width = 310, height = 28 )

StringXAxisLower = tk.StringVar()
EntryXAxisLower = tk.Entry( textvariable = StringXAxisLower )
EntryXAxisLower.place( x = 110, y = 60, width = 100, height = 28 )

StringXAxisUpper = tk.StringVar()
EntryXAxisUpper = tk.Entry( textvariable = StringXAxisUpper )
EntryXAxisUpper.place( x = 320, y = 60, width = 100, height = 28 )

StringYAxisLower = tk.StringVar()
EntryYAxisLower = tk.Entry( textvariable = StringYAxisLower )
EntryYAxisLower.place( x = 110, y = 100, width = 100, height = 28 )

StringYAxisUpper = tk.StringVar()
EntryYAxisUpper = tk.Entry( textvariable = StringYAxisUpper )
EntryYAxisUpper.place( x = 320, y = 100, width = 100, height = 28 )

StringZAxisLower = tk.StringVar()
EntryZAxisLower = tk.Entry( textvariable = StringYAxisLower )
EntryZAxisLower.place( x = 110, y = 140, width = 100, height = 28 )

StringZAxisUpper = tk.StringVar()
EntryZAxisUpper = tk.Entry( textvariable = StringZAxisUpper )
EntryZAxisUpper.place( x = 320, y = 140, width = 100, height = 28 )

StringConvertUnit = tk.StringVar()
EntryConvertUnit = tk.Entry( textvariable = StringConvertUnit )
EntryConvertUnit.place( x = 110, y = 180, width = 100, height = 28 )

StringSampleInterval = tk.StringVar()
EntrySampleInterval = tk.Entry( textvariable = StringSampleInterval )
EntrySampleInterval.place( x = 320, y = 180, width = 100, height = 28 )

# button for open filedialog
Pixel = tk.PhotoImage( width = 1, height = 1 )
ButtonOpenFile = tk.Button( text = "Open File", image = Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : ButtonUtility.ButtonOpenClick( EntryOpenFile ) )
ButtonOpenFile.place( x = 10, y = 10 )

# button for starting to plot
ButtonPlot = tk.Button( text = "Plot", image = Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : ButtonUtility.ButtonPlot( StringFilePath.get() ) )
ButtonPlot.place( x = 10, y = 250 )

Win.mainloop()
