# Infant Formula Brand Prediction

<img src=https://user-images.githubusercontent.com/64850893/147841407-113eab7f-e03c-413e-b5ff-c27f1a9127cb.jpg width="600" height="500">

## Web App Link: https://infant-brand-prediction.azurewebsites.net/

## 1. Overview

* Forecasted the probability of a caregiver using MJN as their current formula brand with 64% of accuracy.
* Collected over 12k records from the CDP (customer data platform), D2C (Shopify), NITFS (national infant and toddler feeding survey).
* Conducted data cleansing, EDA (exploratory data analysis) and upsampling.
* Implemented multiple ML classification models (Logistic Regression, KNN, Naive Bayes, SVC, Decision Tree, Random Forest, Ensemble), using GridsearchCV to reach the optimal model.
* Built a client facing Web App using flask, html, CSS, Visual Studio Code, Azure.
> Due to NDA (Non-Disclosure Agreement), the dataset has been modified.

## 2. Code and Packages

* Python Version: 3.9

* Packages: pandas, numpy, sklearn, matplotlib, seaborn, flask, pickle

* For Web App deployment requirements: pip install -r requirements.txt

## 3. Objectives

* Investigate the variables that impact a parent's choice for the current infant formula brand.
* Forecast the probability of a caregiver uses MJN as their current product.

## 4. Data Sources

The samples are collected from from multiple internal databases in the data lake, and the time period is from 2019 Jan to 2020 Dec. 


## 5. Methodology

* Dependent variables: Current formula brand.

* Independent variables: Email OR, CTR, coupon redemption rate, enrollment type, enrollment age, baby age, breastfeed type, hospital zone.​

* Machine Learning Models: Logistic Regression, Naive Bayes, KNN, SVC, Decision Tree, Random Forest, Ensemble (Random Forest + Logistic Regression).​

* Upsampling due to the imbalanced dataset.

* Gridsearch to tune the hyperparameters.


## 6. Data Cleaning

### 6.1 Raw Data:

![raw_data](https://user-images.githubusercontent.com/64850893/147840808-e3cf9b32-9c7b-467d-b92f-c51befe52e16.jpg)

### Variables intepretation:
* Current brand: "1" represents our brand, and other values represent other brands.
* First purchase brand: "1" represents our brand, and other values represent other brands.
* Email OR (open rate): the nubmer of emails opened/the number of emails have been sent to a person.
* Email CTR (open rate): the nubmer of emails clicked/the number of emails have been sent to a person.
* Coupon redemption rate: the nubmer of coupon redeemed/the number of couponss have been sent to a person.
* Enrollment type: the source from which a person enrolled to our program (Self Enrollment, Co-registered).
* Enrollment age: the age of the baby when the parent enrolled in our program.
* Baby age: the age of the babay when the parent took the survey.
* Breastfeed type: "1" represents breastfed only, "2" represents both breastfed and formula feed, "3" represents formula feed only, "4" represents neither.
* Hospital zone: "1" represents our hospital zone, and other values represent other brands.

### 6.3 Cleansing procedures

* Remove the records with “null” value.
* Manipulate certain columns. (e.g. set the ones with current brand as our brand equal to 1 , other brands as 0).
* Create dummy variables.

![clean_data](https://user-images.githubusercontent.com/64850893/147840830-134fc343-7ef1-4eaa-b1b9-8fdf3a8a3fa0.jpg)


## 7. EDA (Exploratory Data Analysis)

### 7.1 Dependent ariables ("1" as our brand, "0" as other "brands"):

<img src=https://user-images.githubusercontent.com/64850893/147840864-802346af-d44d-4e92-a456-d4b84aee028b.jpg width="500" height="300">

### 7.2 Independent variables:

![indep_var](https://user-images.githubusercontent.com/64850893/147840878-a52f0463-d460-45a3-a1f9-49bc0dd11cd2.jpg)

### 7.3 Correlation：

<img src=https://user-images.githubusercontent.com/64850893/147840888-a99387db-85af-45ec-9160-2f0b889928a9.jpg width="700" height="500">


## 8. Modeling

### 8.1 Process outline

* Minmax scaling
* Train-test-split (cross validation)
* Upsamling
* Machine learning algorithms
  * logistic Regression
  * Naive Bayes
  * KNN
  * SVC
  * Decision Tree
  * Random Forest
  * Ensemble
* GridSearchCV


### 8.2 Model performance:

<img src=https://user-images.githubusercontent.com/64850893/147856515-9e2bed77-06aa-42e2-a3d8-3ca61c7c8e68.jpg width="600" height="400">

* Based on the accuracy comparison, the Random Forest will be selected as the optimal model in this case.

### 8.3 Confusion Matrix (Random Forest): 

<img src=https://user-images.githubusercontent.com/64850893/147841182-b1722ca6-1742-4ab6-8aef-4055104f82d1.jpg width="600" height="400">

### 8.4 Feature Importance (Random Forest): 

<img src=https://user-images.githubusercontent.com/64850893/147841123-150d57b1-107a-402c-8b1d-1c0fc4bc3192.jpg width="600" height="400">

## 9. Key Takeaways

* Applying Random Forest will yield the highest accuracy rate (64%) in terms of predicting a parent's current formula brand. 
* Enrollment age is most significant variable in this model, so attracting consumers to enroll early is critical.
* Email open rate and click through rate are also the important features, and we should make email content more appealing to drive the customers' engagement.

## 10. Web Application Deployment

* Conducted front end development with Visual Studio Code, HTML and CSS.
* Completed back end development using Python and Flask.
* Deployed the web app on Microsoft Azure.
