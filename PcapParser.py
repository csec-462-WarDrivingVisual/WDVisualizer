#!/usr/bin/python
#must have tshark installed!
import os
import pyshark
import sys
from pprint import pprint



var = raw_input("Please enter the directory of the pcap: ")
cap = pyshark.FileCapture(var)
sys.stdout = open("output.txt","w")
count=0
while(count<800):
	try:
		pprint(vars(cap[count].wlan_mgt)) 
	except AttributeError as e:
		pass
	count+=1


