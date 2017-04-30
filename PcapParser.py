#!/usr/bin/python
#must have tshark installed!
import os
import pyshark
import sys
from pprint import pprint

cap = pyshark.FileCapture('/home/noel/Desktop/pcap/fu.pcap')
sys.stdout = open("output.txt","w")
count=0
while(count<800):
	try:
		pprint(vars(cap[count].wlan_mgt)) 
	except AttributeError as e:
		pass
	count+=1


