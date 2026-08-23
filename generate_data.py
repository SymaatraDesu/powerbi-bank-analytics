import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 2500

data = {
    'Customer_ID': [f'CUST-{1000 + i}' for i in range(n_samples)],
    'Age': np.random.randint(18, 70, size=n_samples),
    'Gender': np.random.choice(['Male', 'Female'], size=n_samples, p=[0.52, 0.48]),
    'Credit_Score': np.random.randint(350, 850, size=n_samples),
    'Tenure_Years': np.random.randint(0, 10, size=n_samples),
    'Balance': np.round(np.random.uniform(1000, 200000, size=n_samples), 2),
    'Products_Count': np.random.choice([1, 2, 3, 4], size=n_samples, p=[0.45, 0.40, 0.10, 0.05]),
    'Has_Credit_Card': np.random.choice([1, 0], size=n_samples, p=[0.7, 0.3]),
    'Is_Active_Member': np.random.choice([1, 0], size=n_samples, p=[0.55, 0.45]),
    'Estimated_Salary': np.round(np.random.uniform(25000, 150000, size=n_samples), 2),
    'Segment': np.random.choice(['Standard', 'Silver', 'Gold', 'VIP'], size=n_samples, p=[0.5, 0.3, 0.15, 0.05])
}

df = pd.DataFrame(data)

z = (
    0.03 * (df['Age'] - 40)
    + 0.7 * (df['Products_Count'] > 2).astype(int)
    - 0.9 * df['Is_Active_Member']
    - 0.002 * (df['Credit_Score'] - 600)
)
churn_prob = 1 / (1 + np.exp(-z))
df['Exited'] = (churn_prob > 0.45).astype(int)

df.to_csv('bank_analytics_data.csv', index=False)
print("Файл bank_analytics_data.csv успешно создан!")
