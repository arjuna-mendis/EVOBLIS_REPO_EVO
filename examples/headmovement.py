import time
import sys
sys.path.append('../api')
sys.path.append('../settings')
from configuration import *
from datalogger import DataLogger
from evobot import EvoBot
from head import Head

usrMsgLogger = DataLogger()
evobot = EvoBot(PORT_NO, usrMsgLogger)
head = Head( evobot )

if not evobot.hasHomed():
    evobot.home()

while True:
    try:
        head.move( 20, 100 )
        head.move( 90, 100 )
    except KeyboardInterrupt:
        break

evobot.disconnect()
