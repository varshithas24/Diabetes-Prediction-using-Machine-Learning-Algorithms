# 🩺 Diabetes Prediction using Machine Learning

This project aims to build and compare several machine learning models for predicting the likelihood of diabetes based on patient health data. Algorithms implemented are Logistic Regression, Random Forest, K-Nearest Neighbors (KNN), and Decision Tree classifiers.

---

## 📌 Project Objective

To develop machine learning models that predict whether an individual is diabetic or not based on medical attributes, and to compare the performance of different algorithms using metrics such as accuracy, precision, recall, and F1-score.

---

## 🧠 Machine Learning Models Used

- **Logistic Regression**
- **Random Forest Classifier**
- **K-Nearest Neighbors (KNN)**
- **Decision Tree**

Each model was evaluated for performance to identify the best-suited algorithm for early diabetes detection.

---

- **Attributes**:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
  - Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## 🧹 Data Preprocessing

- Handled missing and zero values by replacing them with column means.
- Performed normalization using Min-Max Scaling.
- Removed outliers using the IQR method.
- Conducted feature correlation analysis.

---

## 📈 Implementation Overview

- **Regression**: Linear regression to analyze glucose vs outcome.
- **Clustering**: K-Means clustering for grouping similar patients.
- **Model Training**: Used `train_test_split`, model fitting, prediction, and evaluation.
- **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

---

## 🏆 Results

| Model                | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 74%      | 0.74      | 0.74   | 0.74     |
| Random Forest       | 75%      | 0.76      | 0.75   | 0.75     |
| KNN                 | 73%      | 0.73      | 0.73   | 0.73     |
| Decision Tree       | 70%      | 0.70      | 0.70   | 0.70     |

✅ **Random Forest Classifier** performed the best overall and was selected as the final model.

---
