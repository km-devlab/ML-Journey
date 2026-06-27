# 🪨 Rock vs Mine Prediction

A machine learning project that uses sonar signal data to classify underwater objects as either **rocks** or **mines** using Logistic Regression.

---

## 📌 Overview

This project applies binary classification to the classic **SONAR dataset**, where each sample represents sonar signals bounced off either a metal cylinder (mine) or a rock. The goal is to train a model that can distinguish between the two with high accuracy.

---

## 🧠 How It Works

1. **Load** the SONAR dataset (208 samples, 60 features each)
2. **Explore** the data with statistical summaries and label distributions
3. **Split** into training (90%) and test (10%) sets with stratification
4. **Train** a Logistic Regression model on the training data
5. **Evaluate** accuracy on both training and test sets
6. **Predict** on new sonar input data

---

## 📂 Dataset

- **Source:** [SONAR Dataset (UCI Machine Learning Repository)](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks))
- **Samples:** 208
- **Features:** 60 continuous sonar frequency response values (0.0 – 1.0)
- **Labels:**
  - `M` → Mine
  - `R` → Rock

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| NumPy | Numerical operations |
| Pandas | Data loading & analysis |
| Scikit-learn | Model training & evaluation |
| Jupyter Notebook | Development environment |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rock-vs-mine-prediction.git
cd rock-vs-mine-prediction
```

### 2. Install dependencies
```bash
pip install numpy pandas scikit-learn
```

### 3. Add the dataset
Place `sonar data.csv` in the project directory (or update the file path in the notebook).

### 4. Run the notebook
```bash
jupyter notebook Rock_vs_Mine_Prediction.ipynb
```

---

## 📊 Results

| Dataset | Accuracy |
|---|---|
| Training | ~83% |
| Test | ~76% |

> Accuracy may vary slightly based on your environment.

---

## 🔍 Making a Prediction

The notebook includes a prediction system where you can pass in 60 sonar frequency values and get a classification:

```python
input_data = (0.0374, 0.0586, ..., 0.0126)  # 60 values
# Output: 'R' → Rock | 'M' → Mine
```

---

## 📁 Project Structure
