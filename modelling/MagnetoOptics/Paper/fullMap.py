
'''
Created on 10 Sep 2021

@author: wvx67826
'''

from modelling.MagnetoOptics.UniversalMoke import XrayMoke
import timeit
import numpy as np
import matplotlib.pyplot as plt

from Tools.Output.Output import Output
from scipy import optimize
from _pytest.mark import param

def sin_func(x, a, b,c,d):
    return a + c*np.sin(b + x*np.pi/180.*d)





Dp = Output() 

Dp.add_clipboard_to_figures()


i = complex(0,1)
xrMoke = XrayMoke()

##============= Define sample gamma and beta ===============================
n  = np.array([
               1.0,
               1.0 + 0.00376976072  + 0.00253175874*i, #Pt
               1.0 + 0.0014459691   + 0.000331679883*i, #permalloy 80             
               1.0 + 0.00102811039  + 0.000295088976*i, #SiO2
               1.0 + 0.000922611449 + 0.0001342364124*i #Si 
               ])

d = np.array([
              0,
              15,
              15,
              15,
              15,
              15,
              15,
              15,
              15,
              200,
              308.4
              ])

q = np.array([
              0.0,
              0.0,
              0.0014459691*0.3 + 0.00331679883*0.3*i, 
              0.0,
              0.0
              ])
aPhi =   np.array([0.0, 0.0, 45 ,0.0,    45,  0.0,  45, 0.0, 45,  0, 0.0])
aGamma = np.array([0.0, 0.0, 90,0.0, 90.0, 0.0, 90, 0.0,90, 0.0, 0.0])
##=================================================================================

"""
##============= Define sample gamma and beta ===============================
n  = np.array([
               1.0,
               1.0 + 0.00376976072  + 0.00253175874*i, #Pt
               1.0 + 0.0014459691 + 0.000331679883*i, #permalloy 80
               1.0 + 0.000922611449 + 0.0001342364124*i #Si 
               ])

d = np.array([
              0,
              50,
              100,
              308.4
              ])

q = np.array([
              0.0,
              0,
              0.0014459691*0.01 + 0.00331679883*0.01*i, 
              0.0
              ])
aPhi =   np.array([0.0,0.0, 1,0, 0.0,])
aGamma = np.array([0.0,0.0, 90,0, 0.0,])
##=================================================================================
"""
"""To store result"""
angle = np.array([])

"""Define energy"""
waveLen = 12.4/0.708
"""timer"""
start_time1 = timeit.default_timer()

"""define moment direction and how it changes"""


angle = np.arange(-100,100,1.0)
#angle = np.append(angle, np.arange(100,-100,-1.0))

#spin = [0, 180, 0] #right angle to beam
#spin = [15, -15, 0 ] #right angle to beam

#spin = [-90,90] #parallel 
#hy = np.full((1,80),spin[0])
#hy = np.append(hy, np.arange(spin[0], spin[1], -(spin[0]-spin[1])/5.0))
#hy = np.append(hy, np.full((1,100),spin[1]))
#hy = np.append(hy, np.full((1,120),spin[1]))
#hy = np.append(hy, np.arange(spin[1], spin[0], -(spin[1]-spin[0])/20.0))
#hy = np.append(hy, np.full((1,80),spin[0]))
hy = np.arange (0,180*6, 180*6/200)
angle = hy

"""
hy = np.full((1,100),spin[0])
hy = np.append(hy, np.arange(spin[0], spin[1], -(spin[0]-spin[1])/20.0))
hy = np.append(hy, np.full((1,180),spin[1]))
hy = np.append(hy, np.arange(spin[1], spin[0], -(spin[1]-spin[0])/20.0))
hy = np.append(hy, np.full((1,80),spin[0]))
"""


#lTheta = [2,10,20,30,40,50]
#lTheta = [30]
lTheta = np.arange(0,30,0.2)
field = np.array([])
intensity = np.array([])
lth = np.array([])

aGamma  = np.deg2rad(aGamma)
aPhi = np.deg2rad(aPhi)
lAngle     = np.array([])
lth        = np.array([])
lIntensity1 = np.array([])
lIntensity2 = np.array([])
lIntensity3 = np.array([])
lIntensity4 = np.array([])
lIntensity5 = np.array([])
lIntensity6 = np.array([])
lIntensity7 = np.array([])
lIntensity8 = np.array([])
lIntensity9 = np.array([])
phase = np.array([])
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

    thetaWanted =ange
    theta = 90 - thetaWanted 
    theta = np.deg2rad(theta)
    
    

    """do the hvm loop"""
    for gamma1 in hy:    
        offsetA = 15
        aGamma[2] = np.deg2rad(gamma1)
        aGamma[4] = np.deg2rad(gamma1+offsetA )
        aGamma[6] = np.deg2rad(gamma1+offsetA )
        aGamma[8] = np.deg2rad(gamma1+offsetA )
              

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

    lIntensity9 = np.append(lIntensity9 , ((intensity9-np.min(intensity9))/np.max(intensity9)))

    lIntensity8 = np.append(lIntensity8 , ((intensity8-np.min(intensity8))/np.max(intensity8)))
    try:
        params, params_covariance = optimize.curve_fit(sin_func, hy, intensity9,
                                               p0=[np.max(intensity9), 0,0.1,1])
    except RuntimeError:
        params[1]=0
    #print(params[0])
    lIntensity1 = np.append(lIntensity1,params[1])
    lIntensity2 = np.append(lIntensity2,intensity9[0])
    lIntensity3 = np.append(lIntensity3,intensity8[0])
    #lIntensity9 = np.append(lIntensity9 , ((intensity1-np.min(intensity1))/np.max(intensity1)))

    #lIntensity8 = np.append(lIntensity8 , ((intensity2-np.min(intensity2))/np.max(intensity2)))
    """plt.figure()
    plt.scatter(hy, intensity9, label='Data')
    plt.plot(hy, sin_func(hy, params[0], params[1],params[2]),
         label='Fitted function')

    plt.legend(loc='best')

    plt.show()

"""    
    elapsed = timeit.default_timer() - start_time1
    lAngle = np.append(lAngle,angle )
    tempTh = np.full((1, len(angle)), ange)[0]
    lth    = np.append(lth,tempTh)
    print (elapsed)
    """
    with open("dataOut_90.dat", "w") as f:
        f.write("field, Pi-full, Si-full,Pi-Si, Pi-Pi, Si-Si, Si,-Pi, XMCD, LC,RC \n")
        for k in range (0,len(angle)):                
            f.write("%.8g , %.8g , %.8g, %.8g , %.8g , %.8g,, %.8g , %.8g , %.8g , %.8g \n"
                     %(angle[k],intensity1[k],intensity2[k],intensity3[k],
                       intensity4[k],intensity5[k],intensity6[k],intensity7[k],intensity8[k]
                       ,intensity9[k]))
    """
    """
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
    #plt.figure(7)
    plt.subplot(223)
    plt.title("Pi - Si")
    plt.plot(angle, intensity7)
    #plt.figure(8)
    plt.subplot(224)
    plt.title("LC &RC")
    plt.plot(angle, intensity8)
    plt.plot(angle, intensity9)
    """
    
    plt.show()
i = "PCI"
j = "PNI"
print (len(lth), len(lAngle), len(lIntensity9))
#lth = 4*np.pi/(12.4/0.707)*np.sin(np.deg2rad(lth))
plt.figure()
plt.tricontourf( lth, lAngle, lIntensity9, 30, cmap=plt.get_cmap('jet'))
plt.title("Positive Helicity Increasing", fontsize=18)
#plt.title("Positive Helicity Decreasing", fontsize=18)


plt.xlabel("Theta (\u00b0)", fontsize=18)
plt.colorbar()
plt.savefig("%s-refMap" %(i))
plt.figure()
plt.tricontourf(lth, lAngle, lIntensity8, 30, cmap=plt.get_cmap('jet'))
plt.title("Negative Helicity Increasing", fontsize=18)
#plt.title("Negative Helicity Decreasing", fontsize=18)
plt.xlabel("Theta (\u00b0)", fontsize=18)
plt.colorbar()
plt.savefig("%s-refMap" %(j))
plt.figure()
plt.plot(lTheta,lIntensity1*180/np.pi)

plt.figure()
plt.plot(lTheta,lIntensity2)
plt.plot(lTheta,lIntensity3)

plt.show()

