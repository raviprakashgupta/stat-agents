import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("data.csv")

# Convert DateOfBirth and StudyDate to datetime objects
df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'])
df['StudyDate'] = pd.to_datetime(df['StudyDate'])

# Calculate the age in years
df['Age'] = (df['StudyDate'] - df['DateOfBirth']).dt.days / 365.25

# Create the AgeCategory column based on the age
df['AgeCategory'] = 'Adult'  # Default category
df.loc[df['Age'] < 18, 'AgeCategory'] = 'Child'
df.loc[df['Age'] >= 55, 'AgeCategory'] = 'Senior'

# Create the IsSmokerIndicator column based on smoking status
df['IsSmokerIndicator'] = 'No'  # Default value
df.loc[(df['SmokingStatus'] == 'Current Smoker') | (df['SmokingStatus'] == 'Former Smoker'), 'IsSmokerIndicator'] = 'Yes'

# Print the first few rows of the updated DataFrame to verify the result
print(df.head())