from scipy.spatial.transform import Rotation as R

def GetSampledPositionAndOrientation( Pose, SamplingInterval ):
    # dictionary of sampled position and orientation
    SampledPose = { 'X' : [], 'Y' : [], 'Z' : [], 'OrientationXX' : [], 'OrientationXY' : [], 'OrientationXZ' : [], 'OrientationYX' : [], 'OrientationYY' : [], 'OrientationYZ' : [], 'OrientationZX' : [], 'OrientationZY' : [], 'OrientationZZ' : [] }

    # get sampled position and orientation
    for i in range( 0, len( Pose[ 0 ] ), SamplingInterval ):
        # get position
        SampledPose[ 'X' ].append( Pose[ 0 ][ i ] )
        SampledPose[ 'Y' ].append( Pose[ 1 ][ i ] )
        SampledPose[ 'Z' ].append( Pose[ 2 ][ i ] )

        # get orientation by rotation matrix
        r = R.from_euler( 'zyx', [ Pose[ 3 ][ i ], Pose[ 4 ][ i ], Pose[ 5 ][ i ] ], degrees = True )
        SampledPose[ 'OrientationXX' ].append( r.as_matrix()[ 0 ][ 0 ] )
        SampledPose[ 'OrientationXY' ].append( r.as_matrix()[ 1 ][ 0 ] )
        SampledPose[ 'OrientationXZ' ].append( r.as_matrix()[ 2 ][ 0 ] )
        SampledPose[ 'OrientationYX' ].append( r.as_matrix()[ 0 ][ 1 ] )
        SampledPose[ 'OrientationYY' ].append( r.as_matrix()[ 1 ][ 1 ] )
        SampledPose[ 'OrientationYZ' ].append( r.as_matrix()[ 2 ][ 1 ] )
        SampledPose[ 'OrientationZX' ].append( r.as_matrix()[ 0 ][ 2 ] )
        SampledPose[ 'OrientationZY' ].append( r.as_matrix()[ 1 ][ 2 ] )
        SampledPose[ 'OrientationZZ' ].append( r.as_matrix()[ 2 ][ 2 ] )

    return SampledPose