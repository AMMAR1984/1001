import os 
os.system("clear")
Black="\[\033[0;30m\]" # Black
Red="\[\033[0;31m\]" # Red
Green="\[\033[0;32m\]" # Green
Yellow="\[\033[0;33m\]" # Yellow
Blue="\[\033[0;34m\]" # Blue
Purple="\[\033[0;35m\]" # Purple
#################################

def daysofpython ():

    print ("\033[0;31m ___ \033[0;32m  _____   _____  \033[0;31m  ___ ")
    print ("\033[0;31m|_  |\033[0;32m /  _  \ /  _  \ \033[0;31m |_  |")
    print ("\033[0;31m  | |\033[0;32m | | | | | | | | \033[0;31m   | |")
    print ("\033[0;31m  | |\033[0;32m | |/| | | |/| | \033[0;31m   | |")
    print ("\033[0;31m  | |\033[0;32m | |_| | | |_| | \033[0;31m   | |")
    print ("\033[0;31m  |_|\033[0;32m \_____/ \_____/ \033[0;31m   |_|")

    print ("\033[0;33m groupe \033[0;34m#100daysofpython \033[0;33m^_^")
    print ("😷😷\033[0;35mcovid19😷😷be careful🥵🤧           \033[0;33mby Ammar")
daysofpython ()
print ("")
print ("")
import pafy

print ("*"*40)
url=input(" enter the video link you like to download:")
print ("*"*40)
aw= pafy.new (str(url ))
print ("*")
print ("*")
print ("*"*68)
print ("To download the video image and voice Press Number:==> 1 ")
print ("*"*68)
print ("*")
print ("*")
print ("*"*68)
print (" To download Audio Video Just click Number:===========> 2")
print ("*"*68)
print ("*")
print ("*")
print ("*"*68)
print (" To download the video without sound Press number:====> 3")
print ("*"*68)
hhh=input (" Place the number of your choice please :")
def ammar():
    print ("*"*444)
    az=aw.streams
    for x in az:
        print ("===>", x)
    print ("*"*444)
    jojo=input( "Choose number to download please:")
    taj= aw.streams[int(jojo)]
    taj.download("/sdcard/Download")

def ammar1():
    print ("*"*444)
    az1=aw.audiostreams
    for n in az1:
        print ("===>",n)
    print ("*"*444)
    jojo1=input( "Choose number to download please:")
    taj1= aw.audiostreams[int(jojo1)]
    taj1.download("/sdcard/Download")

def ammar2():
    print ("*"*444)
    az2=aw.videostreams
    for g in az2:
        print ("===>",g)
    print ("*"*444)
    jojo2=input( "Choose number to download please:")
    taj2= aw.videostreams[int(jojo2)]
    taj2.download("/sdcard/Download")
if(int(hhh)==1):
    ammar()
elif (int(hhh)==2):
    ammar1()

elif (int(hhh)==3):
    ammar2()
else :
    print (" Sorry your choice is incorrect")
