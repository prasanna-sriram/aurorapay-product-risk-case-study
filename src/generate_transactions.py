import numpy as np
import pandas as pd

np.random.seed(42)

# Number of Transactions
n = 100000

# Customers: assume 20k unique
customer_ids = np.random.randint(1, 20001, size=n)

# Channels and Products
channels = np.random.choice(
    ['POS', 'Online', 'Mobile'],
    size=n,
    p=[0.4,0.35,0.25]
)

products = np.random.choice(
    ['Debit', 'e-Transfer'],
    size=n,
    p=[0.6,0.4]
)

# Amounts: log-normal to get many small, few large
amounts = np.random.lognormal(mean=3.0, sigma=0.8, size=n)
amounts = np.round(np.clip(amounts, 1, 5000), 2)

# Time window for this case study: Q1 of 2026
start = np.datetime64('2026-01-01')
end = np.datetime64('2026-03-31')

rand_times = start + (end - start) * np.random.random(n)

# Status: Small Failure rates
status = np.random.choice(
    ['Success', 'Failed'],
    size=n,
    p=[0.985,0.015]
)

# Fraud: Higher on e-Transfer than Debit
fraud_prob = np.where(products == 'e-Transfer', 0.003, .0005)
fraud_flags = np.random.binomial(1, fraud_prob)

# Do not flag failed transactions as fraud
fraud_flags = np.where(status == 'Success', fraud_flags, 0)

transactions = pd.DataFrame({
    'transaction_id': np.arange(1, n + 1),
    'customer_id': customer_ids,
    'channel': channels,
    'product': products,
    'amount': amounts,
    'currency': 'CAD',
    'timestamp': rand_times,
    'status': status,
    'fraud_flag': fraud_flags
})

# Quick dataset check
summary = {
    'row_count': len(transactions),
    'total_volume': float(transactions['amount'].sum()),
    'fraud_txn_count': int(transactions['fraud_flag'].sum()),
    'fraud_rate_overall': float(transactions['fraud_flag'].mean()),
    'fraud_rate_etransfer': float(transactions.loc[transactions['product'] == 'e-Transfer', 'fraud_flag'].mean()),
    'fraud_rate_debit': float(transactions.loc[transactions['product'] == 'Debit', 'fraud_flag'].mean())
}


print(summary)


# Save to CSV
transactions.to_csv('data/raw/transactions.csv', index=False)