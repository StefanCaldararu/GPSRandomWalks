import math
import numpy as np
import matplotlib.pyplot as plt

#measurement is the previous locaiton, maxR is the max range we want to allow, max D is the max Domain we want to allow
#the range will be the maximum nudge we are willing to allow. we don't want ot make it 100% that we move in the right direction
#the domain is what maximum from the mean we want to allow before we "force" it to turn around with the highest probability.


def nudge(meas, maxR, maxD):
    myNudge = -np.sign(meas)*(abs(meas)/maxD)**(11)
    if(abs(myNudge) >= maxR):
        myNudge = maxR*np.sign(myNudge)
    return myNudge

def main():
    sigma = 0.01
    maxv = 0.1
    maxNudge = sigma*0.3
    v = 0
    a = np.random.normal(0, sigma)
    t = 1
    meas = 0
    #the actual value will be 0.
    measurements = [0]
    indeces = [0]
    
    for i in range(1000):
        a = np.random.normal(nudge(meas, maxNudge, 1), sigma)
        meas = meas+v*t+a*t**2
        v = v+a*t
        if(abs(v)>maxv):
           v = maxv*np.sign(v)
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
