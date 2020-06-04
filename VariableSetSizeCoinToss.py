import numpy as np 
import matplotlib.pyplot as plt

def coinToss(nos):
    arr=np.random.randint(0,100000,size=nos)
    arr=arr%2
    return(arr)

def standev(arr):
    arr=arr-np.array([np.average(arr)])
    arr=arr*arr
    return(np.sqrt(np.average(arr)))

def makeBins(N):
    raw_bins = [x for x in range(0,N+1)]
    bins = []
    for n in raw_bins:
        bins.append(n/N)
    return bins

def cointoss_hist(set_numbers):
    start=5
    avg=np.array([])
    st_dev=np.array([])
    sets=np.array([])
    for i in range(set_numbers):
        cum=coinToss(start)
        avg=np.concatenate((avg,np.array([np.average(cum)])),axis=0)
        st_dev=np.concatenate((st_dev,np.array([standev(cum)])),axis=0)
        sets=np.concatenate((sets,np.array([start])),axis=0)
        start+=5
    fig=plt.figure()
    ax1=fig.add_subplot(2,1,1)
    ax1.set_xlabel('averages')
    ax1.set_ylabel('frequency')
    bins = makeBins(1000)
    ax1.hist(avg, bins)
    
    ax2=fig.add_subplot(2,1,2)
    ax2.set_xlabel('set')
    ax2.set_ylabel('standard deviation')
    ax2.plot(sets,st_dev)
    plt.show()
    
cointoss_hist(1000)
