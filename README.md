## Dependencies
- Git
- PyTest
- Python 3+

## Setup and Installation
- Clone the Repository
- Pull the repository from the 'develop' branch

- Create Virtual Environment based on OS-specific requirements:
  - For Windows
    - python -m venv venv
    - .venv\Scripts\activate
    - pip install -r requirements.txt
  - For Mac
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt

## Key Files
  - app-config.ini
    - A configuration file that holds constants for all environments; like URLs, making it easy to switch between different environments
  - pytest.ini
    - A configuration file for pytest, defining markers that can be used to categorise and run specific sets of tests.