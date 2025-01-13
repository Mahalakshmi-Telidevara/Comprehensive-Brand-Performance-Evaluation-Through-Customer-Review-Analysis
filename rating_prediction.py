import pandas as pd
import os

def load_data(file_path):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path} with shape {data.shape}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
    except pd.errors.ParserError:
        print("Error: Could not parse the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def clean_data(data):
    """Perform basic data cleaning."""
    # Convert 'customer_rating' to numeric and coerce errors.
    data['customer_rating'] = pd.to_numeric(data['customer_rating'], errors='coerce')
    
    # Drop rows with NaN values in 'customer_rating' or 'review_text'.
    initial_shape = data.shape
    data.dropna(subset=['customer_rating', 'review_text'], inplace=True)
    
    print(f"Data cleaning completed. Dropped {initial_shape[0] - data.shape[0]} rows with missing values.")
    
    # Optionally: Reset index after dropping rows
    data.reset_index(drop=True, inplace=True)
    return data

def predict_ratings(cleaned_data):
    """Placeholder function for rating prediction."""
    # Here you can implement your model logic.
    print("Predicting ratings...") 
    # Example: Add a prediction column for illustration purposes
    cleaned_data['predicted_rating'] = cleaned_data['customer_rating'] + 0.5  # Dummy prediction logic
    return cleaned_data

def main():
    # Check the current working directory 
    print("Current Working Directory:", os.getcwd())

    # Define the file path
    file_path = 'data/reviews.csv'
    
    # Load the data
    data = load_data(file_path)

    if data is not None and not data.empty:
        # Clean the data and define cleaned_data
        cleaned_data = clean_data(data)
        
        # Now cleaned_data is defined, so we can use it in our prediction function
        model = predict_ratings(cleaned_data)
        
        # Display the cleaned data head
        print("\nCleaned Data Overview:")
        print(model.head())
    else:
        print("No data available to process.")

if __name__ == "__main__":
    main()