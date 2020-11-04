#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Matplotlib example, from:
# https://matplotlib.org/

import numpy as np
import matplotlib.pyplot as plt

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 3.1416 * 2, 11)
plt.plot(x, np.sin(x))  # Plot the sine of each x point
plt.show()  # Display the plot
