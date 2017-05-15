import os
import re
import sys
import matplotlib.pyplot as plt
import numpy as np

#array names
ssidList = []
weplist = []
wpalist = []
openlist = []
encypType = []
barCount = []
tempVar = "Open"
WEP = 0
WPA = 0
ocount = 0

oldstdout = sys.stdout
#opening files and setting regex
file = open('output.txt', 'r')
sys.stdout = open("finalout.tsv", "w")
print "SSID", "\t", "auth"
ssidREGEX = re.compile("\s*'wlan_mgt.ssid': '(.*)',")
encryREGEX = re.compile("\s*'wlan_mgt.rsn.akms.list': '(.*)',")

#reading the file
for line in file:
	#for ssid
	m = re.match(ssidREGEX, line);
	if m:
		#grabbing unique ssids
		if m.group(1) not in ssidList:
			ssidList.append(m.group(1))
			#creating diffrent groups 
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

	#for encrypttype
	m = re.match(encryREGEX, line);
	if m:
		#put in temp
		tempVar = m.group(1)


sys.stdout=oldstdout
#counting tims ssid's appeared 
for a in ssidList:
	barCount.append(open('output.txt', 'r').read().count(a))

#creating bar graph
print barCount
f = plt.figure(1)
objects = ssidList
y_pos = np.arange(len(objects))
performance = barCount

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming language usage')

f.show()

#creating list in terminal here
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




#creating pie graph
labels = 'WEP', 'WPA', 'Open'
sizes = [WEP, WPA, ocount]
explode = (0, 0, 0.1,) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  

plt.show()

raw_input()



