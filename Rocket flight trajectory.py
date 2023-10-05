import numpy as np
import matplotlib.pyplot as plt
from func import integrateGraph
plt.style.use('dark_background')

#variables

totalMass = 1
dry = 0.9
burnTime = 3.5
totalImpulse = 50
propellantMass = 0.064
avaregeThrust = totalImpulse/burnTime
massFlowRate = propellantMass/burnTime

time = np.linspace(0 , 10, 100, False)

index = int(np.where(time==burnTime)[0]+1)
thrust = np.append(np.repeat(avaregeThrust, index), np.repeat(0, len(time)-index))
mass = no.append(np.repeat(totalMass, index)-time[0:index]*massFlowRate, np.repeat(dryMass, len(time)-index))
acceleration = thrust/mass - 9.81
velocity = integrateGraph(time, acceleration)
displacement = integrateGraph(time, velocity)

plt.plot(time, acceleration)
plt.plot(time, velocity)
plt.plot(time, displacement)
plt.show()

