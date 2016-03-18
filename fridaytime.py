import subprocess
import select
import os
import time
import sys
audiofile = 'beep.wav'
t = 600
while t:
	os.system('cls' if os.name == 'nt' else 'clear')
	print 'Counting down 10mins'
	if sys.stdin in select.select([sys.stdin],[],[],0)[0]:
		line = raw_input()
		break
	mins, secs = divmod(t, 60)
	timeformat = '{:02d}:{:02d}'.format(mins, secs)
	#if timeformat == '09:50':
	
	#        print(timeformat,end='\r')
	print(timeformat)
	time.sleep(1)
	t -= 1
	print('Time up!')
	#sys.stdout.write('\a')
	#sys.stdout.flush()
	#    return_code = subprocess.call(["afplay",audiofile])
return_code = subprocess.call(["afplay",audiofile])
