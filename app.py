from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

app = Flask(__name__)

# Function to generate randomized bot and human data
def generate_data():
    np.random.seed(None)  # Ensure new random seed each time for unique results

    num_samples = 5000

    # Create bot data
    bot_data = {
        'followers_count': np.random.randint(10, 1000, size=num_samples),
        'friends_count': np.random.randint(50, 500, size=num_samples),
        'listed_count': np.random.randint(0, 10, size=num_samples),
        'favourites_count': np.random.randint(10, 200, size=num_samples),
        'statuses_count': np.random.randint(1, 200, size=num_samples),
        'label': np.ones(num_samples)  # Bot label
    }

    # Create human data
    human_data = {
        'followers_count': np.random.randint(1000, 1000000, size=num_samples),
        'friends_count': np.random.randint(200, 1000, size=num_samples),
        'listed_count': np.random.randint(1, 50, size=num_samples),
        'favourites_count': np.random.randint(50, 1000, size=num_samples),
        'statuses_count': np.random.randint(500, 100000, size=num_samples),
        'label': np.zeros(num_samples)  # Human label
    }

    # Convert to DataFrame
    bot_df = pd.DataFrame(bot_data)
    human_df = pd.DataFrame(human_data)

    # Combine bot and human data
    data = pd.concat([bot_df, human_df], ignore_index=True)

    # Shuffle the data to mix bots and humans
    data = data.sample(frac=1).reset_index(drop=True)

    # Add a unique index column
    data['index'] = data.index

    # Reorder columns to move 'index' to the first column
    columns = ['index'] + [col for col in data.columns if col != 'index']
    data = data[columns]

    # Standardize the data (scale features)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(data.drop(['label', 'index'], axis=1))

    # Apply DBSCAN for clustering
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X_scaled)

    # Add cluster labels
    data['cluster'] = dbscan_labels

    # Map clusters to bot (1) and human (0), assuming cluster 0 corresponds to humans
    data['label'] = data['cluster'].apply(lambda x: 0 if x == 0 else 1)

    # Split data into bot and human
    human_data = data[data['label'] == 0]
    bot_data = data[data['label'] == 1]

    return data.to_dict(orient='records'), human_data.to_dict(orient='records'), bot_data.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    all_data, human_data, bot_data = generate_data()
    return jsonify({
        'all_data': all_data,
        'human_data': human_data,
        'bot_data': bot_data
    })

if __name__ == '__main__':
    app.run(debug=True)
