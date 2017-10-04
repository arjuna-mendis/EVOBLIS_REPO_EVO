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
syringe =  Syringe( evobot, SYRINGES['SYRINGE16'])
evobot.home()

syringe.plungerMoveToDefaultPos()
while True:
    try:
        head.moveToCoord(expBCoord[sr])
        syringe.syringeMove( -20 )
        syringe.plungerPullVol( airVolume )
        time.sleep(1)
        syringe.plungerPullVol( foodVolume ) 
        syringe.syringeMove( 0 )
        head.moveToCoord(expBCoord[dt])
        syringe.syringeMove( -20 )
        syringe.plungerPullVol( airVolume + foodVolume ) 
        syringe.syringeMove( 0 )
    except KeyboardInterrupt:
        break

evobot.disconnect()
