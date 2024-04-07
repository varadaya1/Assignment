import streamlit as st

# Function to display dataset image
def display_image():
    st.image("C:/Windows/System32/Assignment/grace_hopper.jpg", caption="Dataset Image")

# Function to visualize classifier
def visualize_classifier():
    st.write("Insert code to visualize classifier here")

def main():
    st.title("Linear Dataset Visualization")

    # Display dataset image
    st.subheader("Dataset Image")
    display_image()

    # Display classifier visualization
    st.subheader("Classifier Visualization")
    visualize_classifier()

if __name__ == "__main__":
    main()

