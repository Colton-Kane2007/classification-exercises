# Classification Project
# Project description with goals:
## This is a notebook where I analyze drivers of churn within the telco_churn dataset from MySQL. Using the data science pipeline,
## I grab the data, prepare it, explore it, visualize it, train models on it, and use statistical testing in order to answer questions about the data.


# Initial hypotheses and/or questions I have of the data, ideas:
## The main question I'm asking of the data is 'What are the main drivers of churn?' and subsequently 'What actions could I recommend to a stakeholder in order to reduce churn?'
## More specifically, my initial hypothesis is that the shorter contract term is the biggest driver in churn, because people paying month-to-month can leave any time.

# Data Dictionary:
|Feature|Dtype|
|:--------|:-----------|
|payment_type_id|	int64|
|internet_service_type_id|	int64|
|contract_type_id|	int64|
|customer_id|	object|
|gender|	object|
|senior_citizen|	int64|
|partner|	object|
|dependents| object|
|tenure|	int64|
|phone_service|	object|
|multiple_lines|	object|
|online_security|	object|
|online_backup|	object|
|device_protection|	object|
|tech_support|	object|
|streaming_tv|	object|
|streaming_movies|	object|
|paperless_billing|	object|
|monthly_charges|	float64|
|total_charges|	object|
|churn|	object|
|contract_type|	object|
|internet_service_type|	object|
|payment_type|	object|


# Project planning:
## I will grab the data, prepare it, explore it, visualize it, train models on it, and use statistical testing in order to answer questions about the data.



# Instructions or an explanation of how someone else can reproduce my project and findings (What would someone need to be able to recreate my project on their own?):
# In order to recreate this project, another user would need similar acquire and prepare files, and a MySQL account to log in, with the credentials in your acquire file.


# Key findings, recommendations, and takeaways from my project:
## My main takeaway is that the data shows a correlation between higher rates of churn and customers with month-to-month contracts, customers paying with an electronic check, customers with fiber optic internet service, customers who pay more monthly, customers with no partner, customers with no dependents, and customers who use paperless billing. 
## I would recommend longer contracts or an incentive to stay, and finding a way to make every customer's monthly payment closer to equal to each other. The rest of the drivers of churn are determined by outside forces that the company could not affect.
