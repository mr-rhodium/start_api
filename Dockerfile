FROM python:3.11.0

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


WORKDIR /code
COPY . /code
RUN pip install poetry
ADD pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false && poetry config installer.max-workers 10
RUN poetry install --no-root

EXPOSE 8000