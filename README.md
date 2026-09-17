## 💻 Laptop Price Prediction

A Machine Learning web application that predicts the estimated price of a laptop based on its hardware specifications and configuration.

The project uses a trained Machine Learning model with a Streamlit interface to provide interactive laptop price predictions.

# 🚀 Live Demo

👉 Laptop Price Predictor

Try the deployed application online.

## 📌 Project Overview

Laptop prices depend on several factors such as:

* Brand
* Laptop type
* Screen size
* RAM
* Operating system
* Weight
* CPU
* GPU
* Storage capacity
* Storage type
* Display resolution
* Touchscreen support
* IPS display

This project uses these features to predict the estimated price of a laptop.

## ✨ Features

* 🎯 Laptop price prediction using a trained ML model
* 🖥️ Interactive Streamlit web interface
* 📊 Multiple laptop configuration inputs
* 🤖 Pre-trained machine learning model
* 📁 Dataset included for reference
* 🌐 Deployed online using Render

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Jupyter Notebook
* Render

## 📂 Project Structure

```text
laptop-price-prediction/
│
├── app.py
├── laptop_price.csv
├── laptop_price_model.pkl
├── requirements.txt
└── README.md
```

## 📊 Dataset

The dataset contains laptop specifications and their corresponding prices.

| Feature          | Description           |
| ---------------- | --------------------- |
| Company          | Laptop manufacturer   |
| Product          | Laptop model          |
| TypeName         | Type of laptop        |
| Inches           | Screen size           |
| Ram              | RAM in GB             |
| OpSys            | Operating system      |
| Weight           | Laptop weight         |
| IPS              | IPS display indicator |
| Touchscreen      | Touchscreen indicator |
| Cpu Speed        | CPU speed             |
| Gpu Brand        | GPU manufacturer      |
| Storage Capacity | Storage size          |
| Storage Type     | SSD, HDD, etc.        |
| Price_euros      | Laptop price          |

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/syedziaulhaq980/laptop-price-prediction.git
```

Navigate to the project directory:

```bash
cd laptop-price-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## 🤖 Machine Learning Model

The trained model is stored in:

```text
laptop_price_model.pkl
```

The Streamlit application loads this model and uses the user's laptop specifications to generate a predicted price.

## 📈 Workflow

```text
Laptop Specifications
        ↓
Feature Processing
        ↓
Trained ML Model
        ↓
Price Prediction
        ↓
Predicted Laptop Price
```

## 🌐 Deployment

The application is deployed using Render and is available online:

### [🚀 Open Laptop Price Predictor](https://laptop-price-prediction-wiif.onrender.com/)

## 📦 GitHub Repository

[View the source code on GitHub](https://github.com/syedziaulhaq980/laptop-price-prediction)

## 👨‍💻 Author

**Syed Zia Ul Haq**

Machine Learning / Data Science Project
