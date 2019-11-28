import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

initialPopulation = 10000

n1= int(initialPopulation/3)
n2 = int(initialPopulation/3)
n3 = int(initialPopulation/3)



S1 = 0.8
S2 = S1
S3 = 0.8

F3 = 0.78 * 4.41 * 0.36 * 0.10 * 0.65 * 1 * 0.5
print("F3 ",  F3)

timeLapse = 50
n1s = [n1]
n2s = [n2]
n3s = [n3]
pops = [initialPopulation]
xs = [0]
pop_loss = []
tot = initialPopulation
for x in range(timeLapse):
    N2 = int(n1*S1)
    N3 = int(n3*S3 + n2*S2)
    N1 = int(n3*F3)
    totalPopulation = N2 + N3 + N1
    xs.append(x)
    n1s.append(N1)
    n2s.append(N2)
    n3s.append(N3)
    pop_loss.append(int((totalPopulation - tot)/tot*100))
    pops.append(totalPopulation)
    #print("Total Population ", totalPopulation)
    """
    
    print("Year ", x + 1)
    print("n1 ",N1)
    print("n2 ", N2)
    print("n3 ", N3)
    """

    if (N1 < 1 and N2 < 1 and N3 < 1):
        print("YOU DEAD")
        break;
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

