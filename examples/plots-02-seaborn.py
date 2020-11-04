#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A seaborn example, from:
# https://seaborn.pydata.org/index.html
# https://seaborn.pydata.org/examples/index.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)
plt.show()  # Display the plot
