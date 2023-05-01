# Seller Onboarding Form

This project is a simple Flask-based web application that implements a seller onboarding form for a marketplace.

## Prerequisites
Ensure that you have the following software installed on your system:

- Python 3.6 or higher
- pip (Python package manager)
- WSL / Ubuntu (if using Windows)

## Setting Up a Virtual Environment
It is recommended to set up a virtual environment to manage the project's dependencies. Follow the instructions below to create a virtual environment and install the required packages.

1. Open a terminal (WSL / Ubuntu if using Windows).
2. Navigate to the project directory.
3. Create a virtual environment using the following command:
- python3 -m venv venv
4. Activate the virtual environment:
- For WSL / Ubuntu:
  ```
  source venv/bin/activate
  ```
- For Windows:
  ```
  venv\Scripts\activate
  ```
5. Install the required packages:
- pip install -r requirements.txt

## Running the Application
After setting up the virtual environment and installing the required packages, you can run the Flask application using the following command:
- flask run


The application will start, and you can access it at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

The project consists of the following files:

- `app.py`: The main Flask application file.
- `templates/`: A directory containing the HTML templates for the form and results pages.
  - `form.html`: The HTML template for the seller onboarding form.
  - `results.html`: The HTML template for the results page, which displays the submitted form data.
- `requirements.txt`: A file listing the required Python packages for the project.


