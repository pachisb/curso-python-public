#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Matplotlib example, from:
# https://matplotlib.org/

import math
import numpy as np
import matplotlib.pyplot as plt

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 3.1416 * 2, 11)
x = np.linspace(0, 3.1416 * 2, 99)  # línea más "precisa"
# print(x)
plt.plot(x, np.sin(x))  # Plot the sine of each x point

# Alternativa: lo mismo pero "a mano" (sin usar numpy)
x = [0.0, 0.2992, 0.5984, 0.8976, 1.1968, 1.496, 1.7952, 2.0944, 2.3936, 2.6928, 2.992,
     3.2912, 3.5904, 3.8896, 4.1888, 4.488, 4.7872, 5.0864, 5.3856, 5.6848, 5.984, 6.2832]
y = []
for n in x:
     y.append(math.sin(n))
# print(y)
plt.plot(x, y)  # Plot the sine of each x point

plt.show()  # Display the plot
