import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from a CSV file and return the DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
        return None
    except pd.errors.ParserError:
        print("Error: Could not parse the file.")
        return None

def process_data(data):
    """Process the DataFrame to calculate brand scores."""
    # Create sentiment mapping
    sentiment_mapping = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1,
    }

    # Check if sentiment column exists
    if 'sentiment' in data.columns:
        data['sentiment_value'] = data['sentiment'].map(sentiment_mapping)

    # Group by brand and calculate mean ratings
    top_brands = data.groupby('brand_name').agg({
        'customer_rating': 'mean',
        'sentiment_value': 'mean',
        'review_id': 'count'
    }).rename(columns={'review_id': 'review_count'})

    # Calculate overall score
    top_brands['score'] = (top_brands['customer_rating'] + top_brands['sentiment_value']) / 2

    # Get top 5 brands
    top_5_brands = top_brands.sort_values(by='score', ascending=False).head(5)
    return top_5_brands

def plot_top_brands(top_brands):
    """Plot the top brands based on scores."""
    ax = top_brands[['score']].plot(kind='bar', alpha=0.7, color='teal')
    
    # Customizing the plot
    plt.title('Top 5 Mobile Brands Based on Customer Ratings and Sentiment', fontsize=16)
    plt.xlabel('Brand Name', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adding score annotations
    for p in ax.patches:  # Fix the typo here
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom')

    plt.tight_layout()  # Adjust layout
    plt.show()

if __name__ == "__main__":
    file_path = r'data/reviews.csv'
    data = load_data(file_path)

    if data is not None:
        top_5_brands = process_data(data)
        plot_top_brands(top_5_brands)