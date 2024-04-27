
assignment 1 and 2 is skillforge 1-2
Django Blog API

This is a Django project that provides a RESTful API for a simple blogging platform. Users can create, read, update, and delete blog posts, as well as comment on posts. Additionally, the project includes search functionality to allow users to search for specific blog posts based on categories.

Installation

Prerequisites

- Python 3.x
- pip

Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd django-blog-api
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv env
    ```


4. Activate the virtual environment:

    ```bash
    source env/bin/activate   # for Unix/Mac
    env\Scripts\activate      # for Windows
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

 Usage
Running the server

To start the Django development server, run:

```bash
python manage.py runserver
```

The API will be available at  `http://localhost:8000/` using swagger.
The API doc will be available at `http://127.0.0.1:8000/redoc`.

