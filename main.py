import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 30 year bond, coupon rate, 3.5%, yield 5%

#calculate duration
price = -npf.pv(0.05,30,3.5,100)
price_up = -npf.pv(0.06,30,3.5,100)
price_down = -npf.pv(0.04,30,3.5,100)

duration = (price_down-price_up)/(2*price*0.01)

dollar_duration = duration*price*0.01

dv01 = duration*price*0.0001

#calculate convexity

convexity = (price_down+price_up-(2*price))/(price*0.01**2)

#high maturity, low coupon, low yield result in highest convexity

dollar_convexity = convexity*price*(0.01**2)

convexity_adjustment = 0.5 * dollar_convexity * (100**2) * (0.01**2)

# combine duration and convexity to preduct bond price change, convexity adjustment helps capture the curvature of the bond price/yield relationship

combined_prediction = -100*dollar_duration*0.01 + convexity_adjustment



#determining bond convexity w/ various yields ->as yield increases, convexity decreases

bond_yields = np.arange(0,20,0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])
bond['price'] = -npf.pv((bond['bond_yield']/100),30,3.5,100) #actual bond price for each level of yield
bond['price_up'] = -npf.pv((bond['bond_yield']/100)+0.01,30,3.5,100)
bond['price_down'] = -npf.pv((bond['bond_yield']/100)-0.01,30,3.5,100)
bond['convexity'] = (bond['price_down'] + bond['price_up'] - 2 * bond['price']) / (bond['price'] * 0.01 ** 2)

print(bond)
plt.plot(bond['bond_yield'],bond['convexity'])
plt.xlabel('Yield (%)')
plt.ylabel('Convexity')
plt.show()
