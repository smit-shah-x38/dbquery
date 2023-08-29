# Imports
import tensorflow_decision_forests as tfdf
import pandas as pd
from wurlitzer import sys_pipes
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("/var/wd_smit/localdata/datasets/Dataset.csv")

# Define the feature columns
feature_columns = [
    tfdf.FeatureColumnCategorical("MSZoning"),
    tfdf.FeatureColumnNumerical("LotFrontage"),
    tfdf.FeatureColumnNumerical("LotArea"),
    tfdf.FeatureColumnCategorical("Street"),
    tfdf.FeatureColumnCategorical("Alley"),
    # Add more feature columns as needed
]

# Define the target column
target_column = tfdf.FeatureColumnNumerical("SalePrice")

# Create the training dataset
train_data = data.sample(frac=0.8, random_state=42)

# Create the validation dataset
validation_data = data.drop(train_data.index)

# Create the model
model = tfdf.keras.GradientBoostedTreesModel(task=tfdf.Task.REGRESSION)

# Train the model
model.fit(
    train_data=train_data, validation_data=validation_data, target_column=target_column
)

# Evaluate the model
model.evaluate(validation_data)

# Make predictions
predictions = model.predict(validation_data)

# Print the predictions
print(predictions)
