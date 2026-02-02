import numpy as np
import pandas as pd

policy_data = np.array([
    [1001, 12000, 50000, 5000 ],
    [1002, 15000, 60000, 6000 ],
    [1003, 13000, 55000, 5500 ],
    [1004, 16000, 70000, 7000 ],
    [1005, 14000, 65000, 6500 ]
    
])
cal = ["policy number", "premium amount", "insured amount", "claim amount"]

print("original policyholder Data :")

print()
df_before = pd.DataFrame(data=policy_data, columns=cal)
print(df_before)

policy_data[:,[1,3]] = policy_data[:,[3,1]] 

print("\n corrected policyholder Data(After swapping ) :")
print()
df_after = pd.DataFrame(data=policy_data, columns=cal)
print(df_after)

total_claim_amount = np.sum(policy_data[:,3])
print(f"\n Total Claim Amount from all policyholders: {total_claim_amount}")