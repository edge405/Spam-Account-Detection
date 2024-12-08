e# Spam Account Detection in Social Networks Using DBSCAN Clustering Algorithm

This application demonstrates how to detect spam accounts in social networks using the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) clustering algorithm. It leverages various features from user profiles, such as followers count, friends count, and statuses count, to classify accounts as "Human" or "Bot" (Spam).

## Features

- **Data Generation**: The application generates synthetic user data representing human and bot accounts, including various social network statistics.
- **DBSCAN Clustering**: It uses the DBSCAN algorithm to cluster users and classify them as human or bot accounts based on their activity patterns.
- **Interactive Interface**: A web interface built with Flask to dynamically generate and display data tables for human and bot accounts.
- **Indexing**: Each generated account is assigned a unique index, which is displayed first in the data table.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies Used](#technologies-used)
4. [File Structure](#file-structure)

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/edge405/Spam-Account-Detection.git
   cd Spam-Account-Detection
   ```

2. **Install dependencies**:
   Install the required Python dependencies using `pip`. You can use a `virtualenv` for a clean environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Mac/ios, use `source venv/bin/activate`
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   Start the Flask server:

   ```bash
   python app.py
   ```

4. Open the application in your browser:
   ```bash
   http://127.0.0.1:5000/
   ```

## Usage

### 1. **Home Page (`/`)**

- When you navigate to the home page, you’ll be presented with a "Generate Data" button that triggers the generation of synthetic data. This data includes various attributes like followers, friends, and statuses counts for both human and bot accounts.

### 2. **Generate Data**

- Clicking the "Generate Data" button will generate and display tables for:
  - **All Data**: A comprehensive table combining both human and bot accounts.
  - **Human Data**: A table containing data for human accounts only.
  - **Bot Data**: A table containing data for bot (spam) accounts only.

### 3. **Data Table**

- The data is dynamically displayed in tables. When you want to randomize the data just click generate data button, it will do the job randomizing the data.
- The application uses DBSCAN clustering to classify accounts, with bot accounts being marked based on clustering results.

## Technologies Used

- **Backend**:
  - **Flask**: A Python web framework used to serve the application.
  - **Pandas**: For data manipulation and creating synthetic datasets.
  - **NumPy**: For generating random numbers and performing numerical operations.
  - **Scikit-learn**: For the DBSCAN clustering algorithm and feature scaling.
- **Frontend**:
  - **HTML/CSS**: For basic structure and styling.
  - **JavaScript**: For handling user interactions (e.g., button clicks to generate data).
  - **Bootstrap**: For responsive and clean table designs.

## File Structure

```plaintext
/Spam-Account-Detection
├── static/                # Static files such as CSS, images, and JavaScript
│   ├── css/               # CSS styles
│   ├── js/                # JavaScript files (e.g., script.js)
├── templates/             # HTML templates
│   └── index.html         # Main page to generate and display data
├── app.py                 # Flask backend to handle routes and data generation
├── README.md              # This README file
└── requirements.txt       # Python dependencies

```

### `app.py`

- Contains the backend logic for generating the synthetic data, clustering it using DBSCAN, and serving it to the frontend.

### `requirements.txt`

```plaintext
Flask==3.1.0
pandas==2.2.3
numpy==2.1.3
scikit-learn==1.5.2
```

### `index.html`

- Contains the structure of the web page, including the "Generate Data" button and tables for displaying the results.

### `script.js`

- Handles the dynamic rendering of the tables and fetching data from the Flask backend.
