# FSP - Machine Learning Notebooks

## Overview

This repository contains introductory Python and machine learning examples in Jupyter notebooks. The material progresses from NumPy and Pandas fundamentals to visualization, regression, K-nearest neighbors, and decision trees.

## Contents

| File | Topics and examples |
| --- | --- |
| [Numpy.ipynb](Numpy.ipynb) | NumPy arrays, data types, dimensions, reshaping, indexing, slicing, boolean masks, vectorized operations, aggregation, broadcasting, random numbers, sorting, concatenation, views, copies, and Euclidean distance. |
| [Pandas.ipynb](Pandas.ipynb) | Series and DataFrames, inspection, indexing with `loc` and `iloc`, filtering, sorting, concatenation, merging, reshaping with `melt` and `pivot`, missing values, duplicates, grouping, renaming, and conversion to NumPy. |
| [Data Visualization.ipynb](Data%20Visualization.ipynb) | Matplotlib and Seaborn examples including line, marker, scatter, image, pie, interactive button, and heatmap plots. |
| [Linear Regression (PPT Example).ipynb](Linear%20Regression%20(PPT%20Example).ipynb) | Simple and multiple linear regression, correlation, manually calculated coefficients, predictions, and regression plots. |
| [Linear Regression.ipynb](Linear%20Regression.ipynb) | Linear regression with feature standardization, predictions, MSE, RMSE, MAE, LASSO, Ridge, and metric comparison. |
| [KNNClassification.ipynb](KNNClassification.ipynb) | K-nearest neighbors classification with a small two-feature dataset, accuracy, a new prediction, and class probabilities. |
| [KNN-k.ipynb](KNN-k.ipynb) | Iris classification with feature standardization, a pipeline, and five-fold `GridSearchCV` to select `k` from 1 to 10. |
| [DecisionTree_Tennis.ipynb](DecisionTree_Tennis.ipynb) | Categorical decision-tree classification using label encoding, entropy, tree visualization, and manual predictions. |
| [DecisionTree_Eg1.ipynb](DecisionTree_Eg1.ipynb) | Decision-tree workflow with train/test splitting, CART/Gini training, probabilities, confusion matrix, feature importance, accuracy, and a classification report. |
| [iris.csv](iris.csv) | Local Iris dataset used by the Pandas examples. |

## Requirements

- Python 3
- Jupyter Notebook or VS Code with the Jupyter extension
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Optional Graphviz support is demonstrated in the decision-tree notebooks.

## Suggested Run Order

1. [Numpy.ipynb](Numpy.ipynb)
2. [Pandas.ipynb](Pandas.ipynb)
3. [Data Visualization.ipynb](Data%20Visualization.ipynb)
4. [Linear Regression (PPT Example).ipynb](Linear%20Regression%20(PPT%20Example).ipynb)
5. [Linear Regression.ipynb](Linear%20Regression.ipynb)
6. [KNNClassification.ipynb](KNNClassification.ipynb)
7. [KNN-k.ipynb](KNN-k.ipynb)
8. [DecisionTree_Tennis.ipynb](DecisionTree_Tennis.ipynb)
9. [DecisionTree_Eg1.ipynb](DecisionTree_Eg1.ipynb)

## Workflow

flowchart 
	A[Collect or load dataset] --> B[Explore and visualize data]

	B --> C[Clean and preprocess data]

	C --> D[Select features and target]

	D --> E[Split data into training and testing sets]

	E --> F[Train machine learning model]

	F --> G[Evaluate model performance]

	G --> H{Performance acceptable?}

	H -- No --> I[Tune features or model parameters]

	I --> F

	H -- Yes --> J[Make predictions]
  
	J --> K[Report results]


## Running the Notebooks

Open a notebook in Jupyter or VS Code and run its cells from top to bottom. The notebooks are demonstration-focused and can be explored independently, but later cells may depend on variables created earlier in the same notebook.

Only `iris.csv` is included locally. Some notebooks download example data such as Boston housing, PlayTennis, salary, and flights datasets, so network access may be required.

