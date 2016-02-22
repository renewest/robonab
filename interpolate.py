pwm0min, pwm1min, pwm2min, pwm3min = 470, 120, 110, 570
pwm0max, pwm1max, pwm2max, pwm3max = 165, 500, 460, 180
pwm0range = pwm0max - pwm0min
pwm1range = pwm1max - pwm1min
pwm2range = pwm2max - pwm2min
pwm3range = pwm3max - pwm3min

degmin = 0 
degmax = 180
degrange = degmax - degmin
degmid = (degmin + degmax)/2

def degtopwm(deg):
     x = (((deg - degmin) * pwm0range) / degrange) + pwm0min
     return x


print "90 graden", degtopwm(90)
print "45 graden", degtopwm(45)

