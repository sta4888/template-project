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
   
    Этот файл содержит переменные среды, значения которых будут использоваться во всем приложении.
    Образец файла (`.env.sample`) содержит набор переменных со значениями по умолчанию. 
    Таким образом, его можно настроить в зависимости от среды..
    а если вы заливаете проект в продакшен, тогда воспользуйтесь командой

    ```shell
    cp .env.prod_sample .env
    ```
2. Создайте контейнер с помощью Docker Compose.:
    ```shell
    docker compose build
    ```
    Эту команду следует запускать из корневого каталога, где `Dockerfile` расположен.
    You also need to build the docker container again in case if you have updated `requirements.txt`.
   
3. Теперь проект можно запускать внутри Docker-контейнера.:
    ```shell
    docker compose up
    ```
   Когда контейнеры запущены, сервер запускается в [http://0.0.0.0:8000](http://0.0.0.0:8000). Вы можете открыть его в своем браузере.

4. To run application correctly set up the database using commands:
    Connect to the application Docker-container:
    ```shell
    docker compose exec app bash
    ```
   Apply migrations to create tables in the database:
    ```shell
    ./manage.py migrate
    ```
   