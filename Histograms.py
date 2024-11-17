'Constructing histograms with overlay in Python is a common technique used to compare the distributions of two or more datasets. You can overlay histograms using the matplotlib library, which is very flexible and powerful for creating visualizations.

#Example 1: Overlaying Two Histograms

import matplotlib.pyplot as plt
import numpy as np

# Example data: two datasets with random values
data1 = np.random.normal(0, 1, 1000)  # Normally distributed data (mean=0, std=1)
data2 = np.random.normal(1, 2, 1000)  # Normally distributed data (mean=1, std=2)

# Define the number of bins for the histograms
bins = 30

# Plot the first histogram (data1)
plt.hist(data1, bins=bins, alpha=0.5, label='Data 1', color='blue', edgecolor='black')

# Plot the second histogram (data2)
plt.hist(data2, bins=bins, alpha=0.5, label='Data 2', color='red', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Overlayed Histograms')

# Add a legend
plt.legend()

# Show the plot
plt.show()

#Example 2: Overlaying Multiple Histograms (More than Two)
'You can overlay multiple histograms by simply adding more plt.hist() calls. Let s add a third dataset and create an overlay of three histograms.
# Example data: three datasets with random values
data1 = np.random.normal(0, 1, 1000)  # Dataset 1 (mean=0, std=1)
data2 = np.random.normal(2, 1, 1000)  # Dataset 2 (mean=2, std=1)
data3 = np.random.normal(0, 2, 1000)  # Dataset 3 (mean=0, std=2)

# Plot the first histogram (data1)
plt.hist(data1, bins=30, alpha=0.5, label='Data 1', color='blue', edgecolor='black')

# Plot the second histogram (data2)
plt.hist(data2, bins=30, alpha=0.5, label='Data 2', color='red', edgecolor='black')

# Plot the third histogram (data3)
plt.hist(data3, bins=30, alpha=0.5, label='Data 3', color='green', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Overlayed Histograms with Three Datasets')

# Add a legend
plt.legend()

# Show the plot
plt.show()

#Example 3: Adjusting Bin Width and Range
'Sometimes, you may need to adjust the bin width or the range of the histogram to make the comparison between the datasets clearer.

# Example data: two datasets with random values
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 2, 1000)

# Define bin edges manually for more control
bins = np.linspace(-6, 6, 30)  # Bins from -6 to 6, with 30 bins

# Plot the first histogram (data1)
plt.hist(data1, bins=bins, alpha=0.5, label='Data 1', color='blue', edgecolor='black')

# Plot the second histogram (data2)
plt.hist(data2, bins=bins, alpha=0.5, label='Data 2', color='red', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Overlayed Histograms with Custom Bins')

# Add a legend
plt.legend()

# Show the plot
plt.show()

#Example 4: Kernel Density Estimate (KDE) with Histogram Overlay
'Sometimes, a Kernel Density Estimate (KDE) can be overlaid on a histogram to better visualize the distribution. This can be especially useful when you want a smoothed version of the histogram.

import seaborn as sns

# Example data: two datasets with random values
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)

# Plot the histogram of data1 with a KDE
sns.histplot(data1, kde=True, color='blue', label='Data 1', stat='density', alpha=0.5)

# Plot the histogram of data2 with a KDE
sns.histplot(data2, kde=True, color='red', label='Data 2', stat='density', alpha=0.5)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram with KDE Overlay')

# Add a legend
plt.legend()

# Show the plot
plt.show()
