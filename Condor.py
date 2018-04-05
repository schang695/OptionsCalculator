import numpy as np
import matplotlib.pyplot as plt

# Collar
# Long Stock; Buy 1 OTM Put[k1]; Write 1 OTM Call[k2] where k2 < s0 < k1:
s0 = 4           #Initial stock price
k1 = 2;p1 = 5.0 #Buy 1 OTM put strike/premium(p1)
k2 = 6;c1 = 2 #Write 1 OTM call strike/premium(c1)
shares = 100      #100 shares/lot
#Stock price at expiration
sT = np.arange(0, 5*s0 ,1)
#Payoff from long put (k1)
y1 = np.where(k1 > sT,((k1-sT) - p1) * shares, -p1 * shares)
#Payoff from short call
y2 = np.where(sT > k2,((k2-sT) + c1) * shares, c1 * shares)

#Payoff for Butterfly
y = sT*shares + y1 + y2

#Plot
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False) # Top border removed 
ax.spines['right'].set_visible(False) # Right border removed
ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
ax.tick_params(top=False, right=False) # Removes the tick-marks on the RHS

plt.plot(sT,y,lw = 1.5, label = "y")
plt.legend()
plt.show()

print(y)
print(sT)
print(y1)
print(y2)