import time
import sys

sys.path.append('../api')
sys.path.append('../settings')
from configuration import *
from evobot import EvoBot
from syringe import Syringe
from datalogger import DataLogger


usrMsgLogger = DataLogger()
evobot = EvoBot(PORT_NO, usrMsgLogger)
syringe = Syringe( evobot, SYRINGE1)

syringe.plungerSetConversion( PLUNGER_CONVERSION_FACTOR ) #mm per ml

syringe.plungerMoveToDefaultPos()
while True:
    syringe.plungerPullVol( 5 )
    syringe.plungerPushVol( 5 )
