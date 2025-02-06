import streamlit as st
import pandas as pd
import joblib



page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1511027643875-5cbb0439c8f1?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.5);
}

[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)



# Load the trained model
model = joblib.load('fire_prediction_model.pkl')

# Streamlit app
st.title("Forest Fire Prediction")





st.write("""
This app predicts the likelihood of a forest fire based on user input parameters.
Provide the values below to get a prediction.
""")

# Input Fields
area = st.text_input("Area (Encoded - integer value)", value="0")
oxygen = st.slider("Oxygen Level (%)", min_value=0.0, max_value=100.0, value=21.0, step=0.1)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# Validate and Prepare Input
try:
    area = int(area)  # Ensure Area is an integer
    input_data = pd.DataFrame({
        'Area': [area],
        'Oxygen': [oxygen],
        'Temperature': [temperature],
        'Humidity': [humidity]
    })
    valid_input = True
except ValueError:
    st.error("Please enter a valid integer for 'Area'")
    valid_input = False

# Prediction
if valid_input and st.button("Predict"):
    prediction = model.predict(input_data)
    result = "🔥 Fire Detected!" if prediction[0] == 1 else "✅ No Fire Detected!"
    st.subheader("Prediction Result")
    st.write(result)
