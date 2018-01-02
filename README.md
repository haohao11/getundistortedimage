# getundistortedimage
## camera data process for trajectory tracking
### 1. Get camera parameters:
  #### Extrinsic parameters: 
  used to transform point in real world coordinate system to camera coordinate system. The parameters consists of rotation matrix and translation vector.
  #### Intrinsic parameters:
  used to transform point in camera coordinate system to image coordinate system.
### 2. Get undistorted image sequence with pre-defined time-slot (0.5 seconds)  
