import numpy as np
import matplotlib.pyplot as plt

#Long Call Condor Option
s0 = 50
k1 = 40;c1 = 4 #Buy 1 ITM Call (k1)       A
k2 = 45;c2 = 3 #Sell 1 ITM Call (k2 > k1) B
k3 = 55;c3 = 2 #Sell 1 OTM Call (k3)      C
k4 = 60;c4 = 1 #Buy 1 OTM Call (k4>k3)    D
shares = 100 #100 shares/lot 

sT = np.arange(0, 2*s0 ,1) #range from 0 - 2*s0, with intervals of 2
#Payoff of k1
y1 = np.where((sT>k1), ((sT - k1) - c1) * shares, -c1 * shares)
#payoff of k2
y2 = np.where((sT>k2), ((k2 - sT) + c2) * shares, c2 * shares)
#payoff of k3
y3 = np.where((sT>k3), ((k3 - sT) + c3) * shares, c3* shares)
#payoff of k4
y4 = np.where((sT>k4), ((sT - k4) - c4) * shares, -c4 * shares)
#Payoff for Condor
y = y1 + y2 + y3 + y4

#Plot
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False) #Remove top border
ax.spines['bottom'].set_position('zero') # Set X-axis in the center
plt.plot(sT,y,lw = 1.5, label = "y")
plt.show()

print(y)
print(y1)
print(y2)
print(y3)
print(y4)