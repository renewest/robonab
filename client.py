#  
#  |W3---W4| Rear
#  |-------|
#  |-------|
#  |W2---W1| Front
#      |

import socks
import json
import swerve_calculation

swerve = swerve_calculation.swerve
to_sock01 = socks.to_sock01
to_sock02 = socks.to_sock02

#swerve(FWD, STR, TCW, GYA)
#FWD Forward or reverse -1 to + 1
#STR Strafe right -1 to +1
#RCW Rotate clockwise -1 to +1
#GYA Gyro angle

FWD = -1
STR = 0.5 
RCW = 0.5
GYA = 0

SaD =  swerve(FWD, STR, RCW, GYA) # Steer and Drive SaD
WheelSpeed = ({'WheelSpeed': [ SaD[0], SaD[1], SaD[2], SaD[3] ]})
WheelAngle = ({'WheelAngle': [ SaD[4], SaD[5], SaD[6], SaD[7] ]})
to_sock01(WheelSpeed)
to_sock02(WheelAngle)

print SaD
print WheelSpeed 
print WheelAngle
