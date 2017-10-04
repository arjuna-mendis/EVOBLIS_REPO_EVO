import time
import sys
sys.path.append('../../../api')
sys.path.append('../../../settings')
from configuration import *
from evobot import EvoBot
from datalogger import DataLogger
from syringe import Syringe
from powerOutputs import PowerOutputs
from head import Head
import csv
import datetime

usrMsgLogger = DataLogger()
evobot = EvoBot(PORT_NO, usrMsgLogger)
head = Head( evobot )
powerOutputs = PowerOutputs( evobot)

##with open('generation_summary-{}.csv'.format(
##        datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")), 'ab') as f:
##    writer = csv.writer(f, delimiter=',')
##    writer.writerow(['generation %d ' % gen])
##    writer.writerows([
##        my_list
##    ])
currentTime = datetime.datetime.now()
with open('test-{}.csv'.format(datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")), 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow([
        currentTime.strftime("%Y.%m.%d"),
        currentTime.strftime("%H.%M.%S"),
    ])
evobot.disconnect()
