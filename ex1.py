import sys
import cv2
import time

t0 =time.time()

def read_cam():
    #cap = cv2.VideoCapture("v4l2src num-buffers=300 ! video/x-raw,format=UYVY,width=1280,height=720,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink  ")
    #cap = cv2.VideoCapture("videotestsrc is-live=1 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink ")
    t0 =time.time()
    cap = cv2.VideoCapture("v4l2src device=/dev/video6 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink")
    #cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, "  "height=720, framerate=30/1, format=NV12 ! nvvidconv ! "
                                       #"video/x-raw, format=BGRx, width=640, height=360 ! "
                                       #"videoconvert ! video/x-raw, format=BGR ! appsink "
                                       #"wait-on-eos=false drop=true max-buffers=60 -e -vvv")

    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('Src opened, %dx%d @ %d fps' % (w, h, fps))
    
    gst_out = "appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw,format=BGR ! nvvidconv ! nvv4l2h264enc ! h264parse ! matroskamux ! filesink location=test.mkv "
    out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, float(fps), (int(w), int(h)))
    
    if not out.isOpened():
        print("Failed to open output")
        exit()

    if cap.isOpened():
        while True:
            ret_val, img = cap.read();
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    out.write(gray)
            t1 =time.time()
            num_seconds = t1-t0
            if num_seconds > 30:
                 break;
            if not ret_val:
                break;
            out.write(img);
            cv2.waitKey(30)
    else:
     print "pipeline open failed"

    print("successfully exit")
    cap.release()
    out.release()


if __name__ == '__main__':
    read_cam()



#matroskamux
