
import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    return joblib.load("laptop_price_model.pkl")


model = load_model()


# =========================================================
# GET CATEGORIES FROM TRAINED ENCODER
# =========================================================

preprocessor = model.named_steps["preprocessing"]

encoder = preprocessor.named_transformers_["cat"]

categorical_columns = [
    "Company",
    "Product",
    "TypeName",
    "OpSys",
    "Gpu Brand",
    "Gpu Model",
    "Gpu Family",
    "Cpu Brand",
    "Cpu Family",
    "Storage Type"
]

categories = dict(
    zip(categorical_columns, encoder.categories_)
)


# =========================================================
# PAGE HEADER
# =========================================================

st.title("💻 Laptop Price Predictor")

st.markdown(
    "### Predict the estimated price of a laptop using Machine Learning"
)

st.write(
    "Enter the laptop specifications below and click **Predict Price**."
)

st.divider()


# =========================================================
# BASIC INFORMATION
# =========================================================

st.subheader("🏷️ Basic Information")

col1, col2, col3 = st.columns(3)


with col1:

    company = st.selectbox(
        "Company",
        categories["Company"]
    )

    product = st.selectbox(
        "Product",
        categories["Product"]
    )

    typename = st.selectbox(
        "Type",
        categories["TypeName"]
    )

    opsys = st.selectbox(
        "Operating System",
        categories["OpSys"]
    )


with col2:

    ram = st.selectbox(
        "RAM (GB)",
        [2, 4, 6, 8, 12, 16, 24, 32, 64]
    )

    inches = st.number_input(
        "Screen Size (Inches)",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.5,
        max_value=5.0,
        value=2.0,
        step=0.01
    )


with col3:

    storage_capacity = st.number_input(
        "Storage Capacity (GB)",
        min_value=32,
        max_value=4000,
        value=512,
        step=32
    )

    storage_type = st.selectbox(
        "Storage Type",
        categories["Storage Type"]
    )


# =========================================================
# DISPLAY INFORMATION
# =========================================================

st.divider()

st.subheader("🖥️ Display Specifications")

col1, col2, col3 = st.columns(3)


with col1:

    width = st.number_input(
        "Screen Width",
        min_value=800,
        max_value=4000,
        value=1920,
        step=1
    )


with col2:

    height = st.number_input(
        "Screen Height",
        min_value=600,
        max_value=3000,
        value=1080,
        step=1
    )


with col3:

    ips = st.selectbox(
        "IPS Display",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    touchscreen = st.selectbox(
        "Touchscreen",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# =========================================================
# CPU INFORMATION
# =========================================================

st.divider()

st.subheader("⚙️ CPU Specifications")

col1, col2, col3 = st.columns(3)


with col1:

    cpu_brand = st.selectbox(
        "CPU Brand",
        categories["Cpu Brand"]
    )


with col2:

    cpu_family = st.selectbox(
        "CPU Family",
        categories["Cpu Family"]
    )


with col3:

    cpu_speed = st.number_input(
        "CPU Speed (GHz)",
        min_value=0.5,
        max_value=5.5,
        value=2.5,
        step=0.1
    )


# =========================================================
# GPU INFORMATION
# =========================================================

st.divider()

st.subheader("🎮 GPU Specifications")

col1, col2, col3 = st.columns(3)


with col1:

    gpu_brand = st.selectbox(
        "GPU Brand",
        categories["Gpu Brand"]
    )


with col2:

    gpu_family = st.selectbox(
        "GPU Family",
        categories["Gpu Family"]
    )


with col3:

    gpu_model = st.selectbox(
        "GPU Model",
        categories["Gpu Model"]
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Laptop Price",
    type="primary",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    input_data = pd.DataFrame({

        "Company": [company],

        "Product": [product],

        "TypeName": [typename],

        "Inches": [inches],

        "Ram": [ram],

        "OpSys": [opsys],

        "Weight": [weight],

        "Width": [width],

        "Height": [height],

        "IPS": [ips],

        "Touchscreen": [touchscreen],

        "Cpu Speed": [cpu_speed],

        "Gpu Brand": [gpu_brand],

        "Gpu Model": [gpu_model],

        "Gpu Family": [gpu_family],

        "Cpu Brand": [cpu_brand],

        "Cpu Family": [cpu_family],

        "Storage Capacity": [storage_capacity],

        "Storage Type": [storage_type]
    })


    try:

        prediction = model.predict(input_data)[0]

        st.divider()

        st.subheader("💰 Predicted Laptop Price")

        st.success(
            f"Estimated Price: €{prediction:,.2f}"
        )


        # =================================================
        # MODEL INFORMATION
        # =================================================

        st.divider()

        st.subheader("📊 Model Performance")

        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric(
                "MAE",
                "165.53"
            )

        with metric2:
            st.metric(
                "RMSE",
                "249.19"
            )

        with metric3:
            st.metric(
                "R²",
                "0.8777"
            )


        st.caption(
            "Model: Tuned Gradient Boosting Regressor"
        )


        # =================================================
        # SHOW INPUT DATA
        # =================================================

        with st.expander("🔍 View Input Details"):

            st.dataframe(
                input_data,
                use_container_width=True
            )


    except Exception as e:

        st.error(
            "Prediction failed. Please check the model and input features."
        )

        st.exception(e)


