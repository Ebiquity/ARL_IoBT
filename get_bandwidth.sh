#!/bin/bash

# uses vnstat to measure bandwidth on a given interface and 
# records measurements in a tmp file 
#
# writes bandwidth values to the top of a csv file 

# get current timestamp
timestamp() {
    date +"%Y-%m-%d_%H:%M:%S"
}

# update csv file
write_csv() {
    file_name="output.csv"
    if [ -f "$file_name" ]
    then
	sed -i '1 a '$(timestamp)','$2','$1 $file_name
    else
	touch $file_name
	echo 'TemporalEntity,BandwidthAttack,Result'"$(cat $file_name)" > $file_name
	sed -i '1 a '$(timestamp)','$2','$1 $file_name
    fi
}

# get bandwidth stats
main() {
	# define interface vars 
	i=0
	interface='eth0'

	vnstat -tr -i $interface > /tmp/monitor

	# is this needed???
	# switch to rx to get download bandwidth, tx for upload 
	bw=`cat /tmp/monitor | grep rx | grep -v kbit | awk '{print $2}' | cut -d . -f1`
	bwx=$(($bw + $i))

	# get attack stage based on bandwidth 
	if [ $bwx -ge 100 ] && [ $bwx -le 200 ]
	then
	    ba='Stage1BA'
	elif [ $bwx -ge 51 ] && [ $bwx -le 99 ]
	then
	    ba='Stage2BA'
	elif [ $bwx -ge 0 ] && [ $bwx -le 50 ]
	then
	    ba='Stage3BA'
	fi
    
	# write output file
	write_csv "$bwx" "$ba"
}

main








