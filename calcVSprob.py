import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    line = input()
    i = 0

    vs = []

    indeces = []
    noError = True
    while(noError):
        x = float(line)
        vs.append(x)
        indeces.append(i)
        i = i+1

        try:
            line= input()
        except EOFError as e:
            noError = False

    #now we wnat to compute our stats. we want to first get the different size of jumps in an array...
    accels = []
    maxaccel = 0
    
    for j in range(len(indeces)-1):
        accel =vs[j]-vs[j+1]
        accels.append(accel)
        if(accel>maxaccel):
            maxaccel = accel
    #and we also want to know whhat the likelihood of one being negative is...
    """#now we want ot get the types of jumps... 
    smallJMP = 0.008131838385252443
    medsJMP = 1/150
    medlJMP = 2/210
    largeJMP = 0.01
    #s, ms, ml, l
    dist = [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010]
    counts = [0,0,0,0,0,0,0,0,0,0]
    bestdistance = 100
    bestloc = 0
    for accel in accels:
        bestdistance = 100
        bestloc = 0
        for d in range(0,len(dist)):
            distance = abs(accel-dist[d])
            if(distance<bestdistance):
                bestloc = d
                bestdistance = dist[d]
        counts[bestloc] = counts[bestloc]+1
    print(counts)
    """
    plt.hist(vs, 100)
    plt.show()


    """plt.plot(indeces, vs,
             label='vel', color='r', linewidth=0.3)
    
    plt.xlabel('Data Points', fontsize=20)
    plt.ylabel('vel', fontsize=20)
    plt.legend()
    plt.show()"""

    #now, let's get an average for each one of the histogram "groups". We have: 
    mu,std = norm.fit(vs)
    print(mu)
    print(std)

    


if __name__ == '__main__':
    main()
