## Installation and repository 

To run the project locally, follow these steps:
1. Clone the repository:
    ```
   git clone <repository_url>
    cd <repository_name>
    ```

2. Create and activate a virtual environment:

    ```
       pip install poetry
       poetry install
    ```

   Install poetry plugin `poetry-plugin-dotenv`

    ```
     poetry self add poetry-plugin-dotenv
    ```

3. Set up the environment variables:
   - Copy the `example.env` file and rename it to  `.env`
   - Edit the `.env` file to include your PostgreSQL connection information:
   ```dockerignore
    DATABASE_URL=postgresql://<username>@localhost/star_wars
   ```
5. Set up database (using Alembic for migrations):
  
    ```
    poetry run  alembic revision -m "create  table"
    poetry run alembic upgrade head
    ```
6. Start the FastAPI application:
   ```
    poetry run uvicorn main:app --reload
   ```
## Using Docker-Composer

     docker-compose up --build
ПШ
You can visit docs : `http://127.0.0.1:8000/docs`

## Run Test
To run all tests
```
pytest

```

To run `unit tests`:
```
pytest tests/unit_tests/
```
To run `integration tests`:
```
pytest tests/integration_tests/

```