import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create pie charts with different autopct formats
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# One decimal place
axs[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
axs[0].set_title('One Decimal Place')

# No decimal places
axs[1].pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140)
axs[1].set_title('No Decimal Places')

# Two decimal places
axs[2].pie(sizes, labels=labels, autopct='%1.2f%%', startangle=140)
axs[2].set_title('Two Decimal Places')

# Equal aspect ratio ensures that pie is drawn as a circle.
for ax in axs:
    ax.axis('equal')

plt.show()
