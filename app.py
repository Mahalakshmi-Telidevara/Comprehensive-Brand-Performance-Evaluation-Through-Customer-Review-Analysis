import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Function to calculate top brands
def calculate_top_brands(data):
    # Sentiment mapping
    sentiment_mapping = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1,
    }

    # Check if sentiment exists
    if 'sentiment' in data.columns:
        data['sentiment_value'] = data['sentiment'].map(sentiment_mapping)

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

# Set up the Streamlit app
st.title('Top 5 Mobile Brands Based on Customer Ratings and Sentiment')

# Load the data
data_path = 'data/reviews.csv'
data = pd.read_csv(data_path)

# Display current top brands
st.subheader("Current Top 5 Brands")
top_5_brands = calculate_top_brands(data)
st.dataframe(top_5_brands)

# User inputs for brand name, review text, rating, sentiment, and date
brand_name = st.selectbox("Select a Brand:", data['brand_name'].unique())
review_text = st.text_area("Write your review:")
customer_rating = st.slider("Enter your rating (1 to 5):", 1, 5, 3)
sentiment_choice = st.selectbox("Select your sentiment:", ["Positive", "Neutral", "Negative"])
review_date = st.date_input("Select the date of your review:", pd.Timestamp.now())

# Button to submit the review
if st.button("Submit Review"):
    if review_text.strip() == "":
        st.warning("Please enter a review text.")
    else:
        # Update the DataFrame with new review data
        new_review = pd.DataFrame({
            'brand_name': [brand_name],
            'review_text': [review_text],
            'customer_rating': [customer_rating],
            'sentiment': [sentiment_choice],
            'review_id': [len(data) + 1],  # Unique review ID, just for simplicity
            'review_date': [review_date]  # Add review date
        })

        # Append new review to existing data
        data = pd.concat([data, new_review], ignore_index=True)

        # Save updated data to CSV
        data.to_csv(data_path, index=False)

        # Recalculate top brands with updated data
        top_5_brands = calculate_top_brands(data)

        # Create a bar plot using matplotlib
        fig, ax = plt.subplots()
        top_5_brands[['score']].plot(kind='bar', alpha=0.7, ax=ax)
        ax.set_title('Top 5 Mobile Brands')
        ax.set_xlabel('Brand Name')
        ax.set_ylabel('Score')
        ax.set_xticklabels(top_5_brands.index, rotation=45)

        # Display the plot in Streamlit
        st.pyplot(fig)

        # Show updated top brands
        st.subheader("Updated Top 5 Brands")
        st.dataframe(top_5_brands)