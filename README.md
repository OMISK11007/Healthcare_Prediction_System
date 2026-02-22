# Dengue Decision Support System

A Streamlit-based web application for clinical decision support in dengue fever management. This system uses machine learning to classify patients and provide risk-based recommendations for hospitalization and monitoring.

## Features

- **Patient Risk Classification**: Analyzes patient vitals and symptoms to classify dengue severity
- **Clinical Recommendations**: Provides actionable clinical guidance based on risk assessment
- **Risk Visualization**: Shows risk probability trend relative to platelet count
- **Session History**: Tracks all patient assessments during a session

## System Requirements

- Python 3.8+
- Virtual environment (optional but recommended)

## Installation

1. **Clone or navigate to the project directory:**
```bash
cd "nkp pridiction model"
```

2. **Create and activate a virtual environment (recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use:

1. **Enter Patient Vitals** in the sidebar:
   - Age: 1-100 years
   - Days of Fever: 1-14 days
   - Platelet Count: Blood platelet count in cells
   - Hematocrit %: Hematocrit percentage
   - Warning Signs: Yes/No

2. **Click "Analyze Risk"** to get:
   - Clinical recommendation (CRITICAL, HIGH RISK, or STABLE)
   - Model risk confidence percentage
   - Risk trend visualization based on platelet count
   - Automatic addition to session history

## Model Details

The system uses:
- **Random Forest Classifier** with 100 estimators
- **Training Data**: Mock dataset of 10 patient records with dengue outcomes
- **Features**: Age, days of fever, platelet count, hematocrit percentage, warning signs
- **Output**: Risk probability (0-1) and clinical classification

## Risk Classification

- **CRITICAL**: Prob > 50% OR Platelet < 50,000 OR Hematocrit > 50% → **Immediate Hospitalization Required**
- **HIGH RISK**: Platelet < 100,000 → **Close Monitoring Needed**
- **STABLE**: Otherwise → **Home Management with Follow-up**

## Files

- `app.py`: Main Streamlit application
- `healthcare.py`: DengueDecisionSystem class and data functions
- `requirements.txt`: Python dependencies

## Notes

- The current model uses mock data for demonstration purposes
- For production use, replace `get_mock_data()` with real patient data
- The model should be retrained with a larger, more representative dataset
