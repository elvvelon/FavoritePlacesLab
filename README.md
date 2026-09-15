# Favorite Places Lab

A Django web application for saving favorite locations and getting recommendations for where to go based on rating.

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/elvvelon/FavoritePlacesLab.git
   cd FavoritePlacesLab
   ```
   
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install dependencies:
    ```
   
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   Apply database migrations:
   ```
   
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the local server:
    ```bash
    python manage.py runserver
    ```
Open http://127.0.0.1:8000 in your browser to view the application.