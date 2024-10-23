import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
funding_amount = np.array([73, 39, 287, 116, 417, 365])  # in millions
deal_count = np.array([6, 10, 13, 23, 26, 37])

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar plot (Funding amount)
bars1 = ax1.bar(years - 0.2, funding_amount, color='gray', width=0.3, label='Funding Amount ($M)')
ax1.set_xlabel('Year', fontsize=14, )
ax1.set_ylabel('Funding Amount ($M)', fontsize=14,  color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_ylim(0, 500)

# Add labels to the bars for funding amount with dollar sign
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'${yval}M', ha='center', va='bottom', fontsize=12, color='black')

# Create a twin y-axis for the deal count
ax2 = ax1.twinx()
bars2 = ax2.bar(years + 0.2, deal_count, color='lightgray', width=0.3, label='Deal Count', alpha=0.7)
ax2.set_ylabel('Deal Count', fontsize=14, color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylim(0, 40)

# Annotate deal counts
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}', ha='center', va='bottom', fontsize=12, color='black')

# Remove trend lines
# Create a smooth line with a spline (if desired for future reference)
# spl_funding = make_interp_spline(years, funding_amount, k=2)  # Quadratic spline
# x_smooth = np.linspace(years.min(), years.max(), 500)
# y_smooth_funding = spl_funding(x_smooth)

# Plotting the trend line has been removed

# Add title
plt.title('Quantum Computing Deals Are On The Rise\nDisclosed Deals & Equity Funding ($M), 2015 - 2020', fontsize=14, fontweight='bold')

# Combine legends from both axes
handles, labels = [], []
for ax in [ax1, ax2]:
    for handle, label in zip(*ax.get_legend_handles_labels()):
        handles.append(handle)
        labels.append(label)

# Place the combined legend on the left side
ax1.legend(handles, labels, loc='upper left')

# Adjust layout to prevent overlap
plt.tight_layout()

plt.savefig('C:/Users/QC/Desktop/quantum_computing_deals.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()
