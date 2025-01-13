import pandas as pd

def calculate_top_brands(file_path):
    """
    Calculate the top brands based on customer ratings and sentiment.

    Parameters:
    - file_path: str, the path to the CSV file containing reviews data.

    Returns:
    - top_5_brands: DataFrame containing the top 5 brands with their scores.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}. Shape: {data.shape}")

        # Check for required columns
        required_columns = ['brand_name', 'customer_rating', 'sentiment', 'review_id']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"This dataset must contain the columns: {required_columns}")

        # Sentiment mapping
        sentiment_mapping = {
            "Positive": 1,
            "Neutral": 0,
            "Negative": -1,
        }

        # Map sentiment to numeric values
        data['sentiment_value'] = data['sentiment'].map(sentiment_mapping)

        # Handle NaN values in sentiment_value
        if data['sentiment_value'].isnull().any():
            print("Warning: Some sentiment values are NaN and will be filled with 0.")
            data['sentiment_value'].fillna(0, inplace=True)
        
        # Group by brand names and calculate metrics
        top_brands = data.groupby('brand_name').agg({
            'customer_rating': 'mean',
            'sentiment_value': 'mean',
            'review_id': 'count'
        }).rename(columns={'review_id': 'review_count'})

        # Calculate score
        top_brands['score'] = (top_brands['customer_rating'] + top_brands['sentiment_value']) / 2

        # Sort and get top 5 brands
        top_5_brands = top_brands.sort_values(by='score', ascending=False).head(5)

        return top_5_brands

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
    except pd.errors.ParserError:
        print("Error: Could not parse the file.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_path = 'data/reviews.csv'
    top_5_brands = calculate_top_brands(file_path)
    
    if top_5_brands is not None:
        print("\nTop 5 Brands:")
        print(top_5_brands)  # Print only if the DataFrame is valid