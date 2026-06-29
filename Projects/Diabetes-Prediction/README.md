# Diabetes Prediction using SVM

A machine learning model that predicts whether a patient has diabetes based on clinical diagnostic data.

## Dataset

**PIMA Indians Diabetes Dataset** — 8 input features:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin fold thickness (mm) |
| Insulin | 2-hour serum insulin (mu U/ml) |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes hereditary likelihood score |
| Age | Age in years |

**Target:** `Outcome` — `1` (Diabetic) / `0` (Non-Diabetic)

## Workflow

1. Load dataset with Pandas
2. Explore data (shape, statistics, class distribution)
3. Standardize features using `StandardScaler`
4. Split into train/test sets (80/20)
5. Train a **linear SVM** classifier
6. Evaluate accuracy on both splits
7. Run inference on a single input sample

## Results

| Split | Accuracy |
|---|---|
| Training | ~78.7% |
| Test | ~77.3% |

## Dependencies

```
numpy
pandas
scikit-learn
```

## Usage

```python
# Example prediction
input_data = (7, 196, 90, 0, 0, 39.8, 0.451, 41)
# → Output: "Patient has Diabetes"
```

> **Note:** Input must be standardized using the same `StandardScaler` fitted on training data before passing to the classifier.
