'''In a pie chart, the term “explode” refers to the action of pulling out one or more slices from the pie to emphasize their significance. This technique helps to draw attention to specific categories within the data, making it easier for viewers to interpret the chart
explode_indices: A list of indices for the slices you want to explode.
explode: A list comprehension that sets the explode value to 0.1 for the specified indices and 0 for the others.
plt.pie(): Creates the pie chart with the dynamically generated explode list.


'''

import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
sizes = [15, 30, 45, 10, 20, 25, 35, 40, 50]

# Indices of slices to explode
explode_indices = [0, 3, 6]

# Create the explode list dynamically
explode = [0.1 if i in explode_indices else 0 for i in range(len(sizes))]

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the plot
plt.title('Dynamic Exploded Pie Chart')
plt.show()
