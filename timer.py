#!/usr/bin/python
#WMRanger --> Python Script for changing mac address on linux systems
#By Seekersoft
#requires python2.7
from time import sleep
from color import *

#timer 
def timer(args):
        
        from changer import *
        
        if args == 't':
                
                time = float(raw_input(color.Blue+"Required time(in mins): ")) * 60
                
                sysBurnMac()
                
                while True:
                
                        print(color.Blue+"\nWaiting for time expiration...\n")
                        sleep(time)
                        print(color.Red+"\tTime Expired...\n"+color.Blue+"\nChanging Mac Now...\n")
                        sleep(1) 
                        sysBurnMac()

        elif args == 'br':

                macaddr = str(raw_input('Mac octals > '))
                sysWriteMacRange(macaddr)
                time = float(raw_input(color.Blue+"\nRequired time(in mins): ")) * 60
                
                
                while True:
                
                        print(color.Blue+"\nWaiting for time expiration...\n")
                        sleep(time)
                        print(color.Red+"\tTime Expired...\n"+color.Blue+"\nChanging Mac Now...\n")
                        sleep(1) 
                        sysWriteMacRange(macaddr)
        else:
                print(color.Blue+". . .")