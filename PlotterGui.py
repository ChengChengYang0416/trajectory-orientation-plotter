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

# frame for parameters
FrameParam = tk.LabelFrame( width = 410, height = 150, text = "parameters" )
FrameParam.place( x = 10, y = 80 )

# label
LabelXAxisLower = tk.Label( FrameParam, text = "XAxisLower" )
LabelXAxisLower.place( x = 0, y = 0, width = 95, height = 28 )

LabelXAxisUpper = tk.Label( FrameParam, text = "XAxisUpper" )
LabelXAxisUpper.place( x = 200, y = 0, width = 95, height = 28 )

LabelYAxisLower = tk.Label( FrameParam, text = "YAxisLower" )
LabelYAxisLower.place( x = 0, y = 32, width = 95, height = 28 )

LabelYAxisUpper = tk.Label( FrameParam, text = "YAxisUpper" )
LabelYAxisUpper.place( x = 200, y = 32, width = 95, height = 28 )

LabelZAxisLower = tk.Label( FrameParam, text = "ZAxisLower" )
LabelZAxisLower.place( x = 0, y = 64, width = 95, height = 28 )

LabelZAxisUpper = tk.Label( FrameParam, text = "ZAxisUpper" )
LabelZAxisUpper.place( x = 200, y = 64, width = 95, height = 28 )

LabelConvertUnit = tk.Label( FrameParam, text = "ConvertUnit" )
LabelConvertUnit.place( x = 0, y = 96, width = 95, height = 28 )

LabelSampleInterval = tk.Label( FrameParam, text = "SampleInterval" )
LabelSampleInterval.place( x = 200, y = 96, width = 95, height = 28 )

# entry
StringFilePath = tk.StringVar()
EntryOpenFile = tk.Entry( textvariable = StringFilePath )
EntryOpenFile.place( x = 110, y = 9, width = 310, height = 28 )

StringLoadParam = tk.StringVar()
EntryLoadParam = tk.Entry( textvariable = StringLoadParam )
EntryLoadParam.place( x = 110, y = 45, width = 310, height = 28 )

StringXAxisLower = tk.StringVar()
EntryXAxisLower = tk.Entry( FrameParam, textvariable = StringXAxisLower )
EntryXAxisLower.place( x = 97, y = 0, width = 100, height = 28 )

StringXAxisUpper = tk.StringVar()
EntryXAxisUpper = tk.Entry( FrameParam, textvariable = StringXAxisUpper )
EntryXAxisUpper.place( x = 300, y = 0, width = 100, height = 28 )

StringYAxisLower = tk.StringVar()
EntryYAxisLower = tk.Entry( FrameParam, textvariable = StringYAxisLower )
EntryYAxisLower.place( x = 97, y = 32, width = 100, height = 28 )

StringYAxisUpper = tk.StringVar()
EntryYAxisUpper = tk.Entry( FrameParam, textvariable = StringYAxisUpper )
EntryYAxisUpper.place( x = 300, y = 32, width = 100, height = 28 )

StringZAxisLower = tk.StringVar()
EntryZAxisLower = tk.Entry( FrameParam, textvariable = StringZAxisLower )
EntryZAxisLower.place( x = 97, y = 64, width = 100, height = 28 )

StringZAxisUpper = tk.StringVar()
EntryZAxisUpper = tk.Entry( FrameParam, textvariable = StringZAxisUpper )
EntryZAxisUpper.place( x = 300, y = 64, width = 100, height = 28 )

StringConvertUnit = tk.StringVar()
EntryConvertUnit = tk.Entry( FrameParam, textvariable = StringConvertUnit )
EntryConvertUnit.place( x = 97, y = 96, width = 100, height = 28 )

StringSampleInterval = tk.StringVar()
EntrySampleInterval = tk.Entry( FrameParam, textvariable = StringSampleInterval )
EntrySampleInterval.place( x = 300, y = 96, width = 100, height = 28 )

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
