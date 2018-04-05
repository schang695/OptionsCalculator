import numpy as np
import matplotlib.pyplot as plt

print("Options Strategy Calculator/Grapher")
risk_pro_list = ("Bull", "Bear", "Neutral", "Volatile") #Risk Profile
risk_pro = input("Risk Profile [Bull, Bear, Neutral, Volatile]: ").upper()
print("Risk Profile:", risk_pro.title())
if risk_pro == "NEUTRAL": #Neutral Strats: Collar, Short Straddle, Short Strangle, Condor, Calendar Spread, Butterfly Spread
    strategy_neut = input("Butterfly | Condor | Collar: ").upper()
    print(strategy_neut)
    if strategy_neut == "BUTTERFLY": 
        print("Buy ITM Call\nWrite 2 ATM Call\nBuy OTM Call\nWhere k3 > k2 > k1, c1 > c2 > c3")
        shares = 100
        while True:
            s0 = float(input("Current Stock Price [s0]: "))
            if s0 < 0:
                gprint("Error: s0 must be positive, try again.")
                continue
            k1 = float(input("ITM Call Stike Price [k1]: "))
            k2 = s0
            print("ATM Call Strike Price [k2]:",float(s0))
            if k1 >= k2:
                print("Error: k2 must be greater than k1, try again.")
                continue
            k3 = float(input("OTM Call Stike Price [k3]: "))
            if k2 >= k3:
                print("Error: k3 must be greater than k2, try again.")
                continue
            c1 = float(input("ITM Call Premium [c1]: "))
            c2 = float(input("ATM Call Premium [c2]: "))
            if c2 >= c1:
                print("Error: c2 must be smaller than c1, try again.")
                continue
            c3 = float(input("OTM Call Premium [c3]: "))
            if c3 >= c2:            
                print("Error: c3 must be smaller than c2, try again.")
                continue
            else:
                break

        sT = np.arange(0, 2*s0 ,1)
        y1 = np.where(sT > k1,((sT-k1) - c1) * shares, -c1 * shares) #Payoff of k1
        y2 = np.where(sT > k2,((k2-sT) + c2) * shares * 2, c2 * shares * 2) #Payoff of k2
        y3 = np.where(sT > k3,((sT-k3) - c3) * shares, -c3 * shares) #Payoff of k3
        y = y1 + y2 + y3 #Payoff of Butterfly
        fig, ax = plt.subplots()
        ax.spines['top'].set_visible(False) # Top border removed 
        ax.spines['right'].set_visible(False) # Right border removed
        ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
        ax.tick_params(top=False, right=False) # Removes the tick-marks on the RHS


        plt.plot(sT,y,lw = 1.5, label = "y")
        plt.title('Long Call Butterfly') 
        plt.xlabel('Stock Prices')
        plt.ylabel('Profit/loss')
        plt.legend()
        plt.show()

    elif strategy_neut == "CONDOR":
        print("Buy 1 ITM Call\nWrite 1 ITM Call\nWrite 1 OTM Call\nBuy 1 OTM Call\nWhere k4 > k3 > k2 > k1 (k2-k1 = k4-k3); c1 > c2 > c3 > c4")
        shares = 100
        while True:
            s0 = float(input("Current Stock Price [s0]: "))
            if s0 <= 0:
                print("Error: s0 must be positive, try again.")
                continue
            k1 = float(input("Buy ITM Call Stike Price [k1]: "))
            if s0 <= k1:
                print("Error: s0 must be greater than k1, try again.")
            k2 = float(input("Write ITM Call Stike Price [k2]: "))
            if k2 <= k1 or k2==s0:
                print("Error: k2 must be greater than k1, try again.")
                continue
            k3 = float(input("Write OTM Call Stike Price [k3]: "))
            if k3 <= k2:
                print("Error: k3 must be greater than k2, try again.")
            k4 = float(input("Buy OTM Call Strike Price [k4]: "))
            if k4 <= k3:
                print("Error: k4 must be greater than k3, try again.")
                continue
            if k2-k1 != k4-k3:
                print("Error: k2-k1 must be equal to k4-k3, try again.")
                continue
            else:
                break
        while True:
            c1 = float(input("ITM Call Premium [c1]: "))
            c2 = float(input("ITM Call Premium [c2]: "))
            if c1 <= c2:
                print("Error: c2 must be greater than c1, try again.")
                continue
            c3 = float(input("OTM Call Premium [c3]: "))
            if c2 <= c3:
                print("Error: c1 must be greater than c3, try again.")
                continue
            c4 = float(input("OTM Call Premium [c4]: "))
            if c3 <= c4:
                print("Error: c3 must be greater than c4, try again.")
                continue
            else:
                break

        sT = np.arange(0, 2*s0 ,1)
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
        fig, ax = plt.subplots()
        ax.spines['top'].set_visible(False) #Remove top border
        ax.spines['bottom'].set_position('zero') # Set X-axis in the center
        plt.plot(sT,y,lw = 1.5, label = "y")
        plt.show()
    
    elif strategy_neut == "COLLAR":
        print("Long Stock; Buy 1 OTM Put[k1]; Write 1 OTM Call[k2]\nWhere k1 < s0 < k2")
        shares = 100
        while True:
            s0 = float(input("Current Stock Price [s0]: "))
            if s0 <= 0:
                print("Error: s0 must be positive, try again.")
                continue
            k1 = float(input("Buy OTM Put Stike Price [k1]: "))
            if s0 <= k1:
                print("Error: k1 must be greater than s0, try again.")
                continue
            k2 = float(input("Write OTM Call Stike Price [k2]: "))
            if k2 <= s0:
                print("Error: k2 must be greater than s0, try again.")
                continue
            else:
                break
        p1 = float(input("OTM Put Premium [p1]: "))
        c1 = float(input("OTM Call Premium [c1]: "))

        #Stock price at expiration
        sT = np.arange(0, 2*s0 ,1)
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
