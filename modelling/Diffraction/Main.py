'''
Created on 7 Aug 2018

@author: wvx67826

@Description:
    This take scattering formfactor and calculate the scattered intensisty
'''
import numpy as np
import matplotlib.pyplot as plt
i = complex(0,1)

def th2q(lamda, angle):
    return 4.0*np.pi/lamda*np.sin(angle/180*np.pi)
def q2th(lamda,q):
    return np.arcsin(q*lamda/4.0/np.pi)

def fm(z1,z2,z3,lamda,q,f1,f2):
    return i*f1*np.matrix([[0.0,       z1*np.cos(q2th(lamda,q)-z3*np.sin(q2th(lamda,q)))],
                          [z3*np.sin(q2th(lamda,q)) - z1*np.cos(q2th(lamda,q)),      
                                        -z2*np.sin(2.0*q2th(lamda,q))]])+f2*np.matrix([[z2**2,
                                        -z2*(z1*np.sin(q2th(lamda,q))-z3*np.cos(q2th(lamda,q)))],
                                        [z2*(z1*np.sin(q2th(lamda,q))+z3*np.cos(q2th(lamda,q))),
                                    np.cos(q2th(lamda,q))**2*(z1**2*np.tan(q2th(lamda,q))**2+z3**2)]])
def f0 (lamda, q,scale):
    return scale*np.matrix([[1.0, 0.0],
                    [0.0, np.cos(2.0*q2th(lamda,q))]])

def set_ipol(pol, angle = 0):
    ipol = {"Si"    : np.matrix([[1.0],
                                         [0.0]]),
            "Pi"    : np.matrix([[0.0],
                                         [1.0]]),
            "LC"    : np.matrix([[0.707106781186547],
                                         [0.707106781186547*i]]),
            "RC"    : np.matrix([[0.707106781186547],
                                         [-0.707106781186547*i]]),
            "LA"    : np.matrix([[np.cos(np.deg2rad(angle))],
                                         [np.sin(np.deg2rad(angle))]]),
            }

    return ipol[pol]
def intensity (q,lamda, z,z1,z2,z3,fs,f1,f2):
    temp = np.matrix([[0,0],[0,0]])
    
    for k in range(1):
        for y in z:
            z1rot = z1*np.sin(2.0*y/32*np.pi)
            z2rot = z2*np.sin(2.0*y/32*np.pi)
            z3rot = z3*np.cos(2.0*y/32*np.pi)
            temp = temp + np.exp(i*(y)*q)*((f0(lamda,q,fs))+fm(z1rot,z2rot,z3rot,lamda,q,f1,f2))


    return temp


def pol_intensity(intensity, inPol, outPol, inAngle = 0, outAngle = 0):
    mIpol = set_ipol(inPol,inAngle)
    mFinI = np.multiply(intensity,mIpol)
    if outPol == "Si+Pi":
        finI= np.dot(mFinI[0,0]+mFinI[1,0],np.conj(mFinI[0,0]+mFinI[1,0])) + np.dot(
                     mFinI[0,1]+mFinI[1,1],np.conj(mFinI[0,1]+mFinI[1,1]))
        return np.absolute(finI)
    if outPol == "Si":

        finI = np.dot(mFinI[0,0]+mFinI[1,0],np.conj(mFinI[0,0]+mFinI[1,0]))
        return np.absolute(finI)
    if outPol == "Pi":
        
        finI = np.dot(mFinI[0,1]+mFinI[1,1],np.conj(mFinI[0,1]+mFinI[1,1]))
        return np.absolute(finI)
    
    
    if outPol == "LA":
        finI= np.dot((mFinI[0,0]+mFinI[1,0])*np.cos(np.deg2rad(outAngle)),np.conj(mFinI[0,0]+mFinI[1,0])*np.cos(np.deg2rad(outAngle))) + np.dot(
                     (mFinI[0,1]+mFinI[1,1])*np.sin(np.deg2rad(outAngle)),np.conj(mFinI[0,1]+mFinI[1,1])*np.sin(np.deg2rad(outAngle)))
        return np.absolute(finI)
        
        


    

lamda = 17.5388967468
q = np.arange(0.1, 0.71, 0.01)
z = np.arange (0, 400., 8)
iMeasure1 = []
iMeasure2 = []


fm1 = []
fm2 = []

z1 = 1.0
z2 = 0.0
z3 = 1.0

fs = 0
f1 = 1.1
f2 = 0

for k in q:
    tempI = intensity(k,lamda, z,z1,z2,z3, fs, f1,f2)
    iMeasure1 = np.append(iMeasure1,pol_intensity(tempI,"LC","Si+Pi"))
    iMeasure2 = np.append(iMeasure2,pol_intensity(tempI,"RC","Si+Pi"))

plt.figure(1)
plt.plot(q2th(lamda,q)*180/3.14,iMeasure1)
plt.plot(q2th(lamda,q)*180/3.14,iMeasure2)
plt.show()
