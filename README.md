FSP — Machine Learning (Notebooks)

Overview

This workspace contains two Jupyter notebooks used for a foundational ML workshop focused on NumPy and Pandas examples.

Files

- FSP_Day1.ipynb — NumPy examples: array creation, reshaping, indexing, boolean indexing, array math, random numbers, concatenation/stacking, views vs copies.
- FSP_Day_2.ipynb — Pandas examples: Series and DataFrame creation, concatenation, merging, indexing, filtering, sorting, reshaping (melt/pivot), descriptive stats, and reading `iris.csv`.
- iris.csv — Iris dataset used for examples (loaded in Day 2 notebook).

Recommended Sections (match notebooks)

- Environment & Setup
  - Imports: `numpy`, `pandas`
  - Data: `iris.csv`

- NumPy
  - Array creation (`np.array`, `np.arange`, `np.linspace`, `np.logspace`)
  - Special arrays (`np.zeros`, `np.ones`)
  - Reshaping & dimensions (`reshape`, `shape`, `ndim`)
  - Indexing & slicing
  - Boolean indexing & masks
  - Vectorized operations & ufuncs
  - Aggregation & statistics
  - Random numbers and seeds
  - Concatenation & stacking
  - Views vs copies

- Pandas
  - `Series`: creation, index, access
  - `DataFrame`: creation from lists/dicts
  - Concatenation (`pd.concat`) and merge (`pd.merge`)
  - Inspection: `head`, `info`, `describe`, `dtypes`
  - Selection & filtering (`loc`, `iloc`, boolean masks)
  - Sorting & reindexing
  - Reshaping: `melt`, `pivot`
  - Conversion to NumPy (`to_numpy`, `.values`)

How to use

Open the notebooks in Jupyter or VS Code and run cells sequentially. The notebooks are demonstration-focused; feel free to modify examples to explore behavior.

