import matplotlib.pyplot as plt


def main():
    line = input()
    line = input()
    i = 0

    xs = []
    ys = []
    indeces = []
    noError = True
    while(noError):
        data = line.split(',')
        x = float(data[1])
        y = float(data[2])
        xs.append(x)
        ys.append(y)
        indeces.append(i)
        i = i+1

        try:
            line= input()
        except EOFError as e:
            noError = False

    maxv = 0
    maxa = 0
    avga = 0
    vs = []
    vi = []
    #we are assuming the time in between each emasurement is 0.1 sec
    dt = 1
    for j in range(0,len(indeces)-3):
        #want to calculate: max v, max a, standard deviation of a, and will eventually also want to do 
        #something with the mean of a depending on the position!!!
        v1 = xs[j]-xs[j+1]/dt
        vi.append(j)
        vs.append(v1)
        v1 = abs(v1)
        v2 = abs(xs[j+1]-xs[j+2])/dt
        a = abs(v1-v2)/dt
        avga = avga+a
        if(v1>maxv):
            maxv = v1
        if(a>maxa):
            maxa = a

    fx = xs[0]
    fxs = []
    txs = []
    for j in vi:
        #print(vs[j])
        txs.append(xs[j])
        fxs.append(fx)
        fx = fx-vs[j]
    print("maxv: "+str(maxv))
    #print("maxa: "+str(maxa))
    #print("avga: "+str(avga/(len(indeces)-3)))

    fig = plt.figure()
    fig.suptitle(
        'GPS data', fontsize=20)
    plt.plot(vi, fxs,
             label='x', color='r', linewidth=0.3)
    #plt.plot(vi, txs, label  = 'y', color = 'b', linewidth = 0.3)
    plt.xlabel('Data Points', fontsize=20)
    plt.ylabel('Position (m)', fontsize=20)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
