import streamlit as st
import matplotlib.pyplot as plt

def visualize_dataset(X, y):
    """
    Visualize the dataset using a scatter plot.

    Parameters:
    - X (list of list): Features of the dataset.
    - y (list): Labels of the dataset.

    Returns:
    - None
    """
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

    # Display the plot using Streamlit
    st.pyplot(fig)

def test_visualize_dataset():
    # Test visualize_dataset function
    X = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8], [0.9, 0.1]]
    y = [0, 1, 0, 1, 0]
    visualize_dataset(X, y)

if __name__ == "__main__":
    # Define your dataset
    X = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8], [0.9, 0.1]]
    y = [0, 1, 0, 1, 0]  # Example labels

    # Visualize the dataset
    visualize_dataset(X, y)
