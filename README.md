# URLShortner
This is Djnago based app intended to work as URL(Uniform Resource Locator) shortner.
# URL Shortener Project

This Django-based project allows users to shorten URLs easily. It's a simple, yet effective tool for managing long URLs and tracking their usage.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django
- pip

### Setting Up the Project

#### Step 1: Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/sandesh-kun/URLShortner.git
cd URLShortner

#### Step 2: Create and Activate a Virtual Environment

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate

#### Step 3: Install Dependencies
pip install -r requirements.txt

#### Step 4: Database Migrations
python manage.py migrate

#### Step 5: Running the Server
python manage.py runserver
