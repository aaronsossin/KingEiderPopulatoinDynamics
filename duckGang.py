import numpy as np
import matplotlib.pyplot as plt
from statistics import mean


initialPopulation = 10000
n1= int(initialPopulation/3) #node-1 of model
n2 = int(initialPopulation/3)
n3 = int(initialPopulation/3)

oilSpill = 1000
n3 = n3 - oilSpill

S1 = 0.8 #survival rate from n1 -> n2
S2 = S1 #survival rate from n2 -> n3
S3 = 0.8 #survival rate from n3 -> n3

F3 = 0.78 * 4.41 * 0.36 * 0.10 * 0.65 * 1 * 0.5 #fecundity rate
print("Fecundity rate (doesn't make sense) ",  F3)

timeLapse = 50 #years

""" Initialization """
n1s = [n1]
n2s = [n2]
n3s = [n3]
pops = [initialPopulation]
xs = [0]
pop_loss = []
tot = initialPopulation

""" Running model """
for x in range(timeLapse):
    """ NODE UPDATES"""
    N2 = int(n1*S1)
    N3 = int(n3*S3 + n2*S2)
    N1 = int(n3*F3)
    totalPopulation = N2 + N3 + N1

    """ FOR GRAPH"""
    xs.append(x)
    n1s.append(N1)
    n2s.append(N2)
    n3s.append(N3)
    pop_loss.append(int((totalPopulation - tot)/tot*100))
    pops.append(totalPopulation)

    """ STOP WHEN NO MORE EIDERS"""
    if (N1 < 1 and N2 < 1 and N3 < 1):
        print("YOU DEAD")
        break;

    """ SAVE LAST ITERATION"""
    n1 = N1
    n2 = N2
    n3 = N3
    tot = totalPopulation

print("Average loss: ", mean(pop_loss), "%")
plt.plot(xs, n1s, label="n1")
plt.plot(xs,n2s, label="n2")
plt.plot(xs,n3s, label="n3")
plt.plot(xs, pops, label="total_pop")
plt.legend(loc="upper right")
plt.show()

