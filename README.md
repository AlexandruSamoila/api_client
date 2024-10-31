# API Client

This application is a Python client that interacts with the JSONPlaceholder API using three endpoints: '/users', '/posts' and '/comments'. It includes methods to fetch, create, update and delete data.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/AlexandruSamoila/api_client.git
   ```

2. Create a virtual environment:

   ```
   python3 -m venv <venv_name>
   ```

3. Activate the virtual environment:

   ```
   source <venv_name>/bin/activate
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the application, you can run the main script:

```
python3 main.py
```

## Type checks with mypy

Use Mypy to check for type errors in the code:

```
mypy <file_name>.py
```

## Running tests

To run the tests, use the following command:

```
pytest
```

To run the tests with coverage report, use the following command:

```
pytest --cov=app --cov-report=xml --cov-report=term-missing
```
