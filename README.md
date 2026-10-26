# Python — Environment Check & Pandas DataFrame Plot

A small, focused Python script that **verifies a data-science environment** (NumPy, Pandas, Matplotlib, scikit-learn, PyTorch) and then **exercises each core library once**: a NumPy mean, a Pandas DataFrame, a Matplotlib line plot saved to `plot.png`, and a PyTorch tensor sum. It is the quickest way to answer "is my setup working?" before starting a real project, and a compact tour of how the five libraries are imported and used together.

---

## What the Script Does

1. **Imports** NumPy, Pandas, Matplotlib, scikit-learn, and PyTorch — if any import fails, the environment is incomplete.
2. **Prints the version** of each library.
3. **NumPy:** builds an array `[1, 2, 3, 4, 5]` and prints its mean.
4. **Pandas:** builds a DataFrame with columns `X` and `Y` and prints it.
5. **Matplotlib:** plots `Y` against `X` with circle markers, adds a title and axis labels, and saves the figure as `plot.png`.
6. **PyTorch:** builds a tensor `[1.0, 2.0, 3.0]` and prints its sum.

**Example Output** (version numbers will differ on your machine):

```
Numpy version: 2.1.0
Pandas version: 2.2.2
Matplotlib version: 3.9.2
Sklearn version: 1.5.1
PyTorch version: 2.4.0
Numpy array: [1 2 3 4 5] -> Mean: 3.0
Pandas DataFrame:
    X   Y
0  1  10
1  2  20
2  3  30
Plot saved as 'plot.png'.

PyTorch Tensor: tensor([1., 2., 3.]) -> Sum 6.0
```

**Generated file:** `plot.png` — a line chart with three points `(1, 10)`, `(2, 20)`, `(3, 30)` lying on a straight line.

---

## The Code

```python
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
```

---

## The Critical Idea — One Smoke Test Per Library

This script is a **smoke test**: it does not try to do anything deep, only to prove that each library imports and performs one representative operation.

| Library          | Import name         | What is tested                       | Result         |
| ---------------- | ------------------- | ------------------------------------ | -------------- |
| **NumPy**        | `numpy`             | Create an array, compute `.mean()`   | `3.0`          |
| **Pandas**       | `pandas`            | Build a DataFrame from a dictionary  | 3-row table    |
| **Matplotlib**   | `matplotlib.pyplot` | Draw a line plot and save it to disk | `plot.png`     |
| **scikit-learn** | `sklearn`           | Import and print the version only    | Version string |
| **PyTorch**      | `torch`             | Create a tensor, compute `.sum()`    | `6.0`          |

> **Naming note:** the package is installed as `scikit-learn` but imported as `sklearn`. Likewise, Matplotlib is imported twice — `import matplotlib` gives access to `__version__`, while `import matplotlib.pyplot as plt` gives the plotting interface.

---

## How the Plot Works

```python
plt.plot(df["X"], df["Y"], marker='o')
plt.title("Pandas DataFrame Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("plot.png")
```

- **`plt.plot(df["X"], df["Y"], marker='o')`:** draws a line through the points, with a circle marker at each data point. Pandas columns (Series) can be passed straight to Matplotlib.
- **`plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)`:** label the chart and both axes.
- **`plt.savefig("plot.png")`:** writes the figure to the **current working directory**. No window opens, so the script also works on servers and in headless environments.

> **Why no `plt.show()`?** The goal is to save a file, not to display a window. Add `plt.show()` after `savefig` if you want an interactive window as well. Call `savefig` **before** `show`, because `show` can clear the figure.

---

## Algorithm (Pseudocode)

```
import all five libraries
print each library's version

arr  <- [1, 2, 3, 4, 5]
print arr and mean(arr)

df   <- table with X = [1, 2, 3] and Y = [10, 20, 30]
print df

plot Y against X with markers
add title and axis labels
save figure to "plot.png"

t    <- tensor [1.0, 2.0, 3.0]
print t and sum(t)
```

---

## Dry Run

| Step | Operation                     | Value produced                      |
| ---- | ----------------------------- | ----------------------------------- |
| 1    | `arr = np.array([1,2,3,4,5])` | Array of 5 integers                 |
| 2    | `arr.mean()`                  | (1+2+3+4+5) / 5 = **3.0**           |
| 3    | `pd.DataFrame({...})`         | 3 rows × 2 columns                  |
| 4    | `plt.plot(X, Y)`              | Line through (1,10), (2,20), (3,30) |
| 5    | `plt.savefig("plot.png")`     | File `plot.png` created             |
| 6    | `t.sum().item()`              | 1.0 + 2.0 + 3.0 = **6.0**           |

---

## Edge Cases and Common Errors

| Scenario                                                  | Behavior / Fix                                                                          |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| A library is not installed                                | `ModuleNotFoundError` on that import — install it with `pip` (see below) ❌             |
| Importing `sklearn` fails but `scikit-learn` is installed | Check you are using the same Python interpreter for `pip` and for running the script ⚠️ |
| Running on a server with no display                       | Works, because the script only saves a file and never opens a window ✅                 |
| `plot.png` already exists                                 | It is silently **overwritten** ⚠️                                                       |
| Read-only working directory                               | `savefig` raises a `PermissionError` — run from a writable folder ❌                    |
| Running the script repeatedly in one session              | Plots draw onto the same figure unless it is cleared with `plt.close()` ⚠️              |
| PyTorch install is slow or large                          | Expected — PyTorch is by far the heaviest dependency here ⚠️                            |

---

## Code-Quality Notes

**The plot uses `plt.plot`, not `DataFrame.plot`.** The title says "Pandas DataFrame Plot", but the chart is drawn by Matplotlib directly from two columns. The Pandas-native equivalent is `df.plot(x="X", y="Y", marker="o")`, which produces the same line chart.

**No figure cleanup.** `plt.close()` after `savefig` frees the figure. It is harmless in a one-shot script, but good practice if the plotting code is ever reused in a loop or a function.

**scikit-learn is only imported.** It is version-checked but never used, so this script confirms the install, not that any model trains correctly.

**Versions are printed, not enforced.** The script shows what is installed but does not fail on an outdated version. Compare the printed values against your project's requirements by hand.

---

## Repository Structure

```
Python-Environment-Check/
│
├── environment_check.py   # Main Python script
├── plot.png               # Generated when the script runs
└── README.md              # Project documentation
```

---

## How to Install and Run

**Prerequisites:** Python 3.9+ and `pip`

```bash
# Clone the repository
git clone https://github.com/<your-username>/Python-Environment-Check.git
cd Python-Environment-Check

# (Recommended) create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the dependencies
pip install numpy pandas matplotlib scikit-learn torch

# Run
python3 environment_check.py
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
pip install numpy pandas matplotlib scikit-learn torch
python environment_check.py
```

> **Tip:** the default `pip install torch` build is fine for this script. If you need GPU support, use the install command for your CUDA version from the [PyTorch website](https://pytorch.org/get-started/locally/).

---

## Key Concepts Covered

- **Environment verification** — import every dependency and print its `__version__`
- **NumPy arrays** — create an array and use the `.mean()` method
- **Pandas DataFrames** — build a table from a dictionary of columns
- **Matplotlib plotting** — line plot, markers, title, axis labels, and `savefig`
- **Headless plotting** — saving to a file instead of opening a window
- **PyTorch tensors** — create a tensor and reduce it with `.sum()` and `.item()`
- **Package vs. import names** — `scikit-learn` is installed, `sklearn` is imported

---

## Why This Matters in a Data / ML Workflow

These five libraries form the standard Python data-science stack, and each builds on the previous one:

| Library          | Role in a typical workflow                                             |
| ---------------- | ---------------------------------------------------------------------- |
| **NumPy**        | Fast numeric arrays — the foundation everything else is built on       |
| **Pandas**       | Loading, cleaning, and transforming tabular data                       |
| **Matplotlib**   | Visualizing data and results                                           |
| **scikit-learn** | Classical machine learning: regression, classification, clustering     |
| **PyTorch**      | Deep learning with tensors, automatic differentiation, and GPU support |

Running a script like this first catches missing packages and broken installs **before** they interrupt a longer project.

---

## Contributing

Contributions are welcome. Consider adding:

- A **`requirements.txt`** with pinned versions
- A check for **GPU availability** (`torch.cuda.is_available()`)
- A **tiny scikit-learn model** (for example, `LinearRegression` on the same `X` and `Y`) to confirm it works end to end
- The Pandas-native version using `df.plot(...)`
- `plt.close()` and a `main()` function with an `if __name__ == "__main__":` guard
- Graceful error messages when an import fails

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# Then open a Pull Request
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

_A quick sanity check for your Python data-science stack — verify first, build second._
