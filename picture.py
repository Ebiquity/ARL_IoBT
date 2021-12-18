import jetson.utils
import argparse
import sys
import time


# create video sources & outputs
t0 = time.time()
input = jetson.utils.videoSource('/dev/video1')
#output = jetson.utils.videoOutput('video/test23.mp4')
#output = jetson.utils.videoOutput('t/output_1.jpg')
#a = ('t/output_1.jpg')
output = jetson.utils.videoOutput('t/outputq_1.jpg')
	#input = jetson.utils.videoSource('/dev/video2')
	#output = jetson.utils.videoOutput('pic/output_%i.jpg')


# capture frames until user exits
while output.IsStreaming():
	image = input.Capture(format='rgb8')
	t1 = time.time()
	num_seconds = t1-t0
	if num_seconds >30:
		break 	
	output.Render(image)
	output.SetStatus("Video Viewer | {:d}x{:d} | {:.1f} FPS".format(image.width, image.height, output.GetFrameRate()))

