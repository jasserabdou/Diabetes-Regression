# Diabetes-Regression Project

## Overview

The Diabetes-Regression project is a comprehensive data science pipeline designed to address a regression problem. It encompasses the following key stages:

1. **Loading the Data:** This initial stage involves importing a dataset containing information on 442 diabetes patients, including age, sex, body mass index, average blood pressure, and six blood serum measurements.

2. **Exploratory Data Analysis (EDA):** Here, the dataset is thoroughly explored and analyzed to gain valuable insights into its characteristics, relationships, and potential patterns.

3. **Building Regression Models:** Various regression models are constructed and evaluated to predict a quantitative measure of disease progression one year after the baseline.

4. **Model Evaluation and Hyperparameter Tuning:** The performance of different regression models is rigorously assessed, and hyperparameters are fine-tuned to optimize their predictive capabilities.

5. **Saving the Model:** The finalized regression model is saved for later use.

In addition, a Flask web application has been developed and encapsulated within a Docker image for seamless deployment.

## Dataset Information

The dataset provides information on ten baseline variables for 442 diabetes patients. These variables include:

- `age`: Age in years
- `sex`: Gender
- `bmi`: Body mass index
- `bp`: Average blood pressure
- `s1`: Total serum cholesterol (tc)
- `s2`: Low-density lipoproteins (ldl)
- `s3`: High-density lipoproteins (hdl)
- `s4`: Total cholesterol / HDL (tch)
- `s5`: Possibly log of serum triglycerides level (ltg)
- `s6`: Blood sugar level (glu)

The target variable is a quantitative measure of disease progression one year after baseline.

### Data Set Characteristics:

- Number of Instances: 442
- Number of Attributes: First 10 columns are numeric predictive values
- Target: Column 11 is a quantitative measure of disease progression one year after baseline

The data has undergone preprocessing, with each of the 10 feature variables mean-centered and scaled by the standard deviation times the square root of `n_samples` (i.e., the sum of squares of each column totals 1).

For further details about the dataset, please refer to the [source URL](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

## Model Selection

The regression model was constructed and evaluated using three different algorithms:

1. **Linear Regression**: `LinearRegression()`
2. **Logistic Regression**: `LogisticRegression()`
3. **Random Forest Regressor**: `RandomForestRegressor()`

After rigorous evaluation, the 'Random Forest Regressor' model emerged as the best-performing one.

## Running the Container

To run the container locally, use the following command:

```bash
docker pull ghcr.io/jasserabdou/diabetesregression:latest
docker run -p 5000:5000 ghcr.io/jasserabdou/diabetesregression:latest
```

After executing the command, you can access the Flask application at [localhost:8000](http://localhost:8000).

## References

- Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani (2004) "Least Angle Regression," Annals of Statistics (with discussion), 407-499. [Read the paper](https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf).
