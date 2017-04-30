#!/bin/bash

bigStuff=$(cat output.txt)
compareThis="raw_mode"


while read line
do
		
	#grep raw_mode
	if [[ ${line} = * 'raw_mode': False}* ]]; then
		echo "boo"
	fi
done < output.txt

#>> akms_list.txt
#list=$(grep -c wlan_mgt.rsn.akms.list output.txt)
#echo $list
#ssid=$(grep -c wlan_mgt.ssid output.txt)
#echo $ssid
#cat output.txt | grep wlan_mgt.ssid | sort | uniq >> ssid.txt
#for i in `cat output.txt`; do
#	echo ${i} #| grep --after-context=5 --before-context=10 'wlan_mgt.rsn.akms.list'
#| awk -F '\t ' '{print $2}'
#	done
#wait
