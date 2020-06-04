import numpy as np
import matplotlib.pyplot as plt

def coinFlip(p):  
    result = np.random.binomial(1,p)   
    return result

def makeBins(N):
    raw_bins = [x for x in range(0,N+1)]
    bins = []
    for n in raw_bins:
        bins.append(n/N)
    return bins

probability = .5
n = 1000
N = 1000
fullResults = np.arange(n)
head_frequency = []
tail_frequency = []

for i in range(N+1):
    for j in range(0, n):    
        fullResults[j] = coinFlip(probability)    
        j+=1
    head_frequency.append(np.count_nonzero(fullResults == 1)/n)
    tail_frequency.append(np.count_nonzero(fullResults == 0)/n)

fig=plt.figure()
plt.title('Histogram for 1000 tosses done 1000 times')
ctg1=fig.add_subplot()
ctg1.set_xlabel('Averages')
ctg1.set_ylabel('Frequency of Heads')
bins = makeBins(N)
ctg1.hist(head_frequency, bins)

plt.show()