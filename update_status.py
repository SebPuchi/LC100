import numpy as np
import matplotlib.pyplot as plt
import july
from july.utils import date_range

dates = date_range("2020-01-01", "2020-12-31")
data = np.random.randint(0, 14, len(dates))

# GitHub Activity like plot (for someone with consistently random work patterns).
july.heatmap(dates, data, title='Github Activity', cmap="github")
plt.show()

# Month plot with dates.
july.month_plot(dates, data, month=5, date_label=True)
# Month plot with values.
july.month_plot(dates, data, month=6, value_label=True)
july.month_plot(dates, data, month=7, value_label=True)
plt.show()
