# README
Template Engine to create and retrieve customer templates.

### Installation
Install dependencies through `pip install requirements.txt`

### Running
1. Change directory to `website`.
2. Run server through `python manage.py runserver` command.

### Structure
1. The project is at `website`.
2. The Template Engine app is at `website/te`.
3. The MongoDB is hosted on cloud in a Mongo Atlas cluster.
4. The app's logic is broken down into
    1. `views.py` handles the logic for url endpoints.
    2. `view_models.py` acts as the bridge between the view layer and the model layer, It handles the high-level model needs of the view.
    3. `template_engine_model.py` handles the low level transactions with the database.
5. Unit tests for the code are present in `te/tests`
    
### Helpers
1. `main.py` file contains helper functions to send requests to the server.
2. Run the django server before using the helper functions.