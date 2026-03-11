import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

data = {'Size': ['Small', 'Medium', 'Large', 'Extra Large', 'Medium']}

df = pd.DataFrame(data)

size_order = ['Small', 'Medium', 'Large', 'Extra Large']

encoder = OrdinalEncoder(categories=[size_order])

df['Size_encoded'] = encoder.fit_transform(df[['Size']])

print(df)


