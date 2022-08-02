'''
Created on 10 Apr 2019

@author: wvx67826
'''
from UniversalMoke import XrayMoke
import timeit
import numpy as np
import matplotlib.pyplot as plt
from Tools.Output.Output import Output

Dp = Output() 

Dp.add_clipboard_to_figures()

i = complex(0,1)
xrMoke = XrayMoke()

##============= Define sample gamma and beta ===============================
n  = np.array([1.0,
               1.0 + 0.00132421786  + 0.00107614317*i, #pt
               1.0 + 0.00106697413  + 0.0006667712*i,  #CoFeB
               1.0 + 0.00106697413  + 0.0006667712*i,  #CoFeB
               1.0 + 0.000726061175 + 0.000175910551*i, #SiO
               1.0 + 0.000759251474 + 9.64275096E-05*i]) #Si

d = np.array([0,
              20,
              100,
              20,
              200,
              200])
q = np.array([0,
              0,
              1.68661e-4+1.06361e-5*i,
              1.68661e-4+1.06361e-5*i,
              0,
              0])

aPhi =   np.array([0,
                   0,
                   90,
                   90,
                   0,
                   0])
aPhiS =   np.array([0,
                    0,
                   90,
                   90,
                   0,
                   0])
aGamma = np.array([0,
                   0,
                   0,
                   5,
                   0,
                   0])

aGammaS = np.array([0,
                    0,
                    180,
                    170,
                    0,
                    0])
##=================================================================================
"""To store result"""
angle = np.array([])

"""Define energy"""
waveLen = 12.4/0.777198
"""timer"""
start_time1 = timeit.default_timer()

thetaWanted =np.arange(0.1,90,0.1) 
theta = 90 - thetaWanted 

aGamma  = np.deg2rad(aGamma)
aGammaS  = np.deg2rad(aGammaS)
theta = np.deg2rad(theta)
aPhi = np.deg2rad(aPhi)
aPhiS = np.deg2rad(aPhiS)
qth = 4*np.pi/waveLen*np.sin (thetaWanted/180*np.pi)

for j in range (20,121,130):
    intensity1 = np.array([])
    intensity2 = np.array([])
    intensity3 = np.array([])
    intensity4 = np.array([])
    intensity5 = np.array([])
    intensity6 = np.array([])
    intensity7 = np.array([])
    intensity8 = np.array([])
    intensity9 = np.array([])
    intensity1S = np.array([])
    intensity2S = np.array([])
    intensity3S = np.array([])
    intensity4S = np.array([])
    intensity5S = np.array([])
    intensity6S = np.array([])
    intensity7S = np.array([])
    intensity8S = np.array([])
    intensity9S = np.array([])

    d[2] = 120.0-j
    d[3] = j
    print (d)
    
    for i in theta:
        xrMoke.cal_intensity_mD(n, i, aGamma, aPhi, q, d, waveLen)
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
        
    for i in theta:
        xrMoke.cal_intensity_mD(n, i, aGammaS, aPhiS, q, d, waveLen)
        intensity1S = np.append(intensity1S,xrMoke.get_intensity("Pi", "Si+Pi"))
        intensity2S = np.append(intensity2S,xrMoke.get_intensity("Si", "Si+Pi"))
        intensity3S = np.append(intensity3S,xrMoke.get_intensity("Pi", "Si"))
        intensity4S = np.append(intensity4S,xrMoke.get_intensity("Pi", "Pi"))
        intensity5S = np.append(intensity5S,xrMoke.get_intensity("Si", "Si"))
        intensity6S = np.append(intensity6S,xrMoke.get_intensity("Si", "Pi"))
        intensity7S = np.append(intensity7S,(xrMoke.get_intensity("LC", "Si+Pi")
                                           -xrMoke.get_intensity("RC", "Si+Pi")))
        intensity8S = np.append(intensity8S,xrMoke.get_intensity("LC", "Si+Pi"))
        intensity9S = np.append(intensity9S,xrMoke.get_intensity("RC", "Si+Pi"))
        
        
    elapsed = timeit.default_timer() - start_time1
    print (elapsed)
    
    plt.figure()
    title = "Current Driven saturation asymmetry d = {}".format(j)
    plt.suptitle(title)
    

    plt.subplot(211)
    plt.semilogy()
    plt.plot(qth , intensity8 , label = "CP m1", ls = "--", color = "red")
    plt.plot(qth , intensity8S, label = "CP m2", ls = ":", color = "blue" )
    plt.plot(qth , intensity9 * 100.0 , label = "CN m1", ls = "--", color = "red")
    plt.plot(qth , intensity9S * 100.0, label = "CN m2", ls = ":", color = "blue" )
    plt.legend()
    plt.subplot(212)
    plt.plot(qth ,(intensity8-intensity8S)/(intensity8+intensity8S),
              label = "CP", ls = "--", color = "red")
    plt.plot(qth ,  (intensity9-intensity9S)/(intensity9+intensity9S),
              label = "CN", ls = "--", color = "blue")
    plt.legend()
    plt.figure(2)
    title = "Current Driven saturation asymmetry"
    plt.suptitle(title)
    plt.plot(qth ,(intensity8-intensity8S)/(intensity8+intensity8S)
             -(intensity9-intensity9S)/(intensity9+intensity9S),
              label = "double aasymmetry d={}".format(j), ls = "--")
    plt.legend()
    
    plt.figure()
    title =  "Current Driven polarization asymmetry d = {} ".format(j)
    plt.suptitle(title)

    
    plt.subplot(211)
    plt.semilogy()
    plt.plot(qth , intensity8 , label = "CP m1", ls = "--", color = "red")
    plt.plot(qth, intensity8S* 100.0, label = "CP m2", ls = ":", color = "red" )
    plt.plot(qth, intensity9  , label = "CN m1", ls = "--", color = "blue")
    plt.plot(qth, intensity9S * 100.0, label = "CN m2", ls = ":", color = "blue" )
    plt.legend()
    plt.subplot(212)
    plt.plot(qth ,(intensity8-intensity9)/(intensity8+intensity9),
              label = "m1", ls = "--", color = "red")
    plt.plot(qth ,  (intensity8S-intensity9S)/(intensity8S+intensity9S),
              label = "m2", ls = "--", color = "blue")
    plt.legend()
    plt.figure(4)
    title =  "Current Driven polarization asymmetry"
    plt.suptitle(title)
    plt.plot(qth ,(intensity8-intensity9)/(intensity8+intensity9)
             -(intensity8S-intensity9S)/(intensity8S+intensity9S)
              ,label = "double asymmetry d={}".format(j), ls = "--")
    plt.legend()
    
plt.show()
"""plt.subplot(212)
plt.semilogy()
plt.plot(thetaWanted , intensity9)
plt.plot(thetaWanted , intensity9S)
plt.subplot(223)
plt.plot(thetaWanted , (intensity8-intensity8S)/(intensity8+intensity8S))
plt.subplot(224)
plt.plot(thetaWanted ,  (intensity9-intensity9S)/(intensity9+intensity9S))

plt.figure(3)
plt.plot(thetaWanted ,(intensity8-intensity8S)/(intensity8+intensity8S))
plt.plot(thetaWanted ,  (intensity9-intensity9S)/(intensity9+intensity9S))"""








