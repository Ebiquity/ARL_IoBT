# ARL_IoBT

## get_bandwidth.sh 

run `bash get_bandwidth.sh` 

The **vnstat** command is used to measure either upload or download bandwidth 
and the measurements are then written to the top of `output.csv` 

```
i=0
interface='wlan0' 
```
Update the code above based on interface configurations 

## get_vars.py 

run `python3 get_vars.py` 

The bash file `get_bandwidth.sh` is executed and the generated csv file is read in to create 
class objects with the given values 

## video-viewer_to-stream.py 

run `bash video-viewer_to-stream.py` on the machine recieving the video stream  

## main.py 

run `python3 main.py` on the machine transmitting the video stream 
