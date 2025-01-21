import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file
data = pd.read_csv('hl_chain_error.csv')

# Melt DataFrame to long format for plotting
df_melted = pd.melt(data, id_vars=['ID', 'Model'], var_name='Region', value_name='Error')

custom_palette = {"ProteinMPNN": "#66c2a5", "MPNN-AbNet": "#fc8d62", "Original": "#8da0cb"}

# Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Error', hue='Model', data=df_melted, palette=custom_palette)
plt.title('Prediction Error for Heavy/Light Chains')
plt.xlabel('Region')
plt.ylabel('RMSD')
plt.show()