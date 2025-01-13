import pandas as pd

# Function to load data from CSV and handle potential errors
def load_data(file_path):
    try:
        # Load the data from CSV while handling potential issues
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: No data found in the CSV file.")
    except pd.errors.ParserError:
        print("Error: There was an issue parsing the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# File path
file_path = r'data\reviews.csv'

# Load the data
data = load_data(file_path)

# Further exploration of the data if it was loaded successfully
if data is not None:
    # Display the first few rows of the DataFrame
    print(data.head())

    # Display basic information about the DataFrame
    print(data.info())

    # Describe the statistical details of the numeric columns
    print(data.describe())

    # Check for missing values
    print("Missing values in each column:")
    print(data.isnull().sum())