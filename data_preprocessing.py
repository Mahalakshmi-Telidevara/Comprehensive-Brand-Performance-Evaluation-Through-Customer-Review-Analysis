import pandas as pd

def load_and_preprocess_data(file_path):
    try:
        # Load the data from CSV
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        
        # Display the first few rows and summary of the dataset
        print("\nInitial Data Overview:")
        print(data.head())
        print("\nData Information:")
        print(data.info())
        
        # Handling missing values
        print("\nHandling missing values...")
        data['review_text'].fillna('', inplace=True)  # Fill NaNs in 'review_text' with an empty string
        data['customer_rating'] = pd.to_numeric(data['customer_rating'], errors='coerce')  # Convert to numeric
        
        # Remove rows with NaNs in 'brand_name' and other important fields
        data = data.dropna(subset=['brand_name', 'sentiment'])  # Remove rows where 'brand_name' or 'sentiment' is NaN
        
        # Informational messages about action taken
        print(f"Rows after removing NaNs in 'brand_name' and 'sentiment': {data.shape[0]}")

        # Further data preprocessing steps can be added here

        return data
    
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# File path
file_path = r'data/reviews.csv'

# Load and preprocess the data
processed_data = load_and_preprocess_data(file_path)

# If you wish, you could display the cleaned data
if processed_data is not None:
    print("\nCleaned Data Overview:")
    print(processed_data.head())
    print(f"\nFinal shape of the dataset: {processed_data.shape}")