#!/usr/bin/python
#WMRanger --> Python Script for changing mac address on linux systems
#By Seekersoft
#requires python2.7
import os
import sys 
from changer import *
from timer import *
from color import * 

if sys.platform == 'win32':
    print(color.Red + "Sorry you are not compatible")
else:
    os.system("clear")
    print(color.Blue + "\n/* Welcome to WMRanger\n\tBy Seekersoft */\n")
    

    writeMac = '' 

    # parse the command-line arguments, set global variables
    def parse(args):
        global writeMac
        
        i = 0
        while i < len(args):
            # charsets args
            if args[i] == '-b':
                sysBurnMac()
            elif args[i] == '-m':
                sysWriteMac()
            elif args[i] == '-t':
                timer('t')
            elif args[i] == '-br':
                timer('br')

            # help args
            elif args[i] == '-h':
                help()
                sys.exit(0)
            i += 1
        if len(args) == 0:
            help()
            exit(1) 

    #help
    def help():
        print(color.Blue + '''
    
        \t[+]Welcome to WMRanger[+]\n\t\t\t\t[+]By Seekersoft[+]\n
            Usage:                                                              
            WMRanger.py -b  --> [Pretend to be a burned in address]              
            WMRanger.py -m XX:XX:XX:XX:XX:XX --> [Write your own MAC XX:XX:XX:XX:XX:XX] 
            WMRanger.py -t time [Specify the time in minutes for changing the Mac]
            WMRanger.py -br [Specify the first three octals of the random mac]
            WMRanger.py -h --> [for the help menu]                               
                                                                                
            Note: You have to be logged in as root            
            Shutdown: Press Ctrl+c                    
            ''')

    #main
    def main():
        parse(sys.argv[1:])

    main()