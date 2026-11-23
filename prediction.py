import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('./clean_survey.csv')

df['Buys_Often'] = (df['Online_Shopping_Frequency'].isin(
    ['Often', 'Always'])).astype(int)

X = df[['Age', 'Social_Ads_Influence_Score',
        'Review_Influence_Score', 'Discount_Importance_Score', 'Trust_In_Online_Reviews_Score', 'Online_Shopping_Satisfaction_Score']]
y = df['Buys_Often']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print('Accuracy :', accuracy_score(y_test, model.predict(X_test)))
print("Features:", list(X.columns))
print(model.coef_)

# print(df['Online_Shopping_Frequency'].value_counts())
