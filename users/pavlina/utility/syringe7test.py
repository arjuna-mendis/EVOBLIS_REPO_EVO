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
syringe =  Syringe( evobot, SYRINGES['SYRINGE7'])
syringe2 =  Syringe( evobot, SYRINGES['SYRINGE14'])
evobot.home()
syringe.home()
syringe2.home()
head.moveToCoord(expBCoord[sr])
syringe.syringeMove( -60 )
syringe.syringeMove( 0 )

evobot.disconnect()
