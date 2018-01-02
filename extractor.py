'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

'''

import cv2
import numpy as np
import os

print(cv2.__version__)

# Playing video from file:
vidcap = cv2.VideoCapture('HA_2.avi')
currentFrame = 0
slot = 1
vidcap.set(cv2.CAP_PROP_POS_MSEC,2000)

# This is the camera parameters for HA datasets
# camera matrix
K = np.array([[  1410.7395877898227,     0.  ,  1317.4509679240998],
              [    0.  ,   1401.2597462184024,   680.3912106607918],
              [    0.  ,     0.  ,     1.  ]])  
# distortion coefficients
D = np.array([-0.4521215675827466, 0.40599767988190066, 0.009465939972631884, 9.935228282721559E-5]) 

# use Knew to scale the output
Knew = K.copy()
Knew[(0,1), (0,1)] = 1 * Knew[(0,1), (0,1)]   

try:
    if not os.path.exists('HA_2'):
        os.makedirs('HA_2')
except OSError:
    print ('Error: Creating directory of data')

data_dir ='./HA_test'
if not os.path.exists(data_dir):
      os.makedirs(data_dir)

success = True
while success:
    # added this line 
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    # cv2.imwrite(name, image) # save frame as JPEG file
    currentFrame = currentFrame + 1
    # the vedio is 30fps and the time-slot is defined as 0.5 seconds
    if currentFrame%15 == 0:
        # cv2.imwrite(name, image)
        slot = slot + 1
        if slot >= 0:
            img_undistorted = cv2.fisheye.undistortImage(image, K, D=D, Knew=Knew)            
            #cv2.imwrite(name, img_undistorted)
            #cv2.imwrite(name, image)
            cv2.imwrite(os.path.join(data_dir, "%05d.jpg" % slot), img_undistorted)             
    if currentFrame >= 99999:
        break     
    
# When everything done, release the capture
vidcap.release()
cv2.destroyAllWindows()
