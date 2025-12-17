import pandas as pd
import numpy as np

# 1. Create sample data as a pandas DataFrame
data = {
    'country': ['USA', 'USA', 'USA', 'UK', 'UK', 'UK', 'UK', 'Japan', 'Japan', 'USA', 'UK', 'USA'],
    'breed': ['Maine Coon', 'Maine Coon', 'Siamese', 'Persian', 'Siamese', 'Maine Coon', 'Persian', 'Siamese', 'Siamese', 'Persian', 'Siamese', 'Maine Coon']
}
df = pd.DataFrame(data)

# Optional: Add totals for rows and columns using margins=True
# frequency_table = pd.crosstab(df['country'], df['breed'], margins=True, margins_name="Total")

# 2. Create the frequency table using pd.crosstab()
frequency_table = pd.crosstab(df['country'], df['breed'])

# 3. Print the resulting frequency table
print(frequency_table)