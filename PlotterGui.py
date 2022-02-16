from calendar import c
import tkinter as tk
from Modules import ButtonUtility

# build main window
Win = tk.Tk()

#------------------- basic setting -------------------#
# set title
Win.title( "Plotter Gui" )

# set geometry of window ( width x height )
Win.geometry( "430x277" )
Win.resizable( False, False )

# color, transparency, pin on top
Win.config( background = "#C0C0C0" )
Win.attributes( "-topmost", True )
#------------------- end of basic setting -------------------#

# label
LabelXAxisLower = tk.Label( text = "XAxisLower" )
LabelXAxisLower.place( x = 10, y = 80, width = 95, height = 28 )

LabelXAxisUpper = tk.Label( text = "XAxisUpper" )
LabelXAxisUpper.place( x = 220, y = 80, width = 95, height = 28 )

LabelYAxisLower = tk.Label( text = "YAxisLower" )
LabelYAxisLower.place( x = 10, y = 120, width = 95, height = 28 )

LabelYAxisUpper = tk.Label( text = "YAxisUpper" )
LabelYAxisUpper.place( x = 220, y = 120, width = 95, height = 28 )

LabelZAxisLower = tk.Label( text = "ZAxisLower" )
LabelZAxisLower.place( x = 10, y = 160, width = 95, height = 28 )

LabelZAxisUpper = tk.Label( text = "ZAxisUpper" )
LabelZAxisUpper.place( x = 220, y = 160, width = 95, height = 28 )

LabelConvertUnit = tk.Label( text = "ConvertUnit" )
LabelConvertUnit.place( x = 10, y = 200, width = 95, height = 28 )

LabelSampleInterval = tk.Label( text = "SampleInterval" )
LabelSampleInterval.place( x = 220, y = 200, width = 95, height = 28 )

# entry
StringFilePath = tk.StringVar()
EntryOpenFile = tk.Entry( textvariable = StringFilePath )
EntryOpenFile.place( x = 110, y = 9, width = 310, height = 28 )

StringLoadParam = tk.StringVar()
EntryLoadParam = tk.Entry( textvariable = StringLoadParam )
EntryLoadParam.place( x = 110, y = 45, width = 310, height = 28 )

StringXAxisLower = tk.StringVar()
EntryXAxisLower = tk.Entry( textvariable = StringXAxisLower )
EntryXAxisLower.place( x = 110, y = 80, width = 100, height = 28 )

StringXAxisUpper = tk.StringVar()
EntryXAxisUpper = tk.Entry( textvariable = StringXAxisUpper )
EntryXAxisUpper.place( x = 320, y = 80, width = 100, height = 28 )

StringYAxisLower = tk.StringVar()
EntryYAxisLower = tk.Entry( textvariable = StringYAxisLower )
EntryYAxisLower.place( x = 110, y = 120, width = 100, height = 28 )

StringYAxisUpper = tk.StringVar()
EntryYAxisUpper = tk.Entry( textvariable = StringYAxisUpper )
EntryYAxisUpper.place( x = 320, y = 120, width = 100, height = 28 )

StringZAxisLower = tk.StringVar()
EntryZAxisLower = tk.Entry( textvariable = StringZAxisLower )
EntryZAxisLower.place( x = 110, y = 160, width = 100, height = 28 )

StringZAxisUpper = tk.StringVar()
EntryZAxisUpper = tk.Entry( textvariable = StringZAxisUpper )
EntryZAxisUpper.place( x = 320, y = 160, width = 100, height = 28 )

StringConvertUnit = tk.StringVar()
EntryConvertUnit = tk.Entry( textvariable = StringConvertUnit )
EntryConvertUnit.place( x = 110, y = 200, width = 100, height = 28 )

StringSampleInterval = tk.StringVar()
EntrySampleInterval = tk.Entry( textvariable = StringSampleInterval )
EntrySampleInterval.place( x = 320, y = 200, width = 100, height = 28 )

# button for open filedialog
Pixel = tk.PhotoImage( width = 1, height = 1 )
ButtonOpenFile = tk.Button( text = "Open File", image = Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c", command = lambda : ButtonUtility.ButtonOpenClick( EntryOpenFile ) )
ButtonOpenFile.place( x = 10, y = 10 )

# button for loading parameters
ButtonLoadParam = tk.Button( text = "Load Param", image = Pixel, background = "#FFFFFF", width = 88, height = 20, compound = "c" )
ButtonLoadParam.config( command = lambda : ButtonUtility.ButtonLoadParamClick( EntryLoadParam, EntryXAxisLower, EntryXAxisUpper, EntryYAxisLower, EntryYAxisUpper, EntryZAxisLower, EntryZAxisUpper, EntryConvertUnit, EntrySampleInterval ) )
ButtonLoadParam.place( x = 10, y = 45 )

# button for starting to plot
ButtonPlot = tk.Button( text = "Plot", image = Pixel, background = "#FFFFFF", width = 405, height = 20, compound = "c" )
ButtonPlot.config( command = lambda : ButtonUtility.ButtonPlot( StringFilePath.get(), int( StringXAxisLower.get() ), int( StringXAxisUpper.get() ), int( StringYAxisLower.get() ), int( StringYAxisUpper.get() ), int( StringZAxisLower.get() ), int( StringZAxisUpper.get() ), int( StringConvertUnit.get() ), int( StringSampleInterval.get() ) ) )
ButtonPlot.place( x = 10, y = 238 )

Win.mainloop()
