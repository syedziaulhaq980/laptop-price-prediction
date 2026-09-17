# 💻 Laptop Price Prediction

A **Machine Learning web application** that predicts the estimated price of a laptop based on its hardware specifications and configuration.

The project uses a trained Machine Learning model with a **Streamlit** interface to provide interactive laptop price predictions.

---

## 📌 Project Overview

Laptop prices vary depending on specifications such as:

* 🏢 Company / Brand
* 💻 Laptop Type
* 📏 Screen Size
* 🧠 RAM
* ⚙️ CPU
* 🎮 GPU
* 💾 Storage Capacity
* 💽 Storage Type
* 🖥️ Display Resolution
* 🪟 Operating System
* ⚖️ Weight
* 👆 Touchscreen
* 🎨 IPS Display

This project processes these features and uses a trained Machine Learning model to estimate the price of a laptop.

---

## 🚀 Features

* Interactive **Streamlit web application**
* Machine Learning based laptop price prediction
* User-friendly input interface
* Supports multiple laptop configurations
* Pre-trained Machine Learning model
* Dataset included in the repository
* Easy to run locally

---

## 🛠️ Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| 🐍 Python           | Programming language |
| 🐼 Pandas           | Data processing      |
| 🔢 NumPy            | Numerical operations |
| 🤖 Scikit-learn     | Machine Learning     |
| 🎈 Streamlit        | Web application      |
| 📦 Pickle           | Model serialization  |
| 📓 Jupyter Notebook | Model development    |

---

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

### File Description

| File                     | Description                    |
| ------------------------ | ------------------------------ |
| `app.py`                 | Streamlit web application      |
| `laptop_price.csv`       | Laptop dataset                 |
| `laptop_price_model.pkl` | Trained Machine Learning model |
| `requirements.txt`       | Required Python libraries      |
| `README.md`              | Project documentation          |

---

## 📊 Dataset

The dataset contains laptop specifications and their corresponding prices.

### Important Features

| Feature            | Description           |
| ------------------ | --------------------- |
| `Company`          | Laptop manufacturer   |
| `Product`          | Laptop model          |
| `TypeName`         | Type of laptop        |
| `Inches`           | Screen size           |
| `Ram`              | RAM capacity          |
| `OpSys`            | Operating system      |
| `Weight`           | Laptop weight         |
| `IPS`              | IPS display indicator |
| `Touchscreen`      | Touchscreen indicator |
| `Cpu`              | CPU information       |
| `Gpu`              | GPU information       |
| `Storage Capacity` | Storage size          |
| `Storage Type`     | SSD, HDD, etc.        |
| `Price_euros`      | Laptop price          |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/syedziaulhaq980/laptop-price-prediction.git
```

### 2. Navigate to the Project

```bash
cd laptop-price-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your web browser.

You can then enter the laptop specifications and receive an estimated price.

---

## 🤖 Machine Learning Model

The trained Machine Learning model is stored in:

```text
laptop_price_model.pkl
```

The Streamlit application loads this model and uses the laptop specifications entered by the user to generate a predicted price.

### Prediction Workflow

```text
Laptop Specifications
        ↓
Feature Processing
        ↓
Trained ML Model
        ↓
Price Prediction
        ↓
Estimated Laptop Price
```

---

## 🌐 Project Repository

**GitHub:**
https://github.com/syedziaulhaq980/laptop-price-prediction

---

## 👨‍💻 Author

### Syed Zia Ul Haq

Machine Learning & Data Science Project

---

⭐ If you found this project useful, consider giving the repository a star!

