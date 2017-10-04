# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import schedule
import datetime
import threading
import sys
sys.path.append('../../api')
sys.path.append('../../settings')
from configuration import *
from evobot import EvoBot
from datalogger import DataLogger
from syringe import Syringe
from head import Head
import csv
import os
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import time
import random
import Queue
import visa
#visa.log_to_screen()

lock = threading.Lock()
C1MFC1 = 0
C1MFC2 = 0
C1MFC3 = 0
C1MFC4 = 0
C1MFC5 = 0
C1MFC6 = 0
C1MFC7 = 0
C1MFC8 = 0
C1MFC9 = 0
C1MFC10 = 0
C1MFC11 = 0
C1MFC12 = 0
C1MFC13 = 0
C1MFC14 = 0
C1MFC15 = 0
C1MFC16 = 0
C1MFC17 = 0
C1MFC18 = 0

safeMFC1 = []
safeMFC2 = []
safeMFC3 = []
safeMFC4 = []
safeMFC5 = []
safeMFC6 = []
safeMFC7 = []
safeMFC8 = []
safeMFC9 = []
safeMFC10 = []
safeMFC11 = []
safeMFC12 = []
safeMFC13 = []
safeMFC14 = []
safeMFC15 = []
safeMFC16 = []
safeMFC17 = []
safeMFC18 = []
safeTimeCard1 = []

print " Start Polarization "
for Counter in range(255,0,-1):
    resval=(Counter+1)*4.4921875+50   #calibration : (1200-50)/256*(counter+1)+50
    print "Current Resistor value: "+ str(resval)
    time.sleep(1) #------------------------Set time here in seconds for interval
    try:
        rm = visa.ResourceManager()
        inst = 'ASRL7::INSTR'
        agilent = rm.open_resource(inst)
        print(agilent.query('*IDN?'))
        print(agilent.query('*IDN?'))
        print(agilent.query("SET:"+Counter))
    except:
        print "something was wrong with the pol gadget"
        
    try:
        print "Agilent DA OPP"
        Card1voltage='0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,\n'

        
        rm = visa.ResourceManager()
        inst = 'USB0::2391::8199::MY49012441::0::INSTR'
        agilent = rm.open_resource(inst)
        print(agilent.query('*IDN?'))
        agilent.write("*RST")
        agilent.write("*CLS")
        agilent.write('CONFigure:VOLTage:DC 1,(@101:120)')
        agilent.write('SENSe:VOLTage:DC:NPLC 1,(@101:120)')
        agilent.write("ROUTe:CHANnel:DELay 0,(@101:120) ")
        print(agilent.query('ROUTe:SCAN?'))
        time.sleep(1)
        ##print "scan"
        agilent.write('INITiate')
        time.sleep(5)
        agilent.write('FETC?')

        Card1voltage = agilent.read() #saves all the values as an array
        print Card1voltage
        #print(agilent.read())
        agilent.write("*RST")
        agilent.write("*CLS")
        agilent.close()
        rm.close()

        today1 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
        C1MFC1, C1MFC2, C1MFC3, C1MFC4, C1MFC5, C1MFC6, C1MFC7, C1MFC8, C1MFC9, C1MFC10, C1MFC11, C1MFC12, C1MFC13, C1MFC14, C1MFC15, C1MFC16, C1MFC17, C1MFC18, C1MFC19, C1MFC20 = (Card1voltage.split(','))
        #saves the measured values in variables NUMBER OF VARIABLES NEED TO BE THE SAME THAN THE MEASURED CHANNELS OR ELSE YOU WILL GET AN ERROR MESSAGE!
        C1MFC20 = C1MFC20.rstrip('\n') #last value still contains the new line command which needs to be delete
        
       
        #print "write logfile"
        Card1txt = ''
        Card1txt = 'RES Val' + '\t'+ str(resval)+'\t' +today1 + '\t' + str(C1MFC1) + '\t' + str(C1MFC2) + '\t' + str(C1MFC3) + '\t' + str(C1MFC4) + '\t' + str(C1MFC5) + '\t' + str(C1MFC6) + '\t' + str(C1MFC7) + '\t' + str(C1MFC8) + '\t' + str(C1MFC9) + '\t' + str(C1MFC10) + '\t' + str(C1MFC11) + '\t' + str(C1MFC12) + '\t' + str(C1MFC13) + '\t' + str(C1MFC14) + '\t' + str(C1MFC15) + '\t' + str(C1MFC16) + '\t' + str(C1MFC17) + '\t' + str(C1MFC18) + '\t' + str(C1MFC19) + '\t' + str(C1MFC20) + '\n'
        logfile1 = open('Polarize_RV.txt', 'a') #appends the logfile
        logfile1.write(Card1txt)
        logfile1.close()

        timeNow = datetime.datetime.now()
        # [AM] - need to return float if i want to take mean etc. using numpy
        #return [float(C1MFC1), float(C1MFC2), float(C1MFC3), float(C1MFC4), float(C1MFC5), float(C1MFC6), float(C1MFC7), float(C1MFC8), float(C1MFC9), float(C1MFC10), float(C1MFC11), float(C1MFC12), float(C1MFC13), float(C1MFC14), float(C1MFC15), float(C1MFC16), float(C1MFC17), float(C1MFC18), float(C1MFC19), float(C1MFC20)]
    except:

        print "Agilent not connected?"
        #return None
        #quit_prog()
