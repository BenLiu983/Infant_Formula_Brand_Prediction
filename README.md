# Infant Formula Brand Prediction
Predicting consumers' current brand choice by Machine Learning algorithms

## 1. Overview

* Forecasted the probability of a caregiver uses MJN as their formula brand with 66% of accuracy.
* Collected over 12k records from the CDP (customer data platform), D2C (Shopify), NITFS (national infant and toddler feeding survey).
* Conducted data cleansing, EDA (exploratory data analysis) and upsampling
* Implemented multiple ML classification models (Logistic Regression, KNN, Naive Bayes, SVC, Decision Tree, Random Forest, Ensemble) using Gridsearch to reach the optimal model.
* Built a client facing Web App using flask, html, CSS, Azure.

** Due to NDA (Non-Disclosure Agreement), the dataset has been modified.


# 2. Objectives

* Investigate the variables that impact a parent's choice for the current infant formula brand.
* Forecast the probability of a caregiver uses MJN as their current product.


# 3. Data Sources

The samples are collected from from multiple internal databases in the data lake, and the time period is from 2019 Jan to 2020 Dec. 


# 4. Methodology

* Dependent variables: current formula brand.

* Independent variables: Email OR, CTR, coupon redemption rate, enrollment type, enrollment age, baby age, breastfeed type, hospital zone.​

* Machine Learning Models: Logistic regression, decision tree, Artificial Neural Network.​

# 5. Raw Data

Note that the dataset has been modified and resamples due to the non-disclosure agreement.

The following dataset is from different tables in the data lake and survey data, and the time period is from 2019 Jan to 2020 Dec.

![image](https://user-images.githubusercontent.com/64850893/135674163-5a02499b-76e9-4add-b6ee-68105cad432e.png)


## Variable intepretation:
* Current brand: "1" represents our brand, and other values represent other brands.
* First purchase brand: "1" represents our brand, and other values represent other brands.
* Email OR (open rate): the nubmer of emails opened/the number of emails have been sent to a person
* Email CTR (open rate): the nubmer of emails clicked/the number of emails have been sent to a person
* Coupon redemption rate: the nubmer of coupon redeemed/the number of emails have been sent to a person
* Enrollment type: the source from which a person enroll to our program (Digital Self Enrollment, Co-registered)
* Enrollment age: the age of the baby when the parent enrolled in our program
* Baby age: the age of the babay when the parent took the survey 
* Breastfeed type: "1" represents breastfed only, "2" represents both breastfed and formula feed, "3" represents formula feed only, "4" represents neither.
* Hospital zone: "1" represents our hospital zone, and other values represent other brands.


# 6. Data cleaning

* Remove the records with “null” value.
* Manipulate certain columns. (e.g. set the ones with current brand as our brand equal to 1 , other brands as 0).

![image](https://user-images.githubusercontent.com/64850893/135674873-f071c940-9765-414c-8cca-a9165718165d.png)

# 7. EDA (Exploratory Data Analysis)

## Dependent ariables ("1" as our brand, "0" as other "brands"):

![image](https://user-images.githubusercontent.com/64850893/135921753-71200654-e635-411f-a587-339514dd20ee.png)

Note: "1" as our brand, "0" as other "brands".

## Independent variables :

![image](https://user-images.githubusercontent.com/64850893/135923401-28312897-4d1b-4d9f-a87e-a16c4894236d.png)

Note: 
For "enrollment type" - "1" for self-enrolled, "0" for co-registered;
For "breastfeed" type -  "1" for formula feed, "0" for breast feed;
For "Zone" - "1" for our hospital zone, "0" for other brands' hospital zone.
