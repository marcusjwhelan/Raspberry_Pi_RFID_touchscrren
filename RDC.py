"""
    Written By Marcus Whelan for Senior 1 project 2
    This file work with reading the RFID and with
    the time checking and variable holdting for the
    Gui to process the data the correct way.
"""

import subprocess
import inspect
import time
import signal
import datetime
import os
import XL
from easyprocess import EasyProcess
import sys
import logging
from PIL import Image

def getImage(path):
    img = Image.open(path)
    return img
inc = False
ison = False

def snap():
    os.popen("sudo python /home/pi/Senior1/cam.py")
    return
def buz():
    os.popen("sudo python /home/pi/Senior1/Buzzer.py")
    return
def buz2():
    os.popen("sudo python /home/pi/Senior1/Buzzer2.py")
    return
def Button():
    os.popen("sudo python /home/pi/Senior1/Button.py")
    return
def readCard():
    ext = subprocess.Popen('/home/pi/libnfc/libnfc-1.7.1/examples/nfc-poll',stdout=subprocess.PIPE).communicate()[0]
    ext = ext
    temp = ext[281:283]+ext[285:287]+ext[289:291]+ext[293:295]
    return temp
def setison(param):
    global ison
    ison = param
    return
def getison():
    global ison
    ison1 = ison
    return ison1
def setinc(param):
    global inc
    inc = param
    return
def getinc():
    global inc
    inc1 = inc
    return inc1
def formatC(ext):
    temp = ext[281:283]+ext[285:287]+ext[289:291]+ext[293:295]
    return temp
def readC():
    lis = []
    while(True):
        ext = EasyProcess('/home/pi/libnfc/libnfc-1.7.1/examples/nfc-poll').call(timeout=5).stdout
        if(ext):
            temp = ext[281:283]+ext[285:287]+ext[289:291]+ext[293:295]
            lis.append(temp)
            buz()
        else:
            print "nothing read"
        print lis
# get datetime current second
def getS():
    second = datetime.datetime.now().second
    return second
# get datetime current minute
def getDM():
    minute = datetime.datetime.now().minute
    return minute
# get datetime current hour
def getDH():
    hour = datetime.datetime.now().hour
    return hour
# get hours from minutes
def getHfromM(M):
    hour = M/60
    return hour
# get remainder of min from min/60 division
def getRemHfromM(M):
    minutesleft = M%60
    return minutesleft
# make a datetime of minutes
def setTM(M):
    minutes = datetime.timedelta(minutes=M)
    return minutes
# make a datetime of hours
def setTH(H):
    hours = datetime.timedelta(hours=H)
    return hours
# make a datetime of hours and minutes
def setT(H,M):
    time = datetime.timedelta(hours=H,minutes=M)
    return time
# get current time
def getCT():
    currentM = getDM()
    currentH = getDH()
    currentT = setT(currentH,currentM)
    return currentT
# get this classN class time
def getClassT():
    classM = int(XL.getM())
    classH = int(XL.getH())
    classTime = setT(classH,classM)
    return classTime
# returns the time that the class will end
def getEOC():
    classTime = getClassT()
    currentTime = getCT()
    classEnd = currentTime+classTime
    return classEnd






