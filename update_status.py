import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import july
from july.utils import date_range

mpl.rcParams['font.family'] = 'Hack Nerd Font Mono'
dates = date_range("2025-05-01", "2025-8-31")
data = np.random.randint(0, 2, len(dates))

fig, ax = plt.subplots(nrows=1, ncols=4)

july.month_plot(dates, data, month=5, ax=ax[0])
july.month_plot(dates, data, month=6, ax=ax[1])
july.month_plot(dates, data, month=7, ax=ax[2])
july.month_plot(dates, data, month=8, ax=ax[3])

fig.suptitle("Completed Days", fontsize=16)
plt.savefig("./auto_assets/plot.png", dpi=100)
plt.show()

