# Project: Comprehensive Brand Performance Evaluation Through Customer Review Analysis 

## Description

This project entails the development of a review analysis application designed to evaluate the performance of various brands based on customer feedback. Built using Python, the application leverages the Pandas library for data manipulation and Streamlit for crafting an interactive and user-friendly interface. It aims to provide data-driven insights to help consumers make informed decisions and businesses improve their offerings.

## Requirements

- Python 3.x
- Numpy
- Streamlit
- Matplotlib

## Setup Instructions

### 1. Install Visual Studio Code (VSCode)
If you haven’t already, [download and install Visual Studio Code](https://code.visualstudio.com/).

### 2. Install Python
Ensure that Python 3.x is installed on your system. If not, download and install it from [here](https://www.python.org/downloads/).

### 3. Clone the Project
Clone the repository or download the project files to your local system.

### 4. Install Dependencies
Install all the required packages using `pip`:
```bash
pip install -r requirements.txt
```

### 5. Running the Application
1. Run the application:
        streamlit run app.py  
2. Open the application in your browser (default: http://localhost:8501).
3. Upload the review data file or connect to the specified data source.
4. View interactive tables and performance metrics generated for each brand.


## Project Structure

```
MAIN3/
├── data/  
│   └── reviews.csv          # Dataset containing customer reviews  
├── template/  
│   └── index.html           # HTML template for visualization  
├── app.py                   # Main application file for running the Streamlit app  
├── data_collection.py       # Script for collecting review data from various sources  
├── data_preprocessing.py    # Script for cleaning and preprocessing the review data  
├── rating_prediction.py     # Script for predicting ratings based on data  
├── sentiment_analysis.py    # Script for performing sentiment analysis on reviews  
├── visualization.py         # Script for generating visualizations and interactive tables  
├── reviews.db               # Database file for storing review data (SQLite or similar)  
├── README.md                # Documentation for the project  
├── requirements.txt         # List of dependencies needed for the project  
```
