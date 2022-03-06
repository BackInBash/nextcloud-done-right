import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

dateparse = lambda x: datetime.strptime(x, '%M:%S')

data = pd.read_csv("performance.csv")
data1 = pd.read_csv("performance_default.csv")

fig, ax = plt.subplots()

l1 = ax.plot(data["files"], data["time"])
ax1 = ax.twinx()
l2 = ax1.plot(data1["files"], data1["time"], color='red')

ax.set_xlabel("Uploaded Files")
ax.set_ylabel("Time")

line_labels = ['Default', 'Worker Scale']
fig.legend([l1, l2],     # The line objects
        labels=line_labels,   # The labels for each line
        loc='right',   # Position of legend
        borderaxespad=0.1,    # Small spacing around legend box
        fontsize=10
        )
fig.tight_layout()

plt.savefig("default.png")