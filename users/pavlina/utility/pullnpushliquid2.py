import time
import sys
sys.path.append('../../../api')
sys.path.append('../../../settings')
from configuration import *
from evobot import EvoBot
from datalogger import DataLogger
from syringe import Syringe
from head import Head
from ExpBCoordinates import *   
from powerOutputs import PowerOutputs

Food1Vessel = 'beakerE'
Food2Vessel = 'beakerD'
heightFood1Vessel = -60
heightFood2Vessel = -60
heightMFCs = -35
foodVolume = 20 #3.5mm = 1 ml
airVolume = 5


sr = 'beakerD'
dt='mfc4'

usrMsgLogger = DataLogger()
evobot = EvoBot(PORT_NO, usrMsgLogger)
head = Head( evobot )
syringe =  Syringe( evobot, SYRINGES['SYRINGE12'])
dispensingModule = Syringe(evobot, SYRINGES['SYRINGE7'])
powerOutputs = PowerOutputs( evobot)


syringe.plungerMoveToDefaultPos()
while True:
    try:
        head.moveToCoord(expBCoord[sr])
        dispensingModule.syringeMove( -45 )
        powerOutputs.turnOnD9()
        time.sleep(3)
        powerOutputs.turnOffD9()
        dispensingModule.syringeMove( 0 )
        
        head.moveToCoord(expBCoord[dt])
        dispensingModule.syringeMove( -45 )
        powerOutputs.turnOnD10()
        time.sleep(3)
        powerOutputs.turnOffD10()
        dispensingModule.syringeMove( 0 )
    except KeyboardInterrupt:
        break

evobot.disconnect()
