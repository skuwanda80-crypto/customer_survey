🛍️ Predicting Frequent Buyers - Consumer Behaviour Analysis

Can we predict who will become a frequent buyer?
I analysed 500 shoppers using Python (Machine Learning) + Power BI (Dashboard).

───

📊 Project Overview

Part 1 - Descriptive: What is happening?
Part 2 - Predictive: Can we predict who buys often?

Tools: Python (Pandas, Scikit-Learn, Matplotlib) | Power BI | Logistic Regression

───

📁 Files in this Repo


File
What it is

consumer_data.csv
Dataset - 500 shoppers

analysis.py
Python code - cleaning + Logistic Regression model

survey.pbix
Power BI Dashboard - Part 1

prediction_chart.png
Prediction Graph - Part 2



───

🔍 Key Findings

Part 1 - Dashboard
• Most shoppers buy Occasionally
• Top product: Electronics
• Top payment: Credit Card
• Discounts drive one-time purchases, not loyalty

Part 2 - Prediction Model
Model: Logistic Regression
Accuracy: 66%

What predicts frequent buying?


Feature
Importance

Trust in Reviews
0.142

Age
-0.028

Discount
-0.024

Reviews
-0.007

Social Ads
-0.003

Satisfaction
0.0008



Conclusion: Only ONE real predictor - Trust in Reviews.
Discounts, Social Ads, and Satisfaction = almost zero.

You can't predict loyalty from discounts. You predict it from trust.

───

💡 Business Recommendation

Stop spending more on discounts to get loyalty.
Invest in trustworthy reviews:
1. Show verified reviews only
2. Reply to negative reviews fast
3. Remove fake reviews

Trust brings customers back. Discounts don't.

───

👤 Author
Salem Kuwanda
Data Analyst | Python | Power BI | Machine Learning