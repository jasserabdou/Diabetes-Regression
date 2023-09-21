# Diabetes-Regression Project

## Overview

The Diabetes-Regression project is a data science pipeline designed to tackle a regression problem. It encompasses the following main stages:

1. **Loading the Data:** In this stage, the dataset containing information on 442 diabetes patients, including age, sex, body mass index, average blood pressure, and six blood serum measurements, is loaded into the pipeline.

2. **Exploratory Data Analysis (EDA):** This step involves exploring and analyzing the dataset to gain insights into its characteristics, relationships, and potential patterns.

3. **Building Regression Models:** Various regression models are constructed and evaluated to predict a quantitative measure of disease progression one year after baseline.

4. **Model Evaluation and Hyperparameter Tuning:** The performance of different regression models is assessed, and hyperparameters are fine-tuned to optimize their predictive capabilities.

5. **Saving the Model:** The finalized regression model is saved for later use.

Additionally, a Flask web application has been developed and encapsulated within a Docker image for easy deployment.

## Dataset Information

The dataset contains information on ten baseline variables for 442 diabetes patients. These variables include:

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

The data has been preprocessed, with each of the 10 feature variables mean-centered and scaled by the standard deviation times the square root of `n_samples` (i.e., the sum of squares of each column totals 1).

For more information about the dataset, refer to the [source URL](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

## Model Selection

The regression model was constructed and evaluated on three different algorithms:

1. **Linear Regression**: `LinearRegression()`
2. **Logistic Regression**: `LogisticRegression()`
3. **Random Forest Regressor**: `RandomForestRegressor()`

After rigorous evaluation, the 'Random Forest Regressor' model emerged as the best-performing one.

## Running the Container

To run the container locally, use the following command:

```bash
docker run -p 8000:8000 your-docker-image
```

After running the command, you can access the Flask application at [localhost:8000](http://localhost:8000).

## References

- Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani (2004) "Least Angle Regression," Annals of Statistics (with discussion), 407-499. [Read the paper](https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf).

---
