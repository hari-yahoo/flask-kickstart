# flask-kickstart

This is a Python-based command-line tool for scaffolding a Flask project with a predefined structure. It generates a boilerplate for a Flask application, including basic configuration, routes, templates, and testing setup.

## Features
Automatically sets up a Flask project with a basic directory structure.
Includes boilerplate code for:
- app/__init__.py: Flask application factory.
- app/routes.py: Sample route with HTML template rendering.
- config.py: Configurable settings (e.g., SECRET_KEY).
- run.py: Application entry point.
- tests/test_app.py: Basic unit test for Flask routes.
- templates/base.html: Basic HTML template.
- requirements.txt: List of required dependencies (Flask, Flask-SQLAlchemy).
- Object-oriented design to ensure modularity and scalability.
## Prerequisites
Before using this tool, ensure you have the following installed:

- Python 3.6+
- Flask (pip install Flask)

## Customization
You can modify the template files in the templates/ directory to customize the structure of your Flask project.
Placeholders like {{secret_key}} in config.py.template can be dynamically replaced by the tool if needed.

## Contribution
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.