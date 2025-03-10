import pandas as pd

# Load the data from the CSV file
df_validation = pd.read_csv("data.csv")

# Convert DateOfBirth and StudyDate to datetime objects
df_validation['DateOfBirth'] = pd.to_datetime(df_validation['DateOfBirth'])
df_validation['StudyDate'] = pd.to_datetime(df_validation['StudyDate'])

# Calculate age in years
df_validation['Age'] = (df_validation['StudyDate'] - df_validation['DateOfBirth']).dt.days / 365.25

# Create AgeCategory column
df_validation['AgeCategory'] = pd.cut(df_validation['Age'],
                                      bins=[0, 18, 55, float('inf')],
                                      labels=['Child', 'Adult', 'Senior'],
                                      right=False)

# Print the first few rows of the updated DataFrame to verify the result
print(df_validation.head())