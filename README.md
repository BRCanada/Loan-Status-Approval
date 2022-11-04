# Mini-project IV
## Brandon Rose
### [Assignment](assignment.md)

## Project/Goals
The goal for this project is to create and train a model that will predict loan status approval. The model is to be run on the cloud and queried using the *requests* package from a local machine. The model will return it's prediction in json format.

## Hypothesis
It is my hypothesis that Males will get higher amounts and more frequent approvals compared to females. I plan to look for signs of this in EDA.

## EDA 
While exploring the dataset, I found that there was a much larger male representation across the whole dataset. With some basic data visualization I found that around 62% of approved loans were male applicants, and an even greater 80% of denied applications were male as well.

[Approved Loans by Profile](images/Approved_Loans_by_Profile_pie.png)

[Denied Loans by Profile](images/Denied_Loans_by_Profile_pie.png)
<br>
<br>
Some violin charts showed me that a larger portion of the female applicants are graduated, and those that aren't graduated represent a small portion of the ungraduated male population. There was also some interesting insight on the female violin, where a small number were ungraduated, yet in the 15000-20000 income range. [Education Violin](images/gender_education_violin.png)
<br>
<br>
While exploring the violins, I also noticed there were more males with a loan application approved than those with a denied application. For the females it was the opposite. [Loan Approval Violin](images/gender_loanstatus_violin.png)

## Process
I did the following steps in my process:
### Step 1: EDA
* Isolate Loan_Approval column for use in train/test data as target.
* Remove Loan_Id column as it is not needed for predictions
* Use pivot tables to grab different insights based on the categorical feature chosen for the index
    * Make some data visualizations (as seen above) on my pivot tables.

### Step 2: Feature Engineering
* Create more features based on original dataset:
    * Profile categorical feature from Gender, Marital Status, and Education
    * Created a CombinedIncome feature based on Applicant and Co-Applicant income.
    * Made logarithmic transformation columns for both income features.
    * One Hot Encoded my categorical variables.

### Step 3: Preliminary Model Training
* Split the X and y datasets
* Use RandomForestClassifier 
* Defined parameters to run through a Grid Search CV
* Fit X_train, y_train to GridSearch with the RFC model and parameters.

### Step 4: Pipeline
* Incorporate steps 2 and 3 into a pipeline, start by separating numerical and categorical.
* **Numerical**:
    * FunctionTransformer
    * SimpleImputer
* **Categorical**:
    * FunctionTransformer
    * SimpleImputer
    * OneHotEncoder
* Run both pipelines through a ColumnTransformer named preprocess
* Create final pipeline, preprocess first, RFC second.
* Replace data in GridSearchCV with pipeline, include parameters. 
* Fit the X_Train and y_train data

### Step 5: Pickle and Ship
* Pickle trained GridSearchCV with RFC model 
* Upload to EC2 AWS instance at
    * http://ec2-18-191-164-122.us-east-2.compute.amazonaws.com:4242/
* Run mp4_app.py from EC2 Terminal

### Step 6: Predict
* Query AWS app with a random row from test data
    * Row is selected and converted to dictionary
    * dictionary is used in EC2 request line
    * Prediction is returned

## Results/Demo
My first test of the api was accurate.

## Challanges 
I struggled with transforming some of my functions to be used properly in Pipeline, as I learned later that using pandas methods is incompatible with Pipeline. The final model is simplified, unfortunately. 

## Future Goals
I would like to rewrite the feature engineering functions in [instructions](notebooks/instructions.ipynb) to be compatible with my Pipeline, so I can see the accuracy difference with additional engineered features.

