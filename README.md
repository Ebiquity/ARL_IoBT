# ARL_IoBT

# Jetson setup 

Follow the directions [here](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) to 
build the jetson-inference repository used in the following code  

vnStat is a console based network monitor that can be used to determine bandwidth. Run `sudo apt install vnstat` 
and [click here](https://www.cyberciti.biz/faq/ubuntu-install-vnstat-console-network-traffic-monitor/) for more information
about how to use the service. 

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

dependencies: 
```
apt-get -y install python3-pip
apt-get install 
```
run `python3 main.py` on the machine transmitting the video stream 
