import sys
import time
sys.path.append('../api')
sys.path.append('../settings')
import cv2
from users.silvia.petri_dish_coordinates import petridishes
from local import *
from syringe import Syringe
from datalogger import DataLogger
from evobot import EvoBot
from head import Head
from worldcor import WorldCor
import numpy as np
import datetime
from dispenser import Dispenser
from pump import Pump
from syringe import Syringe

usrMsgLogger = DataLogger()
evobot = EvoBot(PORT_NO, usrMsgLogger)
head = Head(evobot)
#
# head.setSpeed(9000)
#
# head.move(40, 150)
# head.setSpeed(3000)
# head.move(0, 0)

# s1_syringe = Syringe(evobot, SYRINGES['SYRINGE1'])
# s1_syringe.plungerMoveToDefaultPos()
# s1_syringe.plungerPullVol(1)

# pump_syringe = Pump(evobot, PUMPS['PUMP1'])
# pump_syringe.setSpeed(100)
# pump_syringe.pumpPushVol(5)

# pump_syringe.continuous_dispensation_of_liquid((154, 293), 10, 40)

# pump_syringe.pumpPushVol(30)


# head.move(100, 100)

air_volume_decanoate = 1.8
syringe_height = -70
volume_amount = 5.0

# fin_vol = volume_amount+0.01
# print fin_vol
#
# s1_syringe = Syringe(evobot, SYRINGES['SYRINGE1'])
# s1_syringe.plungerMoveToDefaultPos()
# s1_syringe.homeSyringe()
# head.move(23, 499)
# # s1_syringe.plungerPullVol(air_volume_decanoate)
# # s1_syringe.syringeMove(syringe_height)
# # s1_syringe.plungerPullVol(volume_amount)
# # s1_syringe.homeSyringe()
# head.move(135.3, 37.4)
# s1_syringe.syringeMove(s1_syringe.syringeGoalPos)
# time.sleep(4)
# # s1_syringe.syringeMove(-30)
#
# # s1_syringe.plungerPushVol(volume_amount+air_volume_decanoate)
# s1_syringe.homeSyringe()


# s1_syringe.continuous_dispensation_of_liquid(head, (135.3, 37.4), volume_amount + air_volume_decanoate, radius=30,
#                                              radius_max=40)


# for i in range(0, 10):
#     i += 1
#     s1_syringe.plungerPullVol(0.9)
#     s1_syringe.plungerPushVol(0.9)


# s1_syringe = Syringe(evobot, SYRINGES['SYRINGE4'])
# head.move(134, 67)
# s1_syringe.syringeMove(-69)
# s1_syringe.plungerPullVol(0.05)
# s1_syringe.homeSyringe()
# head.move(194, 147)
# s1_syringe.syringeMove(s1_syringe.syringeGoalPos)
# s1_syringe.plungerPushVol(0.03)
# time.sleep(3)
# s1_syringe.homeSyringe()

from beaker_coordinates import *
decanol_volume = 0.015

s4_syringe = Syringe(evobot, SYRINGES['SYRINGE4'])
s4_syringe.homeSyringe()

# s4_syringe.plungerMoveToDefaultPos()
# s4_syringe.plungerPullVol(1)

head.move(decanol['decanol_stock'][0], decanol['decanol_stock'][1])
if s4_syringe.canAbsorbVol(decanol_volume):
    s4_syringe.syringeSetSpeed(90)
    # self.decanol_syringe.syringeSetAcc(200)
    s4_syringe.syringeMove(-69)
    s4_syringe.plungerPullVol(decanol_volume)
    s4_syringe.homeSyringe()

head.move(190, 170)
s4_syringe.syringeSetSpeed(80)
s4_syringe.syringeMove(s4_syringe.syringeGoalPos)
s4_syringe.plungerSetSpeed(50)
s4_syringe.plungerPushVol(decanol_volume)
time.sleep(2)
s4_syringe.syringeSetSpeed(120)
s4_syringe.homeSyringe()


evobot.disconnect()

