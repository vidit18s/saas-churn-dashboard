import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

N_CUSTOMERS = 500
segments = ['SMB', 'Mid-Market', 'Enterprise']
seg_weights = [0.55, 0.30, 0.15]
industries = ['SaaS', 'Retail', 'Healthcare', 'Finance', 'Manufacturing', 'Education']
plans = ['Starter', 'Growth', 'Professional', 'Enterprise']
seg_arr = {'SMB': (3000, 8000), 'Mid-Market': (12000, 40000), 'Enterprise': (60000, 150000)}
seg_churn = {'SMB': 0.032, 'Mid-Market': 0.018, 'Enterprise': 0.006}
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 3, 1)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def main():
    records = []
    for i in range(N_CUSTOMERS):
        segment = np.random.choice(segments, p=seg_weights)
        arr_min, arr_max = seg_arr[segment]
        arr = round(random.uniform(arr_min, arr_max), -2)
        mrr = round(arr / 12, 2)
        churn_prob = seg_churn[segment]
        churned = np.random.random() < churn_prob * 12
        signup_date = random_date(start_date, end_date - timedelta(days=90))
        if churned:
            churn_date = random_date(signup_date + timedelta(days=90), end_date)
            churn_date_str = churn_date.strftime('%Y-%m-%d')
            status = 'Churned'
        else:
            churn_date_str = None
            status = 'Active'
        login_freq = {'SMB': (2, 8), 'Mid-Market': (5, 15), 'Enterprise': (10, 30)}
        logins = random.randint(*login_freq[segment])
        nps = random.randint(0, 10)
        support_tickets = random.randint(0, 5) if status == 'Active' else random.randint(3, 12)
        expansion = round(arr * random.uniform(0, 0.25), -2) if status == 'Active' else 0
        records.append({
            'customer_id': f'CUST-{1000+i}',
            'segment': segment,
            'industry': random.choice(industries),
            'plan': random.choice(plans),
            'arr': arr,
            'mrr': mrr,
            'expansion_arr': expansion,
            'signup_date': signup_date.strftime('%Y-%m-%d'),
            'churn_date': churn_date_str,
            'status': status,
            'monthly_logins': logins,
            'nps_score': nps,
            'support_tickets': support_tickets,
        })
    df = pd.DataFrame(records)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/customers.csv', index=False)
    print(f"Generated {len(df)} customer records")

if __name__ == "__main__":
    main()
