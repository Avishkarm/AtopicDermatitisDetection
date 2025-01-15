# Eczema Detection ML Project

## Repository Structure

```
eczema-detection/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/                      # Original, immutable data
│   ├── processed/                # Cleaned and processed data
│   ├── interim/                  # Intermediate processing data
│   └── external/                 # External source data
│
├── docs/
│   ├── api/                      # API documentation
│   ├── model/                    # Model architecture documentation
│   ├── preprocessing/            # Data preprocessing documentation
│   └── README.md                 # Documentation home
│
├── models/
│   ├── trained/                  # Saved model files
│   └── configs/                  # Model configuration files
│
├── notebooks/
│   ├── 1.0-data-exploration.ipynb
│   ├── 2.0-preprocessing.ipynb
│   ├── 3.0-feature-engineering.ipynb
│   └── 4.0-model-development.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── make_dataset.py
│   │   └── preprocess.py
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization/
│       ├── __init__.py
│       └── visualize.py
│
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── tox.ini
```

### Key Files Content

**README.md**
```markdown
# Eczema Detection ML Project

Machine learning model for detecting Eczema using visual indicators including Dennie-Morgan fold analysis.

## Project Overview
This project implements a machine learning solution for automated detection of Eczema through image analysis, focusing on:
- Infraorbital fold (Dennie-Morgan fold) detection
- Lower eyelid dermatitis analysis
- Pattern recognition for eczematous dermatoses

## Setup
1. Clone the repository
```bash
git clone https://github.com/username/eczema-detection.git
cd eczema-detection
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
- `data/`: Dataset storage and management
- `docs/`: Project documentation
- `models/`: Trained models and configurations
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code
- `tests/`: Unit tests

## Contributing
Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
```

**requirements.txt**
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=0.24.2
tensorflow>=2.6.0
opencv-python>=4.5.3
pillow>=8.3.1
matplotlib>=3.4.2
seaborn>=0.11.1
jupyter>=1.0.0
pytest>=6.2.4
flake8>=3.9.2
black>=21.6b0
```

**.gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Project specific
data/raw/*
data/processed/*
models/trained/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!models/trained/.gitkeep

# OS specific
.DS_Store
Thumbs.db
```

### Module Descriptions

1. **data/**: Contains all data files
   - `raw/`: Original, immutable data
   - `processed/`: Cleaned and transformed data
   - `interim/`: Intermediate transformations
   - `external/`: Data from external sources

2. **src/**: Main source code
   - `data/`: Data processing scripts
   - `features/`: Feature engineering code
   - `models/`: Model training and prediction
   - `visualization/`: Data visualization tools

3. **notebooks/**: Jupyter notebooks for:
   - Data exploration
   - Model prototyping
   - Result analysis
   - Documentation

4. **tests/**: Unit tests for all modules
   - Test data processing
   - Test feature engineering
   - Test model performance

5. **models/**: Model artifacts
   - Saved model files
   - Model configurations
   - Training checkpoints

6. **docs/**: Project documentation
   - API documentation
   - Model architecture
   - Data preprocessing steps
