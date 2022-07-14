'''
Created on 10 Sep 2021

@author: wvx67826
'''
'''
Created on 10 Apr 2019

@author: wvx67826
'''
from modelling.MagnetoOptics.UniversalMoke import XrayMoke
import timeit
import numpy as np
import matplotlib.pyplot as plt

from Tools.Output.Output import Output


Dp = Output() 

Dp.add_clipboard_to_figures()


i = complex(0,1)
xrMoke = XrayMoke()

##============= Define sample gamma and beta ===============================
n  = np.array([
               1.0,
               1.0 + 0.0014459691 + 0.000331679883*i, #permalloy 80
               ])

d = np.array([
              0,
              100,
              ])

q = np.array([
              0.0,
              0.0014459691*0.1 + 0.00331679883*0.1*i, 
              ])
aPhi =   np.array([0.0, 90,])
aGamma = np.array([0.0, 90,])
##=================================================================================

"""To store result"""
angle = np.array([])

"""Define energy"""
waveLen = 12.4/0.708
"""timer"""
start_time1 = timeit.default_timer()

"""define moment direction and how it changes"""


angle = np.arange(-100,100,1.0)
angle = np.append(angle, np.arange(100,-100,-1.0))

#spin = [0, 180, 0] #right angle to beam
#spin = [15, -15, 0 ] #right angle to beam

spin = [90,-90] #parallel 
hy = np.full((1,100),spin[0])
hy = np.append(hy, np.arange(spin[0], spin[1], -(spin[0]-spin[1])/20.0))
hy = np.append(hy, np.full((1,180),spin[1]))
hy = np.append(hy, np.arange(spin[1], spin[0], -(spin[1]-spin[0])/20.0))
hy = np.append(hy, np.full((1,80),spin[0]))

lTheta = [1]
#lTheta = [30]
field = np.array([])
intensity = np.array([])
lth = np.array([])

aGamma  = np.deg2rad(aGamma)
aPhi = np.deg2rad(aPhi)
for ange in lTheta:
    
    intensity1 = np.array([])
    intensity2 = np.array([])
    intensity3 = np.array([])
    intensity4 = np.array([])
    intensity5 = np.array([])
    intensity6 = np.array([])
    intensity7 = np.array([])
    intensity8 = np.array([])
    intensity9 = np.array([])
    
    print (intensity9)
    
    thetaWanted =ange
    theta = 90 - thetaWanted 
    theta = np.deg2rad(theta)
    
    

    #for gamma1 in np.arange (90,450, 1.0):
    """do the hvm loop"""
    for gamma1 in hy:    
        #aPhi[1] = np.deg2rad(gamma1)
        #aPhi[4] = np.deg2rad(gamma1)
        aGamma[1] = np.deg2rad(gamma1)
        #aGamma[4] = np.deg2rad(gamma1)
        """    if gamma1 ==spin[0]:
            aPhi[3] = np.deg2rad(14)
        if gamma1 == spin[1]:
            aPhi[3] =  np.deg2rad(14)
        if gamma1 == spin[2]:
            aPhi[3] = np.deg2rad(-14)
        """
        #aGamma[2] = np.deg2rad(gamma1)
        #aGamma[3] = -np.deg2rad(gamma1)
        ##aGamma[2] = np.deg2rad(gamma1)
        Qz = gamma1-90#4.0*np.pi/waveLen*np.sin(np.deg2rad(90.-gamma1))   
          
        #aGamma = np.array([0, 90,0])
        #aGamma  = np.deg2rad(aGamma)
        xrMoke.cal_intensity_mD(n, theta, aGamma, aPhi, q, d, waveLen)
        intensity1 = np.append(intensity1,xrMoke.get_intensity("Pi", "Si+Pi"))
        intensity2 = np.append(intensity2,xrMoke.get_intensity("Si", "Si+Pi"))
        intensity3 = np.append(intensity3,xrMoke.get_intensity("Pi", "Si"))
        intensity4 = np.append(intensity4,xrMoke.get_intensity("Pi", "Pi"))
        intensity5 = np.append(intensity5,xrMoke.get_intensity("Si", "Si"))
        intensity6 = np.append(intensity6,xrMoke.get_intensity("Si", "Pi"))
        intensity7 = np.append(intensity7,(xrMoke.get_intensity("LC", "Si+Pi")
                                           -xrMoke.get_intensity("RC", "Si+Pi")))
        intensity8 = np.append(intensity8,xrMoke.get_intensity("LC", "Si+Pi"))
        intensity9 = np.append(intensity9,xrMoke.get_intensity("RC", "Si+Pi"))

    elapsed = timeit.default_timer() - start_time1
    print (elapsed)
    with open("dataOut_90.dat", "w") as f:
        f.write("field, Pi-full, Si-full,Pi-Si, Pi-Pi, Si-Si, Si,-Pi, XMCD, LC,RC \n")
        for k in range (0,len(angle)):                
            f.write("%.8g , %.8g , %.8g, %.8g , %.8g , %.8g,, %.8g , %.8g , %.8g , %.8g \n"
                     %(angle[k],intensity1[k],intensity2[k],intensity3[k],
                       intensity4[k],intensity5[k],intensity6[k],intensity7[k],intensity8[k]
                       ,intensity9[k]))
    
    plt.figure()
    plt.suptitle("th = {}".format(ange))
    plt.title(theta)
    plt.subplot(221)
    #plt.semilogy()
    plt.title("Pi")
    plt.plot(angle, intensity1)
    #plt.figure(2)
    plt.subplot(222)
    plt.title("Si")
    plt.plot(angle, intensity2)
    #plt.figure(3)
    """plt.title("Pi-Si")
    plt.plot(angle, intensity3)
    plt.figure(4)
    plt.title("Pi-Pi")
    plt.plot(angle, intensity4)
    plt.figure(5)
    plt.title("Si-Si")
    plt.plot(angle, intensity5)
    plt.figure(6)
    plt.title("Si-Pi")
    plt.plot(angle, intensity6)
    """
    #plt.figure(7)
    plt.subplot(223)
    plt.title("XMCD")
    plt.plot(angle, intensity7)
    #plt.figure(8)
    plt.subplot(224)
    plt.title("LC &RC")
    plt.plot(angle, intensity8)
    plt.plot(angle, intensity9)
    
    
plt.show()
