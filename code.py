import numpy as np
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import sklearn
import torch

print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Sklearn version:", sklearn.__version__)
print("PyTorch version:", torch.__version__)

arr = np.array([1, 2, 3, 4, 5])
print("Numpy array:", arr, "-> Mean:", arr.mean())

df = pd.DataFrame({"X": [1, 2, 3], "Y": [10, 20, 30]})
print("Pandas DataFrame:\n", df)

plt.plot(df["X"], df["Y"], marker='o')
plt.title("Pandas DataFrame Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("plot.png")
print("Plot saved as 'plot.png'.")

t = torch.tensor([1.0, 2.0, 3.0])
print("\nPyTorch Tensor:", t, "-> Sum", t.sum().item())
