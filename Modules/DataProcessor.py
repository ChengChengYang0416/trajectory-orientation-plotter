from scipy.spatial.transform import Rotation as R

class CDataProcessor:
	def GetSampledPositionAndOrientation( self, Pose, SamplingInterval ):
		# dictionary of sampled position and orientation
		SampledPose = { 'X' : [], 'Y' : [], 'Z' : [], 'A' : [], 'B' : [], 'C' : [], 'OrientationXX' : [], 'OrientationXY' : [], 'OrientationXZ' : [], 'OrientationYX' : [], 'OrientationYY' : [], 'OrientationYZ' : [], 'OrientationZX' : [], 'OrientationZY' : [], 'OrientationZZ' : [], 'Time' : [] }

		# get sampled position and orientation
		for i in range( 0, len( Pose[ 0 ] ), SamplingInterval ):
			# get position
			SampledPose[ 'X' ].append( Pose[ 0 ][ i ] )
			SampledPose[ 'Y' ].append( Pose[ 1 ][ i ] )
			SampledPose[ 'Z' ].append( Pose[ 2 ][ i ] )

			# get orientation by ABC
			SampledPose[ 'A' ].append( Pose[ 3 ][ i ] )
			SampledPose[ 'B' ].append( Pose[ 4 ][ i ] )
			SampledPose[ 'C' ].append( Pose[ 5 ][ i ] )

			# get orientation by rotation matrix
			r = R.from_euler( 'zyx', [ Pose[ 5 ][ i ], Pose[ 4 ][ i ], Pose[ 3 ][ i ] ], degrees = True )
			SampledPose[ 'OrientationXX' ].append( r.as_matrix()[ 0 ][ 0 ] )
			SampledPose[ 'OrientationXY' ].append( r.as_matrix()[ 1 ][ 0 ] )
			SampledPose[ 'OrientationXZ' ].append( r.as_matrix()[ 2 ][ 0 ] )
			SampledPose[ 'OrientationYX' ].append( r.as_matrix()[ 0 ][ 1 ] )
			SampledPose[ 'OrientationYY' ].append( r.as_matrix()[ 1 ][ 1 ] )
			SampledPose[ 'OrientationYZ' ].append( r.as_matrix()[ 2 ][ 1 ] )
			SampledPose[ 'OrientationZX' ].append( r.as_matrix()[ 0 ][ 2 ] )
			SampledPose[ 'OrientationZY' ].append( r.as_matrix()[ 1 ][ 2 ] )
			SampledPose[ 'OrientationZZ' ].append( r.as_matrix()[ 2 ][ 2 ] )

			# produce time list
			SampledPose[ 'Time' ].append( i * 0.01 )

		return SampledPose

	def GetSampledXYZABCStates( self, Pose, SamplingInterval ):
		# dictionary of sampled position and orientation
		SampledPose = { 'X' : [], 'Y' : [], 'Z' : [], 'A' : [], 'B' : [], 'C' : [], 'Time' : [] }

		# get sampled position and orientation
		for i in range( 0, len( Pose[ 0 ] ), SamplingInterval ):
			# get XYZABC states
			SampledPose[ 'X' ].append( Pose[ 0 ][ i ] )
			SampledPose[ 'Y' ].append( Pose[ 1 ][ i ] )
			SampledPose[ 'Z' ].append( Pose[ 2 ][ i ] )
			SampledPose[ 'A' ].append( Pose[ 3 ][ i ] )
			SampledPose[ 'B' ].append( Pose[ 4 ][ i ] )
			SampledPose[ 'C' ].append( Pose[ 5 ][ i ] )

			# produce time list
			SampledPose[ 'Time' ].append( i * 0.01 )

		return SampledPose

	def GetSampledJointStates( self, Pose, SamplingInterval ):
		# dictionary of sampled joint states
		SampledPose = { 'Joint1' : [], 'Joint2' : [], 'Joint3' : [], 'Joint4' : [], 'Joint5' : [], 'Joint6' : [], 'Time' : [] }

		# get sampled joint states
		for i in range( 0, len( Pose[ 0 ] ), SamplingInterval ):
			# get joint states
			SampledPose[ 'Joint1' ].append( Pose[ 0 ][ i ] )
			SampledPose[ 'Joint2' ].append( Pose[ 1 ][ i ] )
			SampledPose[ 'Joint3' ].append( Pose[ 2 ][ i ] )
			SampledPose[ 'Joint4' ].append( Pose[ 3 ][ i ] )
			SampledPose[ 'Joint5' ].append( Pose[ 4 ][ i ] )
			SampledPose[ 'Joint6' ].append( Pose[ 5 ][ i ] )

			# produce time list
			SampledPose[ 'Time' ].append( i * 0.01 )

		return SampledPose
