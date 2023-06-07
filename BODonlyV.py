import math
import numpy as np
import matplotlib.pyplot as plt

def nudge(meas, v, maxR, maxD):
    myNudge = -(meas)
    myNudge = (myNudge/maxD)
    if(abs(myNudge) >= maxR):
        myNudge = maxR*np.sign(myNudge)
    """myNudge = (-np.sign(meas)*(abs(meas)/maxD)**(3))
    #if v is also very large, then want to control the nudge a good bit... that way we can flatten out 
    #and still get some noise....

    if(abs(myNudge) >= maxR):
        myNudge = maxR*np.sign(myNudge)"""
    return myNudge

def main():
    #sigma = 0.01
    sigma = 0.020582206531589924
   #maxvs = [0.02, 0.04, 0.08, 0.1]
    #probmaxV = [0.15, 0.3, 0.4, 0.15]
    #maxvs = [0.02,0.04,0.04,0.05,0.04,0.08,0.08,0.08,0.08,0.1,0.1,0.1]
    maxv = 0.03
    maxNudge = sigma*0.2
    maxa = 0.005
    v = 0
    #a = np.random.normal(0, sigma)
    t = 1
    meas = 0
    #the actual value will be 0.
    measurements = [0]
    indeces = [0]
    for i in range(1000):
        #maxNudge*nudge(meas, v, 1, 1)
        v = np.random.normal(0,sigma)
        meas = meas+v*t
        #probv = np.random.randint(12)
        #print(probv)
        #maxv = maxvs[probv]

        #if(abs(v)>maxv):
        #   v = maxv*np.sign(v)
        measurements.append(meas)
        indeces.append(i)
    fig = plt.figure()
    fig.suptitle(
        'test', fontsize=20)
    plt.plot(indeces, measurements,
             label='Measurements', color='r', linewidth=0.3)
    plt.xlabel('Data Points', fontsize=20)
    plt.ylabel('Position (m)', fontsize=20)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
