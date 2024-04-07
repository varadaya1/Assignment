import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define your dataset
X = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8], [0.9, 0.1]]
y = [0, 1, 0, 1, 0]  # Example labels

# Define the number of epochs
num_epochs = 1000

# Training loop
for epoch in range(num_epochs):
    # Insert your training logic here
    pass  # Placeholder for training logic

# Plot the dataset
st.title('Custom Classifier Visualization')
st.write('Dataset Visualization')
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(len(X)):
    if y[i] == 0:
        ax.scatter(X[i][0], X[i][1], color='blue', label='Class 0')
    else:
        ax.scatter(X[i][0], X[i][1], color='red', label='Class 1')

ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_title('Dataset Visualization')
ax.legend()
ax.grid(True)

# Save scatter plot as image
image_path = "scatter_plot.png"  # Define the path for saving the image
plt.savefig(image_path)

# Display the scatter plot in Streamlit
st.pyplot(fig)

# Display parameters
st.write('## Parameters Used:')
st.write(f'- Number of Epochs: {num_epochs}')

# Include other parameters as needed

# Save the parameters to the README file
with open("README.md", "a") as readme_file:
    readme_file.write("\n## Parameters\n")
    readme_file.write(f"- Number of Epochs: {num_epochs}\n")

# Add a message indicating successful completion
st.write("Scatter plot and parameters saved successfully!")
