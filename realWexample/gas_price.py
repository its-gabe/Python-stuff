import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gas = pd.read_csv(r'Python-stuff\gas_prices.csv')

plt.title('Gas Price over time (in USD)')

# for countries in gas:
#     if countries != 'Year':
#         plt.plot(gas['Year'], gas[countries])
plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas.Year, gas['Australia'], marker='.', label='Australia')
plt.xlabel('Year')
plt.ylabel('US Dollar')
plt.xticks(gas.Year[::3])
plt.legend()
plt.show()
