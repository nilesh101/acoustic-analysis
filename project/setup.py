import sys
import os
#if python version < 3.0
if sys.version_info < (3,0) : 
	os.system("sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy  python-sklearn libav-tools python-matplotlib \
                     libatlas-dev libatlas3gf-base")
	os.system("sudo pip install eyed3")
	os.system("sudo apt-get install libgs-dev")
	os.system("sudo pip install sklearn")
	os.system("sudo pip install scikits.talkbox")
#if python version > 3.0	
else :
	os.system("sudo apt-get install build-essential python3-dev python3-setuptools \
                     python3-numpy python3-scipy  libav-tools python-matplotlib \
                     libatlas-dev libatlas3gf-base")
	os.system("sudo pip install eyed3")
	os.system("sudo apt-get install libgs-dev")
	os.system("sudo pip install sklearn")
	os.system("sudo pip install scikits.talkbox")
		
	
