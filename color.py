import jetson.utils
import argparse
import sys
import time


# create video sources & outputs
t0 = time.time()
input = jetson.utils.videoSource("/dev/video0", ["--input-width=1000"])
#output = jetson.utils.videoOutput('test18.mp4')
output = jetson.utils.videoOutput('rtp://10.42.0.39:1234')

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







