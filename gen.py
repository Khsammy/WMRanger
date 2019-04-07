#!/usr/bin/python
#WMRanger --> Python Script for changing mac address on linux systems
#By Seekersoft
#requires python2.7
import random 
 
#generators

#generate burned mac
#first 3 cols of mac address vendors 
def generateBurnedMac():

    macAddressdb  = {0:'CC:46:D6', 1:'3C:5A:B4', 2:'3C:D9:2B', 3:'00:9A:CD', 4:'E0:43:DB',
                     5:'24:05:F5', 6:'3C:D9:2B', 7:'2C:22:8B', 8:'B4:99:BA', 9:'1C:C1:DE',
                     10:'3C:35:56', 11:'00:50:BA', 12:'00:17:9A', 13:'1C:BD:B9', 15:'28:10:7B',
                     16:'1C:7E:E5', 17:'C4:A8:1D', 18:'18:62:2C', 19:'7C:03:D8', 20:'E8:F1:B0', 
                     21:'00:F8:71', 22:'20:BB:76', 23:'34:8A:AE', 24:'BC:EC:23', 25:'AC:06:C7',
                     26:'CC:46:D6', 27:'48:AD:08', 28:'2C:AB:00', 29:'00:E0:FC', 30:'24:DF:6A', 
                     32:'00:9A:CD', 33:'38:F2:3E', 34:'58:AC:78', 35:'90:7F:61', 36:'28:BC:18', 
                     37:'80:7A:BF', 38:'40:9F:87', 39:'3C:5A:B4', 40:'00:1A:11', 41:'D8:3C:69',
                     42:'74:AC:5F', 43:'BC:83:A7', 44:'E4:F8:9C', 45:'A4:02:B9', 46:'4C:34:88', 
                     47:'00:0D:0B', 48:'00:24:A5', 49:'DC:FB:02', 50:'F4:CE:46', 51:'00:1C:C4',
                     52:'00:25:B3', 53:'00:0B:CD', 55:'00:0E:7F', 56:'00:0F:20', 57:'00:11:0A', 
                     58:'00:17:A4', 59:'90:E7:C4', 60:'74:A7:8E', 61:'D8:60:B0', 62:'80:38:BC',
                     63:'D4:40:F0', 64:'64:A6:51', 65:'E8:CD:2D', 66:'AC:E2:15', 67:'EC:23:3D', 
                     68:'78:F5:FD', 69:'80:B6:86', 70:'10:C6:1F', 71:'88:53:D4', 72:'0C:37:DC', 
                     73:'BC:76:70', 74:'24:DB:AC', 75:'00:07:D8', 76:'84:74:2A', 77:'68:1A:B2',
                     78:'E0:05:C5', 79:'A0:F3:C1', 80:'8C:21:0A', 81:'EC:17:2F', 82:'EC:88:8F', 
                     83:'14:CF:92', 84:'64:56:01', 85:'14:CC:20', 86:'BC:46:99', 87:'0C:45:BA', 
                     88:'84:77:78', 89:'04:53:D5', 89:'CC:A2:23', 90:'E8:08:8B', 91:'60:E7:01',
                     92:'C4:34:6B', 93:'8C:DC:D4', 94:'34:64:A9', 95:'D4:C9:EF', 96:'A4:5D:36', 
                     97:'A0:D3:C1', 98:'40:A8:F0', 99:'6C:3B:E5'}

    genRandNum = random.randrange(0, 99)
    macAddress = ""

    if (genRandNum in macAddressdb.keys()):
        macAddress += str(macAddressdb[genRandNum])
    else:
        macAddress += str(genRandNum)

    for i in range(0,3):
        if macAddress == "":
            macAddress = generateRandom()
        else:
            macAddress = macAddress+":"+generateRandom()
    
    return macAddress

    #random generator
def generateRandom():

    genlist = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    genRandNum = random.randint(0, 15)

    if (genRandNum in genlist.keys()):
        Gen_Sucess1 = str(genlist[genRandNum])
    else:
        Gen_Sucess1 = str(genRandNum)

    genRandNum2 = random.randint(0, 15)

    if (genRandNum2 in genlist.keys()):
        Gen_Sucess2 = str(genlist[genRandNum2])
    else:
        Gen_Sucess2 = str(genRandNum2)
    
    return Gen_Sucess1+""+Gen_Sucess2