# Swerve Drive Calculation v 0.1
#  |W3---W4| Rear
#  |-------|
#  |-------|
#  |W2---W1| Front
#      |	

import math

# L = wheelbase, W = Trackwidth
# Only ratios counts, units makes no differents
L, W = 45, 45
R = math.sqrt( L**2 +  W**2 )

#FWD = -0.5 # Forward or reverse -1 to + 1
#STR = 1 # Strafe right -1 to +1
#RCW = 0.5 # Rotate clockwise -1 to +1
#GYA = 0 # Gyro angle

def swerve(FWD, STR, RCW, GYA):
        tmp = FWD * math.cos(GYA) + STR * math.sin(GYA)
        STR = -FWD * math.sin(GYA) + STR * math.cos(GYA)
        FWD = tmp

        A = STR - RCW * ( L / R )
        B = STR + RCW * ( L / R )
        C = FWD - RCW * ( W / R )
        D = FWD + RCW * ( W / R )

        ws1 = math.sqrt( B**2 + C**2 ) # wheel speed front right
        ws2 = math.sqrt( B**2 + D**2 ) # front left
        ws3 = math.sqrt( A**2 + D**2 ) # rear left
        ws4 = math.sqrt( A**2 + C**2 ) # rear right

        wa1 = math.atan2( B, C ) * ( 180 / math.pi ) # wheel angle front right
        wa2 = math.atan2( B, D ) * ( 180 / math.pi ) # front left
        wa3 = math.atan2( A, D ) * ( 180 / math.pi ) # rear left
        wa4 = math.atan2( A, C ) * ( 180 / math.pi ) # rear right

        # Normalize speed
        smax = ws1
        if ws2 > smax: smax = ws2
        if ws3 > smax: smax = ws3
        if ws4 > smax: smax = ws4

        # print "Gyro angle ", GYA
        # print "ws1, ws2, ws3, ws4 ", ws1, ws2, ws3, ws4
        # print "wa1, wa2, wa3, wa4 ", wa1, wa2, wa3, wa4
	return(ws1,  ws2,  ws3, ws4, wa1, wa2, wa3,  wa4)

#swerve(1, 1, 0.5, 0)
