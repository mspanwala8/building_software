# Plot 

import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

ttc_bus_delay= pd.read_csv('C:\\Users\\mspan\\Desktop\\Manthan_DSI\\Assignment_3\\PANWALA_MANTHAN_python_assignment2_orig.csv')

# Plot 'Min Delay' and 'Min Gap' against 'Day' using Matplotlib

Min_Delay  = ax.scatter(ttc_bus_delay['Day'], ttc_bus_delay['Min Delay'])
Min_Gap  = ax.scatter(ttc_bus_delay['Day'], ttc_bus_delay['Min Gap'])

# Add title, labels, grid, and legend

ax.set_title('Days vs Minutes Delays and Gaps')
ax.set_xlabel('Days')
ax.set_ylabel('Minutes')
ax.set_axisbelow(True)
ax.grid()
ax.legend([Min_Delay, Min_Gap], ['Minutes Delay', 'Minutes Gap'],
          bbox_to_anchor=(1, 0),
          loc='lower left')

plt.savefig('building_software_hw1_plot.pdf')
