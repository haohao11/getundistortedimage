'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
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
    if slot < 10:
        name = './HA_2/0000' + str(slot) + '.jpg'
    elif slot < 100 and slot >= 10:
        name = './HA_2/000' + str(slot) + '.jpg'
    elif slot < 1000 and slot >= 100:
        name = './HA_2/00' + str(slot) + '.jpg'
    elif slot < 10000 and slot >= 1000:
        name = './HA_2/0' + str(slot) + '.jpg'
    #cv2.imwrite(name, image) # save frame as JPEG file
    currentFrame = currentFrame + 1
    if currentFrame%15 == 0:
        #cv2.imwrite(name, image)
        slot = slot + 1
        if slot >= 0:
            #img_undistorted = cv2.fisheye.undistortImage(image, K, D=D, Knew=Knew)            
            #cv2.imwrite(name, img_undistorted)
            #cv2.imwrite(name, image)
            cv2.imwrite(os.path.join(data_dir, "%05d.jpg" % slot), image)             
    if currentFrame >= 150000:
        break     
    
# When everything done, release the capture
vidcap.release()
cv2.destroyAllWindows()