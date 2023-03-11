import math as m 

theta = m.radians(30)

x = 0 
y = 1.5 
v = 1 
dv = 0.9799
t = x/(v*m.cos(m.radians(30)))
dt = 0.1
a_y = -9.82

while y >= 0 and x < 100: 
    x = v * m.cos(theta) * t 
    y = y + v * m.sin(theta) * t + 1/2 * a_y * t**2
    t += dt 
    v += dv
    print(x, 'm', v, 'm/s', y, 'm', t, 's')
