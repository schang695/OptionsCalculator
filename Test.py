import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

print("start")
strategy = input("Butterfly or Condor: ")
print(strategy, "Long Call Strategy")

if strategy == "Butterfly":
    print("Buy ITM Call\nWrite 2 ATM Call\nBuy OTM Call\nWhere k3 > k2 > k1, c1 > c2 > c3")
    shares = 100
    while True:
        s0 = float(input("Current Stock Price [s0]: "))
        if s0 < 0:
            print("s0 must be positive, try again")
            continue
        k1 = float(input("ITM Call Stike Price [k1]: "))
        k2 = s0
        print("ATM Call Strike Price [k2]: ", s0)
        if k1 > k2:
            print("k2 must be greater than k1, try again")
            continue
        k3 = float(input("OTM Call Stike Price [k3]: "))
        if k2 > k3:
            print("k3 must be greater than k2, try again")
            continue
        c1 = float(input("ITM Call Premium [c1]: "))
        c2 = float(input("ATM Call Premium [c2]: "))
        if c2 > c1:
            print("c2 must be smaller than c1, try again")
            continue
        c3 = float(input("OTM Call Premium [c3]: "))
        if c3 > c2:
            print("c3 must be smaller than c2, try again")
            continue
        else:
            break
    sT = np.arange(0, 2*s0 ,2)
    y1 = np.where(sT > k1,((sT-k1) - c1) * shares, -c1 * shares)
    y2 = np.where(sT > k2,((k2-sT) + c2) * shares * 2, c2 * shares * 2)
    y3 = np.where(sT > k3,((sT-k3) - c3) * shares, -c3 * shares)
    y = y1 + y2 + y3
    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False) # Top border removed 
    ax.spines['right'].set_visible(False) # Right border removed
    ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
    ax.tick_params(top=False, right=False) # Removes the tick-marks on the RHS

    plt.plot(sT,y,lw = 1.5, label = "y")
    plt.legend()
    plt.show()

        
elif strategy == "Condor":
    s0 = float(input("Current Stock Price: ")) 
    k1 = float(input("Buy ITM Call Stike Price: "))
    c1 = float(input("ITM Call Premium: "))
    k2 = float(input("Write ITM Call Stike Price: "))
    c2 = float(input("OTM Call Premium: "))
    k3 = float(input("BuyOTM Call Stike Price: "))
    c3 = float(input("OTM Call Premium: "))
    