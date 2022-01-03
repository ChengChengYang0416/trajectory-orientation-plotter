import xml.etree.ElementTree as ET

def GetPlotterParameters():
    # initialize dictionary
    Parameters = { 'Filename' : 0, 'UnitConvert' : 0, 'SamplingInterval' : 0, 'XAxisLower' : 0, 'XAxisUpper' : 0, 'YAxisLower' : 0, 'YAxisUpper' : 0, 'ZAxisLower' : 0, 'ZAxisUpper' : 0 }

    # read parameters from XML
    tree = ET.parse( 'Parameters.xml' )
    root = tree.getroot()
    for child in root:
        if child.tag == 'Filename':
            Parameters[ 'Filename' ] = child.text

        if child.tag == 'UnitConvert':
            Parameters[ 'UnitConvert' ] = int( child.text )

        if child.tag == 'SamplingInterval':
            Parameters[ 'SamplingInterval' ] = int( child.text )

        if child.tag == 'XAxisLower':
            Parameters[ 'XAxisLower' ] = int( child.text )

        if child.tag == 'XAxisUpper':
            Parameters[ 'XAxisUpper' ] = int( child.text )

        if child.tag == 'YAxisLower':
            Parameters[ 'YAxisLower' ] = int( child.text )

        if child.tag == 'YAxisUpper':
            Parameters[ 'YAxisUpper' ] = int( child.text )

        if child.tag == 'ZAxisLower':
            Parameters[ 'ZAxisLower' ] = int( child.text )

        if child.tag == 'ZAxisUpper':
            Parameters[ 'ZAxisUpper' ] = int( child.text )

    return Parameters
