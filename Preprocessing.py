# -*- coding: utf-8 -*-
"""new preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18b-yGGV4DN49rv3ChsGOILVWhFpUf-UM
"""

#data cleaning and replacing empty tuples with mean values
import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Convert relevant columns to numeric (handle any unexpected types)
df[columns_with_missing_values] = df[columns_with_missing_values].apply(pd.to_numeric, errors='coerce')

# Replace zeros with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mean of each column, excluding 'Outcome'
df_filled = df.drop(columns=['Outcome']).fillna(df.mean())
print(df_filled.head(10))


df_filled.to_csv('preprocessed_data.csv', index=False)
from google.colab import files
files.download('preprocessed_data.csv')

import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Convert relevant columns to numeric (handle any unexpected types)
df[columns_with_missing_values] = df[columns_with_missing_values].apply(pd.to_numeric, errors='coerce')

# Replace zeros with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the median of each column, excluding 'Outcome'
df_filled_median = df.drop(columns=['Outcome']).fillna(df.median())
print("Filled with Median:")
print(df_filled_median.head(10))

# Save the filled DataFrame to a CSV file
df_filled_median.to_csv('preprocessed_data_median.csv', index=False)

# Download file in Google Colab
from google.colab import files
files.download('preprocessed_data_median.csv')

import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Convert relevant columns to numeric (handle any unexpected types)
df[columns_with_missing_values] = df[columns_with_missing_values].apply(pd.to_numeric, errors='coerce')

# Replace zeros with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mode of each column, excluding 'Outcome'
# Note: mode() returns a Series, we take the first value [0] for each column
df_filled_mode = df.drop(columns=['Outcome']).fillna(df.mode().iloc[0])
print("Filled with Mode:")
print(df_filled_mode.head(10))

# Save the filled DataFrame to a CSV file
df_filled_mode.to_csv('preprocessed_data_mode.csv', index=False)

# Download file in Google Colab
from google.colab import files
files.download('preprocessed_data_mode.csv')

#data integration using correlation analysis
# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace zero values with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mean of the respective columns
df_filled = df.fillna(df.mean())

# Calculate the correlation matrix
correlation_matrix = df_filled.corr()

# Plot the correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Find the highest correlations with "Outcome" (diabetes indicator)
outcome_correlations = correlation_matrix["Outcome"].drop("Outcome").sort_values(ascending=False)

# Generate an analysis based on the highest correlations with "Outcome"
analysis = "Key Analysis of Correlation Findings:\n"
for feature, corr_value in outcome_correlations.items():  # Changed iteritems() to items()
    if corr_value >= 0.4:
        analysis += f"- {feature} has a strong positive correlation with Outcome ({corr_value:.2f}), suggesting that higher {feature.lower()} levels may increase the likelihood of diabetes.\n"
    elif 0.2 <= corr_value < 0.4:
        analysis += f"- {feature} shows a moderate positive correlation with Outcome ({corr_value:.2f}), implying that higher {feature.lower()} values might be linked to a higher risk of diabetes.\n"
    else:
        analysis += f"- {feature} has a weaker positive correlation with Outcome ({corr_value:.2f}), indicating a slight association with diabetes risk.\n"

print(analysis)

#data transformation using normalisation
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace zero values with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mean of the respective columns
df_filled = df.fillna(df.mean())

# Normalizing the data (excluding the 'Outcome' column)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df_filled.drop(columns=['Outcome']))

# Create a new DataFrame with the normalized data
df_normalized = pd.DataFrame(normalized_data, columns=df_filled.columns[:-1])

# Display the first few rows of the normalized dataframe
print(df_normalized.head())

#data transformation using principal component analysis
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace zero values with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mean of the respective columns
df_filled = df.fillna(df.mean())

# Standardizing the data
features = df_filled.drop(columns=['Outcome'])  # Exclude the target column 'Outcome'
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Perform PCA
pca = PCA(n_components=2)  # Reducing to 2 components for easy visualization
principal_components = pca.fit_transform(scaled_features)

# Create a dataframe with the principal components
pca_df = pd.DataFrame(data=principal_components, columns=['Principal Component 1', 'Principal Component 2'])

# Plot the explained variance ratio for each component
plt.figure(figsize=(6, 4))
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.7)
plt.title('Explained Variance Ratio by Principal Components')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.show()

# Scatter plot of the first two principal components
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Principal Component 1', y='Principal Component 2', data=pca_df)
plt.title('PCA: Principal Component 1 vs Principal Component 2')
plt.show()

#data reduction using outlier analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Columns that need missing value handling (non-sensible zeros)
columns_with_missing_values = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# Replace zero values with NaN for appropriate columns
df[columns_with_missing_values] = df[columns_with_missing_values].replace(0, pd.NA)

# Fill missing values with the mean of the respective columns
df_filled = df.fillna(df.mean())

# Function to detect and remove outliers using the IQR method
def remove_outliers_iqr(dataframe):
    Q1 = dataframe.quantile(0.25)
    Q3 = dataframe.quantile(0.75)
    IQR = Q3 - Q1
    # Filter rows that are within the acceptable IQR range
    df_outliers_removed = dataframe[~((dataframe < (Q1 - 1.5 * IQR)) | (dataframe > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Identify outliers
    outliers = dataframe[((dataframe < (Q1 - 1.5 * IQR)) | (dataframe > (Q3 + 1.5 * IQR))).any(axis=1)]

    return df_outliers_removed, outliers

# Remove outliers from the dataset and identify them
df_no_outliers, outliers = remove_outliers_iqr(df_filled)

# Print the outliers
print("Outliers:")
print(outliers)

# Generate box plots for each numeric column
plt.figure(figsize=(15, 10))
df_no_outliers.boxplot(column=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
plt.title('Box Plots of Columns After Removing Outliers')
plt.xticks(rotation=45)
plt.show()

#data visualisation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('/content/diabetes.csv')

# Replace zeros with np.nan in specific columns to indicate missing data
df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

# Use SimpleImputer to fill missing values (with the mean of the columns)
imputer = SimpleImputer(strategy='mean')
df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = imputer.fit_transform(df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])

# Step 1: Bar graph for the distribution of 'Outcome' (0 or 1)
plt.figure(figsize=(7, 5))
sns.countplot(x='Outcome', data=df)
plt.title('Distribution of Diabetes Outcome')
plt.xlabel('Outcome (0 = No Diabetes, 1 = Diabetes)')
plt.ylabel('Count')
plt.show()

# Step 2: Bar graph showing average values of features for each Outcome class
# Group data by 'Outcome' and calculate the mean of each feature
grouped_data = df.groupby('Outcome').mean()

# Plot bar graph for each feature's mean value
grouped_data.T.plot(kind='bar', figsize=(12, 6))
plt.title('Mean Values of Features by Outcome')
plt.xlabel('Features')
plt.ylabel('Mean Value')
plt.xticks(rotation=45)
plt.legend(title='Outcome', loc='upper right')
plt.show()

# Step 3: Bar graph for the correlation between features and 'Outcome'
correlation = df.corr()['Outcome'].sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=correlation.index, y=correlation.values)
plt.title('Correlation of Features with Outcome')
plt.xlabel('Features')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45)
plt.show()

from google.colab import files
import pandas as pd

# Step 1: Upload the CSV files
uploaded = files.upload()

# Step 2: Load the datasets into DataFrames
diabetes_df = pd.read_csv('diabetes.csv')
preprocessed_df = pd.read_csv('preprocessed_data.csv')

# Display original data
print("Diabetes Data:")
print(diabetes_df.head())  # Display the first few rows of the diabetes dataset

print("\nPreprocessed Data:")
print(preprocessed_df.head())  # Display the first few rows of the preprocessed dataset

# Step 3: Binning the Age column in the original dataset
diabetes_df['Age_bin'] = pd.cut(diabetes_df['Age'], bins=3, labels=["Young", "Middle-aged", "Old"])
print("\nDiabetes Data after Binning Age:")
print(diabetes_df[['Age', 'Age_bin']].head())

# Step 4: Binning the Age column in the preprocessed dataset
preprocessed_df['Age_bin'] = pd.cut(preprocessed_df['Age'], bins=3, labels=["Young", "Middle-aged", "Old"])
print("\nPreprocessed Data after Binning Age:")
print(preprocessed_df[['Age', 'Age_bin']].head())

# Binning the Age column in original and preprocessed datasets

# For original dataset
df['Age_bin'] = pd.cut(df['Age'], bins=3, labels=["Young", "Middle-aged", "Old"])
print(df[['Age', 'Age_bin']].head())

# For preprocessed dataset
df_preprocessed['Age_bin'] = pd.cut(df_preprocessed['Age'], bins=3, labels=["Young", "Middle-aged", "Old"])
print(df_preprocessed[['Age', 'Age_bin']].head())

#REGRESSION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Select predictor and target variables
X = df[['Glucose']]  # Predictor
y = df['Outcome']    # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

# Plotting the results
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Glucose')
plt.ylabel('Outcome')
plt.title('Glucose vs Outcome')
plt.legend()
plt.show()

#CLUSTER ANALYSIS
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('diabetes.csv')

# Select features for clustering
features = df[['Glucose', 'BMI', 'Insulin']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Determine the optimal number of clusters using the Elbow method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow curve
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# From the elbow curve, choose the optimal number of clusters (let's say it's 3)
optimal_clusters = 3

# Fit the KMeans model
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(features_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df['Glucose'], df['BMI'], c=df['Cluster'], cmap='viridis', marker='o')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.title('K-Means Clustering of Diabetes Data')
plt.colorbar(label='Cluster')
plt.show()