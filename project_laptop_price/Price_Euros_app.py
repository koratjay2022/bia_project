import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder
import sys
sys.path.append("../")
from Utils.common_function import common_Fucnation,train_and_evaluate_model,train_and_evaluate_multiple_models
from unique_date_extract import unique_company, unique_typeName, unique_ScreenResolution, unique_Ram
from unique_date_extract import unique_Cpu, unique_Gpu, unique_Memory, unique_OpSys

# Load the trained Random Forest model
model = load('random_forest_model.joblib')
comm_fun = common_Fucnation()

# Create a Streamlit app
st.title("Customer Churn Prediction App")

# Input fields for feature values on the main screen
# st.header("Enter Customer Information")
# company = st.selectbox("Select Company", (unique_company))
# typeName = st.selectbox("Select Type Name", (unique_typeName))
# inches = st.number_input('Enter screen size in inches', min_value=10.0, max_value=20.0, value=15.0, step=0.1, format="%.1f")
# screenResolution = st.selectbox("Select Screen Resolution", (unique_ScreenResolution))
# cpu = st.selectbox("Select CPU", (unique_Cpu))
# Ram = st.select_slider("Select RAM", (unique_Ram))
# memory = st.select_slider("Select Memory", (unique_Memory))
# gpu = st.selectbox("Select GPU", (unique_Gpu))
# OpSys = st.select_slider("Select OpSys", (unique_OpSys))
# weight = st.number_input('Enter screen size in Weight', min_value=1.0, max_value=4.0, value=2.0, step=0.1, format="%.1f")
# tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
# internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
# contract = st.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))
# monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=50)
# total_charges = st.number_input("Total Charges", min_value=0, max_value=10000, value=0)
st.header("Enter Customer Information")
company = st.selectbox("Select Company", (unique_company))
typeName = st.selectbox("Select Type Name", (unique_typeName))
inches = st.number_input('Enter screen size in inches', min_value=10.0, max_value=20.0, value=15.0, step=0.1, format="%.1f")
screenResolution = st.selectbox("Select Screen Resolution", (unique_ScreenResolution))
cpu = st.selectbox("Select CPU", (unique_Cpu))
Ram = st.select_slider("Select RAM", (unique_Ram))
memory = st.select_slider("Select Memory", (unique_Memory))
gpu = st.selectbox("Select GPU", (unique_Gpu))
OpSys = st.select_slider("Select OpSys", (unique_OpSys))
weight = st.number_input('Enter weight in kg', min_value=1.0, max_value=4.0, value=2.0, step=0.1, format="%.1f")


# # Map input values to numeric using the label mapping
# label_mapping = {
#     'DSL': 0,
#     'Fiber optic': 1,
#     'No': 2,
#     'Month-to-month': 0,
#     'One year': 1,
#     'Two year': 2,
# }
# internet_service = label_mapping[internet_service]
# contract = label_mapping[contract]

import re

match = re.search(r'\d+x\d+', screenResolution)
if match:
    resolution = match.group()
    resolution_width, resolution_height = map(int, resolution.split('x'))
else:
    st.error("Invalid screen resolution format. Please select a valid option.")
    st.stop()
    
cpu_brand = cpu.split()[0]
cpu_type_match = re.search(r'(Core \w+\d|Atom|FX|Celeron|E-Series|Ryzen|A\d+-Series|Pentium|Xeon|Core M)', cpu)
cpu_type = cpu_type_match.group() if cpu_type_match else None
cpu_clock_speed_match = re.search(r'(\d+\.\d+GHz|\d+GHz)', cpu)
cpu_clock_speed = cpu_clock_speed_match.group() if cpu_clock_speed_match else None

# # Make a prediction using the model
# selected_features = [inches, cpu, Ram, memory, gpu, OpSys, weight,
#        company, typeName, resolution_width,
#        resolution_height, cpu_brand, cpu_type, cpu_clock_speed]
# prediction = model.predict([[selected_features]])

# Display the prediction result on the main screen
# st.header("Prediction Result")
# if prediction[0] == 0:
#     st.success("This customer is likely to stay.")
# else:
#     st.error("This customer is likely to churn.")

# Add any additional Streamlit components or UI elements as needed.
# Encode categorical features
encoded_company = comm_fun.label_encode(data=pd.DataFrame({'Company': [company]}), column="Company").iloc[0]
encoded_cpu = comm_fun.label_encode(data=pd.DataFrame({'Cpu': [cpu]}), column="Cpu").iloc[0]
encoded_typeName = comm_fun.label_encode(data=pd.DataFrame({'TypeName': [typeName]}), column="TypeName").iloc[0]
encoded_gpu = comm_fun.label_encode(data=pd.DataFrame({'GPU': [gpu]}), column="GPU").iloc[0]
encoded_opSys = comm_fun.label_encode(data=pd.DataFrame({'OpSys': [OpSys]}), column="OpSys").iloc[0]
encoded_memory = comm_fun.label_encode(data=pd.DataFrame({'Memory': [OpSys]}), column="Memory").iloc[0]
encoded_cpu_brand = comm_fun.label_encode(data=pd.DataFrame({'CPU_Brand': [cpu_brand]}), column="CPU_Brand").iloc[0]
encoded_cpu_type = comm_fun.label_encode(data=pd.DataFrame({'CPU_Type': [cpu_type]}), column="CPU_Type").iloc[0]
encoded_cpu_clock_speed = float(cpu_clock_speed[:-3]) if cpu_clock_speed else None
print(encoded_cpu_brand)
# df = comm_fun.all_label_encode(data=df)
# ['Inches', 'Cpu', 'Ram', 'Memory', 'Gpu', 'OpSys', 'Weight',
#        'Company_encoded', 'TypeName_encoded', 'resolution_width',
#        'resolution_height', 'Cpu_Brand', 'Cpu_Type', 'Cpu_ClockSpeed'],
# selected_features = [
#     inches, Ram, memory, gpu, OpSys, weight,
#     company, typeName, resolution_width, resolution_height,
#     cpu_brand, cpu_type, cpu_clock_speed
# ]

selected_features = [
    inches, encoded_cpu,Ram, encoded_memory, encoded_gpu, encoded_opSys, weight,
    encoded_company, encoded_typeName, resolution_width, resolution_height,
    encoded_cpu_brand, encoded_cpu_type, encoded_cpu_clock_speed
]

if st.button("Predict Price"):
    if None in selected_features or '' in selected_features:
        st.error("Please fill all fields before making a prediction.")
    else:
        predicted_price = model.predict([selected_features])[0]

        st.header("Predicted Price")
        st.success(f"The predicted price of the laptop is: €{predicted_price:.2f}") 
if None in selected_features or '' in selected_features:
    st.error("Please fill all fields before making a prediction.")
else:
    predicted_price = model.predict([selected_features])[0]
    st.header("Predicted Price")
    st.success(f"The predicted price of the laptop is: €{predicted_price:.2f}") 

# Ensure all features are filled before prediction
# if None in selected_features or '' in selected_features:
#     st.error("Please fill all fields before making a prediction.")
# else:
#     # Make a prediction using the model
#     prediction = model.predict([selected_features])

#     # Display the prediction result on the main screen
#     st.header("Prediction Result")
#     if prediction[0] == 0:
#         st.success("This customer is likely to stay.")
#     else:
#         st.error("This customer is likely to churn.")
        
# how to run
# streamlit run file name
# E.g. :- streamlit run Price_euros_app.py