import jetson.utils
import argparse
import sys
import cv2
import time


'''
t0 =time.time()
input1 = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,width=320,height=240,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink")
#frame_width = int(input.get(3))
#frame_height = int(input.get(4))
#size = (frame_width, frame_height)
result = cv2.VideoWriter('test56.mp4',0x7634706d,20.0, (640,480), 0)
'''
t0 = time.time()
input = jetson.utils.videoSource("/dev/video0", ["--input-width=1000"])
#output = jetson.utils.videoOutput('test18.mp4')
result = jetson.utils.videoOutput('rtp://10.42.0.39:1234')

while(True):
      
      # Capture the video frame
    # by frame
		ret, frame = input1.read()
# converting to gray-scale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Live", gray)
		result.write(gray)
		t1 =time.time()
		num_seconds = t1-t0
		if num_seconds > 30:
			break;
    # exiting the loop
key = cv2.waitKey(30)  
# After the loop release the cap object
      #
# Destroy all the windows
cv2.destroyAllWindows()
input1.release()






