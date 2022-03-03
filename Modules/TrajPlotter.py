import matplotlib.pyplot as plt

class CTrajPlotter:
	def PlotTrajectory( self, Pose, XAxisLower, XAxisUpper, YAxisLower, YAxisUpper, ZAxisLower, ZAxisUpper ):
		# create figure
		Fig3D = plt.figure()
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

		# plot position
		FigPosition, ( AxX, AxY, AxZ ) = plt.subplots( 3, 1 )
		AxX.set_title( "Position" )
		AxX.plot( Pose[ 'Time' ], Pose[ 'X' ] )
		AxX.grid()
		AxX.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxX.set( ylabel = "X (mm)" )
		AxX.yaxis.set_label_coords( -.1, .5 )

		AxY.plot( Pose[ 'Time' ], Pose[ 'Y' ] )
		AxY.grid()
		AxY.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxY.set( ylabel = "Y (mm)" )
		AxY.yaxis.set_label_coords( -.1, .5 )

		AxZ.plot( Pose[ 'Time' ], Pose[ 'Z' ] )
		AxZ.grid()
		AxZ.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxZ.set( ylabel = "Z (mm)", xlabel = "Time (sec)" )
		AxZ.yaxis.set_label_coords( -.1, .5 )

		# plot orientation
		FigOrientation, ( AxA, AxB, AxC ) = plt.subplots( 3, 1 )
		AxA.set_title( "Orientation" )
		AxA.plot( Pose[ 'Time' ], Pose[ 'A' ] )
		AxA.grid()
		AxA.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxA.set( ylabel = "A ($^\circ$)" )
		AxA.yaxis.set_label_coords( -.1, .5 )

		AxB.plot( Pose[ 'Time' ], Pose[ 'B' ] )
		AxB.grid()
		AxB.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxB.set( ylabel = "B ($^\circ$)" )
		AxB.yaxis.set_label_coords( -.1, .5 )

		AxC.plot( Pose[ 'Time' ], Pose[ 'C' ] )
		AxC.grid()
		AxC.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxC.set( ylabel = "C ($^\circ$)", xlabel = "Time (sec)" )
		AxC.yaxis.set_label_coords( -.1, .5 )

		# plot
		plt.show()
