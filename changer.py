#!/usr/bin/python
#WMRanger --> Python Script for changing mac address on linux systems
#By Seekersoft
#requires python2.7
import os, sys
from gen import * 
from timer import *
from color import *


#sys generated mac(-b)
def sysBurnMac():
    
    os.system("iw dev | awk 'NR == 2' >> Chmac.txt")
    
    file = open("Chmac.txt")
    
    target = file.read()
    
    interface = target.split()[1]
    
    mac = str(generateBurnedMac()).lower()
    
    while (len(mac) <> 17):
    
        mac = str(generateBurnedMac()).lower()
    
    sysChanger(mac, interface)

 
#write your own mac(-w)
def sysWriteMac():
        
        writeMac = str(raw_input('Mac > '))
        
        while(len(writeMac) <> 17):
        
            print(color.Red+"Mac not Complete . . ."+color.Blue+"\nTry again . . .")
        
            writeMac = str(raw_input('Mac > '))
        
        mac = str(writeMac).lower()
        
        os.system("iw dev | awk 'NR == 2' >> Chmac.txt")
        
        file = open("Chmac.txt")
        
        target = file.read()
        
        interface = target.split()[1]
        
        sysChanger(mac, interface)

#specify the first three cols of the sys generated mac
def sysWriteMacRange(macaddr):

    while(len(macaddr) <> 8):

        print(color.Red+"Mac octals not Complete . . ."+color.Blue+"\nTry again . . .")

        macaddr = str(raw_input('Mac octals > '))
    
    
    for i in range(0,3):

        if macaddr == "":

            macaddr = generateRandom()

        else:

            while(len(macaddr) <> 17):

                macaddr += ":"+generateRandom()    
    
    mac = str(macaddr).lower()

    os.system("iw dev | awk 'NR == 2' >> Chmac.txt")
    
    file = open("Chmac.txt")
    
    target = file.read()
    
    interface = target.split()[1]
    
    sysChanger(mac, interface)

#changer
def sysChanger(mac, interface):
    
    print(color.Green+"Your New MAC is " + mac)
    
    wFaceDown = "sudo ip link set " + interface + " down"
    
    wFaceUp = "sudo ip link set " + interface + " up"
    
    os.system(wFaceDown)
    
    setAddr = "sudo ip link set " + interface + " address " + mac
    
    os.system(setAddr)
    
    os.system(wFaceUp)
    
    os.system("rm Chmac.txt")