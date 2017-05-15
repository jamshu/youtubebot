import webbrowser
import time
import os

print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : Jamshid      ##'
print '\t\t\t ######################################'





def OpenUrl():
	print("Successfully Viwed. ")
	os.system(" killall -9 " + 'chrome')
	webbrowser.open('https://www.youtube.com/watch?v=YyvEDDVPJbw')
	time.sleep(int(refresh))

for i in range(50):
	OpenUrl()
