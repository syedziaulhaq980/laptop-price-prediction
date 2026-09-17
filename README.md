\# 💻 Laptop Price Prediction



A Machine Learning web application that predicts laptop prices based on hardware and configuration features. The project uses a trained machine learning model and a Streamlit interface to provide interactive price predictions.



\## 📌 Project Overview



Laptop prices depend on several factors such as:



\* Brand

\* Laptop type

\* Screen size

\* RAM

\* Operating system

\* Weight

\* CPU

\* GPU

\* Storage capacity

\* Storage type

\* Display resolution

\* Touchscreen support

\* IPS display



This project uses these features to predict the estimated price of a laptop.



\## 🚀 Features



\* Interactive Streamlit web application

\* Laptop price prediction using a trained ML model

\* User-friendly input interface

\* Supports multiple laptop specifications

\* Pre-trained model stored as a `.pkl` file

\* Dataset included for reference



\## 🛠️ Technologies Used



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Streamlit

\* Pickle

\* Jupyter Notebook



\## 📂 Project Structure



```text

laptop-price-prediction/

│

├── app.py

├── laptop\_price.csv

├── laptop\_price\_model.pkl

├── requirements.txt

└── README.md

```



\## 📊 Dataset



The dataset contains laptop specifications and their corresponding prices.



Important features include:



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

| Price\_euros      | Laptop price          |



\## ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/syedziaulhaq980/laptop-price-prediction.git

```



Move into the project directory:



```bash

cd laptop-price-prediction

```



Install the required dependencies:



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



Start the Streamlit application using:



```bash

streamlit run app.py

```



The application will open in your browser.



\## 🤖 Machine Learning Model



The trained model is saved as:



```text

laptop\_price\_model.pkl

```



The Streamlit application loads this model and uses the user's laptop specifications to generate a predicted price.



\## 📈 Example Workflow



```text

Laptop Specifications

&#x20;       ↓

Feature Processing

&#x20;       ↓

Trained ML Model

&#x20;       ↓

Price Prediction

&#x20;       ↓

Predicted Laptop Price

```



\## 🌐 Project Repository



GitHub:



https://github.com/syedziaulhaq980/laptop-price-prediction



\## 👨‍💻 Author



\*\*Syed Zia Ul Haq\*\*



Machine Learning / Data Science Project



