# Dockerized Flask App with Redis

This project demonstrates a simple Flask application that uses Redis to count the number of times a page has been accessed. The application is containerized using Docker, making it easy to deploy and run in any environment.

## Features

- **Flask**: A lightweight WSGI web application framework in Python.
- **Redis**: An in-memory data structure store, used as a database, cache, and message broker.
- **Docker**: Containerization platform to package the application and its dependencies.

## How It Works

1. The Flask application serves a single page.
2. Each time the page is accessed, the application increments a counter stored in Redis.
3. The current count is displayed on the page.

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/Ammari-Youssef/dockerized-flask-redis.git
    cd dockerized-flask-redis
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Open your web browser and navigate to `http://localhost:5000` to see the page and the access count.

## Project Structure

- `app.py`: The main Flask application.
- `Dockerfile`: Instructions to build the Flask application container.
- `docker-compose.yml`: Configuration for Docker Compose to set up the Flask and Redis services.
