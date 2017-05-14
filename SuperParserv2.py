import os
import re
import sys
import matplotlib.pyplot as plt
import numpy as np

ssidList = []
weplist = []
wpalist = []
openlist = []
encypType = []
tempVar = "Open"
WEP = 0
WPA = 0
ocount = 0

oldstdout = sys.stdout

file = open('output.txt', 'r')
sys.stdout = open("finalout.tsv", "w")
print "SSID", "\t", "auth"
ssidREGEX = re.compile("\s*'wlan_mgt.ssid': '(.*)',")
encryREGEX = re.compile("\s*'wlan_mgt.rsn.akms.list': '(.*)',")
for line in file:
	#for ssid
	m = re.match(ssidREGEX, line);
	if m:
		if m.group(1) not in ssidList:
			ssidList.append(m.group(1))
			if "PSK" in tempVar:
				tempVar="WEP"
				weplist.append(m.group(1))
				WEP+=1
			elif "WPA" in tempVar:
				tempVar="WPA"
				wpalist.append(m.group(1))
				WPA+=1
			else:
				ocount+=1
				openlist.append(m.group(1))			
			encypType.append(tempVar)
			tempVar = "Open"
		#print(m.group(1))

						

	#for encrypttype
	m = re.match(encryREGEX, line);
	if m:
		#put in temp
		tempVar = m.group(1)

for i,j in zip(ssidList,encypType):
	print i,"\t", j
sys.stdout = open("counts.tsv", "w")
print "auth", "\t", "count"
print "WEP", "\t", WEP
print "WPA", "\t", WPA
print "Open", "\t", ocount
sys.stdout = oldstdout

print "WEP SSIDs"
for i in zip(weplist):
	print i
print "WPA SSIDs"
for i in zip(wpalist):
	print i
print "Open SSIDs"
for i in zip(openlist):
	print i



# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = np.genfromtxt('counts.tsv',delimiter='\t', names['name','count'])

labels = 'WEP', 'WPA', 'Open'
sizes = [WEP, WPA, ocount]
explode = (0, 0, 0.1,)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()



