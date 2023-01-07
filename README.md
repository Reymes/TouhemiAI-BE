# Setting up CHAT Backend

## Want to execute the application on Docker Compose ?

1. Make sure you have already installed both [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

2. Add your environmental variables (env.py) in the root directory of the project

3. Build and run the app with Compose:

    ```sh
    $ docker-compose build
    ```

    ```sh
    $ docker-compose up
    ```

## Want to execute the application on your local machine ?

1. Fork/Clone

2. Create and activate a virtual environment:

    ```sh
    (linux)$ python3 -m venv venv && source venv/bin/activate 
    ```
    ```sh
    (windows) python -m venv venv && source venv/Scripts/activate 
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

4. Add your config variables 

5. Run the server:

    ```sh
    (venv)$ FLASK_ENV=development python app.py
    ```

6. Navigate to [http://localhost:6010](http://localhost:6010)