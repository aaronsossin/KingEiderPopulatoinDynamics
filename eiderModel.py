import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

n1= 500 #int(initialPopulation/3) #node-1 of model
n2 = 500 #int(initialPopulation/3)
#n3 = 9000 #int(initialPopulation/3)
n3 = 9000

globalWarming = False #survival rate slowly decreases
globalWarmingEgg = False
literature = True
catastropheType = 0
if catastropheType == 1:
    n3 = n3 - 1000
elif catastropheType== 2:
    n3 = n3 - 3000
elif catastropheType == 3:
    n2 = n2 - (4600-n3)
    n3 = 0
elif catastropheType == 4:
    n1 = n1 / 3
    n2 = n2/2
    n3 = n3/2

S1 = 0.65 #survival rate from n1 -> n2
S2 = 1 #survival rate from n2 -> n3
S3 = 0.94 #survival rate from n3 -> n3

#if (literature):
    #S2 = 0.87

F3 = 0.78 * 4.41 * 0.36 * 0.10 * 0.65 * 1 * 0.5 #fecundity rate
#F3 = 0.09245411971651946
print(F3)
timeLapse = 50 #years

def model(timeLapse, n1,n2,n3, S1, S2, S3, F3, S1rate=1, S2rate=1, S3rate=1, F3rate=1, globalWarming=False, globalWarmingEgg=False):
    """ Initialization """
    n1s = [n1]
    n2s = [n2]
    n3s = [n3]
    initialPopulation = n1 + n2 + n3
    pops = [initialPopulation]
    xs = [0]
    pop_loss = []
    tot = initialPopulation

    for x in range(timeLapse):
        """ NODE UPDATES"""
        N2 = int(n1*S1)
        N3 = int(n3*S3 + n2*S2)
        N1 = int(n3*F3)
        totalPopulation = N2 + N3 + N1

        """ Parameter Updates"""
        F3 = F3 * F3rate
        S1 = S1*S1rate
        S2 = S2*S2rate
        S3= S3*S3rate
        if (S1 > 1):
            S1 = 1
        if (S2 > 1):
            S2 = 1
        if (S3 > 1):
            S3 = 1

        """ Scenarios """
        if (globalWarming):
            S1 = S1 - 0.01
            S3 = S3 - 0.01

        if (globalWarmingEgg):
            F3 = F3 * 1.01
            if (F3 > 1):
                F3 = 1
            #if (x > 15):
               # S1 = S1 * 0.98
               # S2 = S2 * 0.98
               # S3 = S3 * 0.98


        """ FOR GRAPH"""
        xs.append(x+1)
        n1s.append(N1)
        n2s.append(N2)
        n3s.append(N3)
        pop_loss.append(int((totalPopulation - tot)/tot*100))
        pops.append(totalPopulation)

        """ STOP WHEN NO MORE EIDERS"""
        if (N1 < 1 and N2 < 1 and N3 < 1):
            print("YOU DEAD AFTER ",x, " YEARS")
            break;

        """ SAVE LAST ITERATION"""
        n1 = N1
        n2 = N2
        n3 = N3
        tot = totalPopulation
    return (xs, n1s, n2s, n3s, pop_loss, pops)

xs, n1s, n2s, n3s, pop_loss, pops = model(50,n1,n2,n3, S1, S2, S3, F3, S1rate=0.99, S2rate=0.99, S3rate=0.99)


print("Average loss: ", mean(pop_loss[3:]), "%")
print("Population decrease: ", int((1 - pops[-1]/pops[0]) * 100), "%")
title = "King Eider Population Dynamics\n1% Yearly Decrease in All Survival Rates \n 100% Population Decrease, 0.762 Growth Rate"
plt.title(title)
plt.xlabel("Years")
plt.ylabel("Population of King Eiders")
plt.plot(xs, n1s, label="1-2 Years Old")
plt.plot(xs,n2s, label="2-3 Years Old")
plt.plot(xs,n3s, label=">3 Years Old")
plt.plot(xs, pops, label="Total Population")
plt.legend(loc="upper right")
plt.show()

#Normal: 80%pop decrease, 0.97 growth rate