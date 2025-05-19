# Heart Attack Predictor

A web application that predicts the likelihood of a heart attack based on user input, using a machine learning model trained on the [Heart Attack Analysis & Prediction Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset).

## Features

- User-friendly web interface built with Flask
- Predicts heart attack risk using a Random Forest model
- Data preprocessing and model training in Jupyter Notebook

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Heart-Attack-Predictor.git
   cd Heart-Attack-Predictor
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download the dataset:**
   - Download the dataset from [Kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)
   - Place heart.csv in the project root directory.
5. **Train the model:**
    - Open ml_heart.ipynb in Jupyter Notebook or VS Code
    - Run all cells to train and save RF_model.pkl
6. **Run the Flask app:**
    ```bash
    flask --app app run
    ```
    - Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser

### Project Structure
```
.
├── app.py                # Flask web app
├── ml_heart.ipynb        # Model training notebook
├── RF_model.pkl          # Saved Random Forest model (not tracked by git)
├── heart.csv             # Dataset (not tracked by git)
├── templates/
│   ├── index.html
│   └── result.html
├── .gitignore
└── README.md
```
### Dependencies
- Flask
- pandas
- scikit-learn
- seaborn (for EDA)
- maatplotlib (for plotting)
