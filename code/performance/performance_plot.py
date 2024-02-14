import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("logs/performance_majority.log", header=None, names=["num_ingestors", "duration", "throughput", "avg_response_time"])
df_2 = pd.read_csv("logs/performance_1.log", header=None, names=["num_ingestors", "duration", "throughput", "avg_response_time"])

# calculate median for each number of ingestors
df = df.groupby("num_ingestors").median().reset_index()
df_2 = df_2.groupby("num_ingestors").median().reset_index()

# crete canvas
plt.figure()

plt.plot(df["num_ingestors"], df["throughput"], label="Majority")
plt.plot(df_2["num_ingestors"], df_2["throughput"], label="Single")
plt.xlabel("Number of ingestors")
plt.ylabel("Throughput (messages/s)")
plt.legend()

plt.savefig("logs/performance1.png")

# Plot the data; df in blue, df_2 in red
plt.figure()
plt.plot(df["num_ingestors"], df["avg_response_time"], label="Majority")
plt.plot(df_2["num_ingestors"], df_2["avg_response_time"], label="Single")
plt.xlabel("Number of ingestors")
plt.ylabel("Average response time (s)")
plt.legend()

plt.savefig("logs/performance2.png")






