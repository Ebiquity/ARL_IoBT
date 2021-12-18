# importing the module
import cv2
import jetson.utils

	# reading the video
        
source = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink")
       # We need to set resolutions.
       # so, convert them from float to integer.
frame_width = int(source.get(3))
frame_height = int(source.get(4))
   
size = (frame_width, frame_height)
result = cv2.VideoWriter('test1.mp4',0x7634706d,20.0, size, 0)
        # running the loop
while True:

	# extracting the frames
	ret, img = source.read()
	
	# converting to gray-scale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# displaying the video
	
	result.write(gray)

	# exiting the loop
	key = cv2.waitKey(1)
	if key == ord("q"):
		break


	
# closing the window
cv2.destroyAllWindows()
source.release()




