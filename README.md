# template-project
Проект с blueprints


В нем хранятся примеры с пояснением 


## Requirements:

Установите необходимое ПО:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Installation

Склонируйте репозиторий на свой ПК или сервер

1. Для настройки конфигураций, скопируйте файл `.env.sample` в `.env` файл:
    ```shell
    cp .env.sample .env
    ```
   
    This file contains environment variables that will share their values across the application.
    The sample file (`.env.sample`) contains a set of variables with default values. 
    So it can be configured depending on the environment.

2. Build the container using Docker Compose:
    ```shell
    docker compose build
    ```
    This command should be run from the root directory where `Dockerfile` is located.
    You also need to build the docker container again in case if you have updated `requirements.txt`.
   
3. Now it is possible to run the project inside the Docker container:
    ```shell
    docker compose up
    ```
   When containers are up server starts at [http://0.0.0.0:8000](http://0.0.0.0:8000). You can open it in your browser.

4. To run application correctly set up the database using commands:
    Connect to the application Docker-container:
    ```shell
    docker compose exec app bash
    ```
   Apply migrations to create tables in the database:
    ```shell
    ./manage.py migrate
    ```
