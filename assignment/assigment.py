import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file with a flexible delimiter and error handling
file_path = 'D:/Python/pfad/assignment/daily_KP_MEANHKHI_2024.csv'  # Update the file path if needed
data = pd.read_csv(file_path, delimiter=None, engine='python', on_bad_lines='skip')

# Attempt to clean the dataset by filtering out non-data rows based on their structure
# Only keep rows that seem to have numeric or valid data
cleaned_data = pd.read_csv(file_path, delimiter=',', skiprows=5, on_bad_lines='skip', engine='python')

# Inspect the columns to see their actual names and adjust renaming accordingly
print(cleaned_data.columns)

# Adjust column renaming to match the actual structure
# If there are four columns, adjust accordingly
# Modify this based on the actual data structure
if len(cleaned_data.columns) == 4:
    cleaned_data.columns = ['Year', 'Month', 'Day', 'Value']
elif len(cleaned_data.columns) == 5:
    cleaned_data.columns = ['Year', 'Month', 'Day', 'Value', 'Status']

# Clean the 'Value' column by removing non-numeric entries
cleaned_data['Value'] = pd.to_numeric(cleaned_data['Value'], errors='coerce')

# Remove rows with missing or invalid 'Value' entries
cleaned_data = cleaned_data.dropna(subset=['Value'])

# Convert date columns into a datetime format after cleaning
cleaned_data['Date'] = pd.to_datetime(cleaned_data[['Year', 'Month', 'Day']])

# Plotting the cleaned data
plt.figure(figsize=(12, 6))
plt.plot(cleaned_data['Date'], cleaned_data['Value'], marker='o', linestyle='-')
plt.title('Daily Mean HKHI Values')
plt.xlabel('Date')
plt.ylabel('Mean HKHI Value')
plt.grid(True)
plt.show()
