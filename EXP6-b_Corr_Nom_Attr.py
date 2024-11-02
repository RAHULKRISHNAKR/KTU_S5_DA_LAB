import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv('data/Corr_Nom_Attr.csv')

contingency_table = pd.crosstab(df['Gender'], df['Preference'])
print(contingency_table)

chi2, _, _, _ = chi2_contingency(contingency_table)

n = contingency_table.sum().sum()
cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape[0] - 1, contingency_table.shape[1] - 1))))

print(f'Chi2: {chi2}')
print(f'Cramer\'s V: {cramers_v}')

if cramers_v < 0.1:
    print('Weak association')
elif cramers_v < 0.3:
    print('Moderate association')
else:    
    print('Strong association')