# Flask Web Framework Tutorial

## Introduction

Flask is a **lightweight web framework for Python that allows you to build web applications quickly and with minimal boilerplate code**. It's an excellent choice for both small and large projects due to its *simplicity* and *flexibility*.

In this tutorial, we will cover:

1. What is a Web Framework?
2. How to Build a Web Application with Flask
3. Defining Routes in Flask
4. Handling Variables in a Route
5. What is a Template?
6. Creating HTML Responses with Templates
7. Creating Dynamic Templates
8. Displaying Data from a MySQL Database in HTML

## 1. What is a Web Framework?
A **web framework is a collection of tools and libraries that help developers build web applications** quickly and efficiently. Web frameworks handle common tasks such as *routing URLs to code, rendering HTML templates, managing HTTP requests and responses*, and more.

### Examples of Web Frameworks:
- `Flask`: A micro-framework for Python, known for its simplicity.
- `Django`: A more feature-rich, all-in-one framework for Python.
- `Express`: A minimal web framework for `Node.js`.

### Why Use a Web Framework?
Using a web framework allows you to **focus on the unique aspects of your application, while the framework handles the repetitive and complex tasks** associated with web development.

## 2. How to Build a Web Application with Flask

To build a web application using Flask, follow these steps:

### 2.1. Install Flask
First, you need to install Flask using pip:
```python
pip install flask
```

### 2.2. Create a Simple Flask Application
Create a new Python file named app.py and add the following code:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

- **Flask Import**: We import the `Flask` class from the `flask` module.
- **App Instance**: We create an instance of the `Flask` class.
- **Route Definition**: The `@app.route('/')` decorator defines the home page route.
- **Run the App**: The `app.run()` method starts the development server.

### Run the Application
To run the application, use:
```python
python3 app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/` to see `"Hello, Flask!"` displayed.

## 3. Defining Routes in Flask
 
### What is a Route?
A **route in Flask is a URL pattern that is associated with a particular function**. When a user visits a URL, Flask invokes the function linked to that route.

### Example of Route Definition

```python
@app.route('/about')
def about():
    return "This is the About page."
```
- `@app.route('/about')`: This decorator maps the URL `/about` to the `about()` function.

In this example, visiting `http://127.0.0.1:5000/about` will trigger the `about()` function and return `"This is the About page."`

## 4. Handling Variables in a Route
You can capture variables from the URL and pass them to your functions.

### Example of Variables in a Route

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"
```

- `<username>`: A dynamic component in the URL that Flask captures and passes as an argument to the `show_user_profile()` function.

Visiting `http://127.0.0.1:5000/user/John` will display `"User: John"`

## 5. What is a Template?

A template is an **HTML file that contains placeholders for dynamic content**. Flask uses the `Jinja2` template engine to render templates with data passed from the Flask app.

## 6. Creating HTML Responses with Templates
Instead of returning plain text, you can return a rendered HTML template.

### Example:

1. **Create a Template**: Create a directory named `templates`, and inside it, create a file named `home.html`.

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Flask</h1>
</body>
</html>
```