# FSP - Machine Learning Notebooks

## Overview

This repository contains introductory Python, machine learning, and Streamlit examples. The material progresses from NumPy and Pandas fundamentals to visualization, regression, classification, clustering, model evaluation, model persistence, and small interactive web apps.

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
| [KNNClassification-Pickle.ipynb](KNNClassification-Pickle.ipynb) | KNN win/loss classification, predictions, and saving/loading the trained classifier with `pickle`. |
| [DecisionTree_Tennis.ipynb](DecisionTree_Tennis.ipynb) | Categorical decision-tree classification using label encoding, entropy, tree visualization, and manual predictions. |
| [DecisionTree_Eg1.ipynb](DecisionTree_Eg1.ipynb) | Decision-tree workflow with train/test splitting, CART/Gini training, probabilities, confusion matrix, feature importance, accuracy, and a classification report. |
| [KMeans_Cust_Seg.ipynb](KMeans_Cust_Seg.ipynb) | Customer segmentation with K-Means, exploratory statistics, income/spend distributions, violin plots, scatter plots, and cluster visualization. |
| [ROC Error Analysis.ipynb](ROC%20Error%20Analysis.ipynb) | Binary and multiclass classification evaluation using predicted probabilities, confusion matrices, ROC curves, AUC, and error analysis. |
| [iris.csv](iris.csv) | Local Iris dataset used by the Pandas examples. |

### Python and Streamlit apps

| File | Topics and examples |
| --- | --- |
| [K-NN.py](K-NN.py) | Streamlit win/loss prediction app that loads `trained_model.sav` and predicts from two input variables. |
| [prog.py](prog.py) | Streamlit basics: titles, text, Markdown, messages, exceptions, help, and displaying image, audio, and video files. |
| [prog2.py](prog2.py) | Streamlit text, text area, number, date, time, and color-picker input controls. |
| [prog3.py](prog3.py) | Streamlit button, checkbox, radio, select box, multiselect, slider, and select-slider controls. |

### Supporting files

| File | Purpose |
| --- | --- |
| [trained_model.sav](trained_model.sav) | Pickled KNN classifier loaded by `K-NN.py` and recreated by `KNNClassification-Pickle.ipynb`. |
| [plot1.png](plot1.png) | Image displayed by `prog.py`. |
| [rain.mp4](rain.mp4) | Video displayed by `prog.py`. |
| [Tune1.aac](Tune1.aac) | Audio clip displayed by `prog.py`. |

## Requirements

- Python 3
- Jupyter Notebook or VS Code with the Jupyter extension
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `streamlit` (for the Python apps)
- `Pillow` (for the image example in `prog.py`)

Optional Graphviz support is demonstrated in the decision-tree notebooks.

## Suggested Run Order

1. [Numpy.ipynb](Numpy.ipynb)
2. [Pandas.ipynb](Pandas.ipynb)
3. [Data Visualization.ipynb](Data%20Visualization.ipynb)
4. [Linear Regression (PPT Example).ipynb](Linear%20Regression%20(PPT%20Example).ipynb)
5. [Linear Regression.ipynb](Linear%20Regression.ipynb)
6. [KNNClassification.ipynb](KNNClassification.ipynb)
7. [KNN-k.ipynb](KNN-k.ipynb)
8. [KNNClassification-Pickle.ipynb](KNNClassification-Pickle.ipynb)
9. [DecisionTree_Tennis.ipynb](DecisionTree_Tennis.ipynb)
10. [DecisionTree_Eg1.ipynb](DecisionTree_Eg1.ipynb)
11. [KMeans_Cust_Seg.ipynb](KMeans_Cust_Seg.ipynb)
12. [ROC Error Analysis.ipynb](ROC%20Error%20Analysis.ipynb)

## Workflow

flowchart 
    A[Collect or load dataset] --> B[Explore and visualize data]

    B --> C[Clean and preprocess data]

    C --> D[Select features and target]

    D --> E[Split into training and testing sets]

    E --> F[Train machine learning model]

    F --> G[Evaluate model performance]

    G --> H{Performance acceptable?}

    H -- No --> I[Tune features or model parameters]

    I --> F

    H -- Yes --> J[Make predictions]

    J --> K[Report results]
	

## Running the Notebooks

Open a notebook in Jupyter or VS Code and run its cells from top to bottom. The notebooks are demonstration-focused and can be explored independently, but later cells may depend on variables created earlier in the same notebook.

`iris.csv` and the serialized model are included locally. Some notebooks download or expect additional example data such as Boston housing, PlayTennis, salary, flights, and `CLV.csv`, so network access or local dataset configuration may be required. In `KMeans_Cust_Seg.ipynb`, update the dataset path from `e:\datafile\CLV.csv` to the location of your customer dataset before running it.

## Running the Streamlit Apps

Install the requirements, then run an app from the repository directory:

```bash
streamlit run prog.py
streamlit run prog2.py
streamlit run prog3.py
streamlit run K-NN.py
```

Run `K-NN.py` from the same directory as `trained_model.sav`. Its two inputs should be numeric values corresponding to the variables used to train the saved KNN model.

