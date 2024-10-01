# Flask Project Scaffold Tool

## Overview
Flask Project Scaffold Tool is a Python-based CLI tool that helps you quickly bootstrap a Flask web application with a predefined directory structure and boilerplate code. This tool generates the essential components needed to kickstart a Flask project with a minimal setup, saving time for developers by automating repetitive tasks.

Whether you're building a new web app or starting a quick prototype, this tool will give you a clean, organized foundation to build upon.

## Features
- Automated Flask project setup: Get up and running quickly with a ready-to-use Flask project structure.
- Predefined Directory Structure: Includes common directories for static files, templates, configuration, and tests.
- Boilerplate Code: Generates basic files like __init__.py, routes.py, config.py, and requirements.txt.
- Unit Testing Ready: Comes with a basic testing setup to test your Flask app.

## Project Structure
Here’s the project structure that will be generated:
```
your_project_name/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   └── base.html
├── config.py
├── run.py
├── tests/
│   └── test_app.py
└── requirements.txt
```

## 📁 Project Templates
The tool uses the following templates stored under the templates/ folder:

- __init__.tmpl: Initializes the Flask app.
- routes.tmpl: Sample routes and view functions.
- config.tmpl: Configuration file with placeholders for SECRET_KEY.
- base.tmpl: Basic HTML structure.
- test_app.tmpl: Boilerplate for unit testing the Flask app. (will be added soon)

These templates are easy to customize if you want to modify the generated code or structure.

## 🔧 Customization
You can modify the generated files or the scaffold templates to better suit your needs. 
'--setting' option allows you to provide a JSON file to customize the project. Please see the format of the JSON below.

```
{
    "project": {
      "name": "NewAppGenerated",
      "author": "Harikumar G",
      "description": "Generated using Kickstarter",  
      "blueprints": ["main", "auth"]
    },
    "outputFolder" : "generated"
  }
```

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact
For questions, feel free to reach out to the project maintainer at:

Email: hgokulam@yahoo.com
GitHub: @hari-yahoo
