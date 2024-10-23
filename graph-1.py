import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
years = np.array([
    'IBM 1997',
    'RIGETTI 2016', 
    'IBM 2016', 
    'IBM 2017', 
    'INTEL 2018', 
    'GOOGLE 2018', 
    'RIGETTI 2019', 
    'IBM 2022', 
    'IBM 2023'
])
values = np.array([2, 3, 5, 50, 49, 72, 128, 433, 1121])

# Create a DataFrame
data = pd.DataFrame({'Year': years, 'Value': values})

# Set a light style
sns.set(style='whitegrid')

# Create the plot
plt.figure(figsize=(14, 7))
sns.lineplot(x='Year', y='Value', data=data, marker='o', color='#007acc', linewidth=2, label='Values', markersize=8)

# Add a trend line
sns.regplot(x=np.arange(len(data)), y='Value', data=data, scatter=False, color='#ff6f61', label='Trend Line', ci=None)

# Customize the plot
plt.title('Qubits by Quantum Computers Over Time', fontsize=20, fontweight='bold')
plt.xlabel('Year', fontsize=16, fontweight='bold')
plt.ylabel('Number of Qubits', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14, loc='upper left')

# Add annotations for key points
for i in range(len(data)):
    plt.text(x=i, y=values[i] + 20, s=f"{values[i]}", fontsize=10, ha='center', color='black')

# Simplified grid lines
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.grid(which='minor', linestyle=':', linewidth=0.3, alpha=0.5)

# Save the figure
plt.tight_layout()
plt.savefig('Qubits_by_Quantum_Computers.png', dpi=300)

# Show the plot
plt.show()
