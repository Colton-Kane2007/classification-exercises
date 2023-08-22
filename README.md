# Classification Project
# Project description with goals:
* This is a notebook where I analyze drivers of churn within the telco_churn dataset from MySQL. Using the data science pipeline, I grab the data, prepare it, explore it, visualize it, train models on it, and use statistical testing in order to answer questions about the data.


# Initial hypotheses and/or questions I have of the data, ideas:
* The main question I'm asking of the data is 'What are the main drivers of churn?' and subsequently 'What actions could I recommend to a stakeholder in order to reduce churn?'
* More specifically, my initial hypothesis is that the shorter contract term is the biggest driver in churn, because people paying month-to-month can leave any time.

# Data Dictionary:
|Feature|Dtype|
|:--------|:-----------|
|payment_type_id|	int64, numerical version of payment type, respectively|
|internet_service_type_id|	int64, numerical version of internet service type, respectively|
|contract_type_id|	int64, numerical version of contract type, respectively|
|customer_id|	object, customer ID|
|gender|	object, male or female|
|senior_citizen|	int64, yes or no|
|partner|	object, yes or no|
|dependents| object, yes or no|
|tenure|	int64, tenure length|
|phone_service|	object, phone service or not|
|multiple_lines|	object, yes or no|
|online_security|	object, yes or no|
|online_backup|	object, yes or no|
|device_protection|	object, yes or no|
|tech_support|	object, yes or no|
|streaming_tv|	object, yes or no|
|streaming_movies|	object, yes or no|
|paperless_billing|	object, yes or no|
|monthly_charges|	float64, monthly charge per customer|
|total_charges|	object, total charge per customer|
|churn|	object, yes or no|
|contract_type|	object, month-to-month, one year, two year|
|internet_service_type|	object, dsl, fiber optic, none|
|payment_type|	object, electronic check, mailed check, credit card|


# Project planning:
* Aquire data from MySQL
 
* Prepare data
   * Create Engineered columns from existing data
       * churn
       * gender
       * partner
       * dependents
       * phone_service
       * paperless_billing
 
* Explore data in search of drivers of churn
   * Answer the following initial questions
       * Does a month-to-month contract lead to higher rate of churn?
       * How often has churn occured compared to no churn?
       * Does gender affect churn?
       * Does whether the customer has a partner affect churn?
       * Does whether the customer has dependents affect churn?
       * Does phone service type affect churn?
       * Does whether the customer uses paperless billing affect churn?
      
* Develop a Model to predict if a customer will churn
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data



# Instructions or an explanation of how someone else can reproduce my project and findings (What would someone need to be able to recreate my project on their own?):
* In order to recreate this project, another user would need similar acquire and prepare files, and a MySQL account to log in, with the credentials in your acquire file.


# Key findings, recommendations, and takeaways from my project:
* My main takeaway is that the data shows a correlation between higher rates of churn and customers with month-to-month contracts, customers paying with an electronic check, customers with fiber optic internet service, customers who pay more monthly, customers with no partner, customers with no dependents, and customers who use paperless billing. 
* I would recommend an incentive to stay, and finding a way to make every customer's monthly payment closer to equal to each other. The rest of the drivers of churn are determined by outside forces that the company could not affect.
