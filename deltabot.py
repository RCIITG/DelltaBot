import math, serial, struct, time

port = ('COM4')
arduino = serial.Serial(port,9600)
time.sleep(2)

prevTheta1 = 10
prevTheta2 = 10
prevTheta3 = 10

def closerTo(prevTheta,theta1,theta2):
    if (abs(prevTheta - theta1)<=abs(prevTheta-theta2)):
        return theta1
    if (abs(prevTheta - theta2)<abs(prevTheta-theta1)):
        return theta2


L = 20
l = 42
wb = 8.66
up = 3
wp = 1.5
sp = 5.2

a = wb - up
b = (sp - 1.73*wb)/2
c = wp - wb/2

z=-45
i=0

while True:
    if (i%4==0):
        x = 15 
        y = 15
    elif (i%4==1):
        x = -15 
        y = 15
    elif (i%4==2):
        x = -15 
        y = -15
    else:
        x = 15 
        y = -15

    i = i+1

    E1 = 2*L*(y+a)
    F1 = 2*z*L
    G1 = x**2 + (y+a)**2 + z**2 - l**2 + L**2

    E2 = -(L*(1.73*(x+b)+y+c))
    F2 =  2*z*L
    G2 =  x**2 + y**2 + z**2 +b**2 + c**2 +L**2 +2*(x*b + y*c) - l**2

    E3 = L*(1.73*(x-b)-y-c)
    F3 =  2*z*L
    G3 = x**2 + y**2 +z**2 +b**2 +c**2 +L**2 +2*((-x*b)+y*c) - l**2

    D1 = E1**2 + F1**2 - G1**2
    D2 = E2**2 + F2**2 - G2**2
    D3 = E3**2 + F3**2 - G3**2

    if (D1<0)or(D2<0)or(D3<0):
        print ("Not possible")

    else:
        t11 = (-F1 + (E1 ** 2 + F1 ** 2 - G1 ** 2) ** 0.5) / (G1 - E1)
        theta11 = int(math.atan(t11) * 180 / 3.1415)
        t12 = (-F1 - (E1 ** 2 + F1 ** 2 - G1 ** 2) ** 0.5) / (G1 - E1)
        theta12 = int(math.atan(t12)* 180 / 3.1415)

        t21 = (-F2 + (E2 ** 2 + F2 ** 2 - G2 ** 2) ** 0.5) / (G2 - E2)
        theta21 = int(math.atan(t21) * 180 / 3.1415)
        t22 = (-F2 - (E2 ** 2 + F2 ** 2 - G2 ** 2) ** 0.5) / (G2 - E2)
        theta22 = int(math.atan(t22) * 180 / 3.1415)

        t31 = (-F3 + (E3 ** 2 + F3 ** 2 - G3 ** 2) ** 0.5) / (G3 - E3)
        theta31 = int(math.atan(t31) * 180 / 3.1415)
        t32 = (-F3 - (E3 ** 2 + F3 ** 2 - G3 ** 2) ** 0.5) / (G3 - E3)
        theta32 = int(math.atan(t32) * 180 / 3.1415)

        theta1 = closerTo(prevTheta1,theta11,theta12)
        theta2 = closerTo(prevTheta2,theta21,theta22)
        theta3 = closerTo(prevTheta3,theta31,theta32)

        print(theta1,theta2,theta3)
        print(struct.pack('>BBB',theta1,theta2,theta3))


        prevTheta1 = theta1
        prevTheta2 = theta2
        prevTheta3 = theta3

        arduino.write(struct.pack('>BBB',theta1,theta2,theta3))

        time.sleep(1)