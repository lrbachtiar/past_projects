import pandas as pd
import re

def clean_column_names(column_name):
    new_name = re.sub(r'[^A-Za-z0-9]', '_', column_name).strip()
    cameled = re.sub(r'_{1,}', '_', camel_to_lower_case(new_name))
    final = cameled[:-1] if cameled[-1] == '_' else cameled
    return final

def camel_to_lower_case(name):
    step_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z])([0-9A-Z])', r'\1_\2', step_1).lower()

# =============================================================================
#    Data Column Details
#
#    Date - The date of the observation
#    AveragePrice - the average price of a single avocado
#    type - conventional or organic
#    year - the year
#    Region - the city or region of the observation
#    Total Volume - Total number of avocados sold
#    4046 - Total number of avocados with PLU 4046 sold
#    4225 - Total number of avocados with PLU 4225 sold
#    4770 - Total number of avocados with PLU 4770 sold
#
# =============================================================================

# =============================================================================
#    Data Cleaning
# =============================================================================

df = pd.read_csv('avocado.csv')
df.drop(['Unnamed: 0'], axis=1, inplace = True)
for c in df.columns:
    df.rename(columns={c:clean_column_names(c)}, inplace=True)

# Format date column from string to date-type
df['date'] = pd.to_datetime(df['date'])

# =============================================================================
#    Initial Analysis
# =============================================================================
regions = df.groupby(df.region)

print("Total regions :", len(regions))
print("-------------")
for name, group in regions:
    print(name, " : ", len(group))
    






























