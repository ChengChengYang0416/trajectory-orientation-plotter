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

		# plot
		plt.show()

	def Plot2DStates( self, Pose ):
		# plot joint states
		FigJointStates, ( AxJoint1, AxJoint2, AxJoint3, AxJoint4, AxJoint5, AxJoint6 ) = plt.subplots( 6, 1 )
		FigJointStates.set_figwidth( 8 )
		FigJointStates.set_figheight( 6 )

		AxJoint1.set_title( "Joint States" )
		AxJoint1.plot( Pose[ 'Time' ], Pose[ 'Joint1' ] )
		AxJoint1.grid()
		AxJoint1.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint1.set( ylabel = "Joint1 ($^\circ$)" )
		AxJoint1.yaxis.set_label_coords( -.1, .5 )
		AxJoint1.axes.xaxis.set_ticklabels( [] )

		AxJoint2.plot( Pose[ 'Time' ], Pose[ 'Joint2' ] )
		AxJoint2.grid()
		AxJoint2.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint2.set( ylabel = "Joint2 ($^\circ$)" )
		AxJoint2.yaxis.set_label_coords( -.1, .5 )
		AxJoint2.axes.xaxis.set_ticklabels( [] )

		AxJoint3.plot( Pose[ 'Time' ], Pose[ 'Joint3' ] )
		AxJoint3.grid()
		AxJoint3.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint3.set( ylabel = "Joint3 ($^\circ$)" )
		AxJoint3.yaxis.set_label_coords( -.1, .5 )
		AxJoint3.axes.xaxis.set_ticklabels( [] )

		AxJoint4.plot( Pose[ 'Time' ], Pose[ 'Joint4' ] )
		AxJoint4.grid()
		AxJoint4.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint4.set( ylabel = "Joint4 ($^\circ$)" )
		AxJoint4.yaxis.set_label_coords( -.1, .5 )
		AxJoint4.axes.xaxis.set_ticklabels( [] )

		AxJoint5.plot( Pose[ 'Time' ], Pose[ 'Joint5' ] )
		AxJoint5.grid()
		AxJoint5.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint5.set( ylabel = "Joint5 ($^\circ$)" )
		AxJoint5.yaxis.set_label_coords( -.1, .5 )
		AxJoint5.axes.xaxis.set_ticklabels( [] )

		AxJoint6.plot( Pose[ 'Time' ], Pose[ 'Joint6' ] )
		AxJoint6.grid()
		AxJoint6.set_xlim( [ 0, Pose[ 'Time' ][ -1 ] ] )
		AxJoint6.set( ylabel = "Joint6 ($^\circ$)", xlabel = "Time (sec)" )
		AxJoint6.yaxis.set_label_coords( -.1, .5 )

		# plot
		plt.show()

	def PlotXYZABCStates( self, Pose ):
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
