import streamlit as st
import pandas as pd

# Simulate loading a dataset (for demonstration purposes)
@st.cache_data
def load_data():
    # Create a dummy dataset with equal-length columns
    data = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],  # 5 rows
        'household': [0, 1, 0, 1, 0],  # 5 rows (0 = No, 1 = Yes)
        'time_since_previous_visit': [1, 2, 3, 4, 5],  # 5 rows
        'contact_frequency': ['weekly', 'monthly', 'weekly', 'monthly', 'weekly'],  # 5 rows
        'returned': [1, 0, 1, 0, 1]  # Target column (1 = returned, 0 = did not return)
    })
    return data

# Simulate a prediction (rule-based)
import streamlit as st
import pandas as pd

# Function to load sample dataset
def load_data():
    return pd.DataFrame({
        "age": [25, 40, 35],
        "household": [1, 0, 1],
        "time_since_previous_visit": [2, 5, 1],
        "contact_frequency": ["weekly", "monthly", "weekly"]
    })

# Simple prediction function (logic-based)
def predict(input_data):
    """Predict client retention likelihood based on input data."""
    if input_data['age'].values[0] > 30 and input_data['household'].values[0] == 1:
        return [1]  # Likely to return
    else:
        return [0]  # Unlikely to return

# Streamlit App
st.title("Client Retention Prediction for Food Bank")

# Load and display dataset
data = load_data()

if st.checkbox("Show raw data"):
    st.write(data)

# User Input Section
st.header("Enter Client Information")

# Create input fields
input_features = {
    'age': st.number_input("Enter Age", min_value=0, max_value=100, value=30),
    'household': st.selectbox("Is the client part of a household?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No"),
    'time_since_previous_visit': st.number_input("Enter Time Since Previous Visit (in months)", min_value=0, value=1),
    'contact_frequency': st.selectbox("Contact Frequency", options=["weekly", "monthly"])
}

# Convert input to DataFrame
input_df = pd.DataFrame([input_features])

# Prediction Button
if st.button("Predict"):
    prediction = predict(input_df)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.success("✅ The client is likely to return.")
    else:
        st.error("❌ The client is unlikely to return.")

  




   
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Dashboard function
def dashboard():
    # Add the header image
    header_image_url = "https://raw.githubusercontent.com/ChiomaUU/Client-Prediction/refs/heads/main/ifssa_2844cc71-4dca-48ae-93c6-43295187e7ca.avif"
    st.image(header_image_url, use_container_width=True)  # Display the image at the top

    st.title("Client Return Prediction App (MVP)")
    st.write("This app predicts whether a client will return for food hampers.")
    

# Main function to run the app
def main():
    st.sidebar.title("Client Return Prediction App")
    app_page = st.sidebar.radio("Choose a page", ["Dashboard", "Infograph", "Predictions"])

    if app_page == "Dashboard":
        dashboard()
        
    elif app_page == "Infograph":
        exploratory_data_analysis()
        
    elif app_page == "Predictions":
        predict()
    
    
# Run the app
if __name__ == "__main__":
    main()
