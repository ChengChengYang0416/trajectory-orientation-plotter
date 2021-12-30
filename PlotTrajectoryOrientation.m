close all;
scale = 10;

% read parameters of plot from xml
Data = xml2struct( 'Parameters.xml' );
FilePath = Data.Children( 2 ).Children.Data;
UnitConvert = str2double( Data.Children( 4 ).Children.Data );
SamplingInterval = str2double( Data.Children( 6 ).Children.Data );
XAxisLower = str2double( Data.Children( 8 ).Children.Data );
XAxisUpper = str2double( Data.Children( 10 ).Children.Data );
YAxisLower = str2double( Data.Children( 12 ).Children.Data );
YAxisUpper = str2double( Data.Children( 14 ).Children.Data );
ZAxisLower = str2double( Data.Children( 16 ).Children.Data );
ZAxisUpper = str2double( Data.Children( 18 ).Children.Data );

% load the data from text file
Pose = importdata( FilePath );

% convert the unit from BLU to mm
Pose = Pose / UnitConvert;
Pose( :, 4:6 ) = deg2rad( Pose( :, 4:6 ) );
LengthOfPose = length( Pose( :, 1 ) );

% plot orientation
figure(1)
for i = 1 : SamplingInterval : LengthOfPose
    % get orientation
    Rx = [ 1,                   0,                    0;
           0, cos( Pose( i, 4 ) ), -sin( Pose( i, 4 ) );
           0, sin( Pose( i, 4 ) ),  cos( Pose( i, 4 ) ) ];
       
    Ry = [  cos( Pose( i, 5 ) ), 0, sin( Pose( i, 5 ) );
                              0, 1,                   0;
           -sin( Pose( i, 5 ) ), 0, cos( Pose( i, 5 ) ) ];
       
    Rz = [ cos( Pose( i, 6 ) ), -sin( Pose( i, 6 ) ), 0;
           sin( Pose( i, 6 ) ),  cos( Pose( i, 6 ) ), 0;
                             0,                    0, 1 ];
       
    R = Rx*Ry*Rz;
    
    % plot x axis
    quiver3( Pose( i, 1 ), Pose( i, 2 ), Pose( i, 3 ), scale * R( 1, 1 ), scale * R( 2, 1 ), scale * R( 3, 1 ), 'Color', 'r' )
    hold on
    
    % plot y axis
    quiver3( Pose( i, 1 ), Pose( i, 2 ), Pose( i, 3 ), scale * R( 1, 2 ), scale * R( 2, 2 ), scale * R( 3, 2 ), 'Color', 'g' )
    hold on
    
    % plot z axis
    quiver3( Pose( i, 1 ), Pose( i, 2 ), Pose( i, 3 ), scale * R( 1, 3 ), scale * R( 2, 3 ), scale * R( 3, 3 ), 'Color', 'b' )
    hold on
end

% set the boundary
xlim( [ XAxisLower, XAxisUpper ] )
ylim( [ YAxisLower, YAxisUpper ] )
zlim( [ ZAxisLower, ZAxisUpper ] )
