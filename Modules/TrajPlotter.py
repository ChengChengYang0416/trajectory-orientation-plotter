import matplotlib.pyplot as plt

class CTrajPlotter:
	def PlotTrajectory( self, Pose, XAxisLower, XAxisUpper, YAxisLower, YAxisUpper, ZAxisLower, ZAxisUpper ):
		# create figure
		fig = plt.figure()
		ax = plt.axes( projection = '3d' )

		# label of axis
		plt.xlabel( 'X' )
		plt.ylabel( 'Y' )

		# set the boundary
		xlim = [ XAxisLower, XAxisUpper ]
		ylim = [ YAxisLower, YAxisUpper ]
		zlim = [ ZAxisLower, ZAxisUpper ]
		ax.set_xlim3d( xlim )
		ax.set_ylim3d( ylim )
		ax.set_zlim3d( zlim )

		# set the aspect ration of x, y, z to 1:1:1
		ax.set_box_aspect( [ 1, 1, 1 ] )

		# plot the orientation
		ax.quiver( Pose[ 'X' ], Pose[ 'Y' ], Pose[ 'Z' ], Pose[ 'OrientationXX' ], Pose[ 'OrientationXY' ], Pose[ 'OrientationXZ' ], length = 10, normalize = True, color = 'r' )
		ax.quiver( Pose[ 'X' ], Pose[ 'Y' ], Pose[ 'Z' ], Pose[ 'OrientationYX' ], Pose[ 'OrientationYY' ], Pose[ 'OrientationYZ' ], length = 10, normalize = True, color = 'g' )
		ax.quiver( Pose[ 'X' ], Pose[ 'Y' ], Pose[ 'Z' ], Pose[ 'OrientationZX' ], Pose[ 'OrientationZY' ], Pose[ 'OrientationZZ' ], length = 10, normalize = True, color = 'b' )

		# plot
		plt.show()
