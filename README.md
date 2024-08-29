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

2. **Render the Template**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
```

- `render_template('home.html')`: Renders the `home.html` template and returns it as an HTTP response.

## 7. Creating Dynamic Templates
Dynamic templates allow you to insert variables, perform loops, and use conditional statements.

### Example with Variables, Loops, and Conditions:

1. **Template File** (`templates/users.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Users</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.name }} - {% if user.active %}Active{% else %}Inactive{% endif %}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

2. **Route Handling**

```python
@app.route('/users')
def show_users():
    users = [
        {'name': 'Alice', 'active': True},
        {'name': 'Bob', 'active': False},
        {'name': 'Charlie', 'active': True}
    ]
    return render_template('users.html', users=users)
```

- Variables: `{{ user.name }}` inserts the user's name.
- Loops: `{% for user in users %}` loops through the list of users.
- Conditions: `{% if user.active %}` checks if the user is active.

## 8. Displaying Data from a MySQL Database in HTML
To connect Flask to a MySQL database and display data, follow these steps:

### 8.1. Install MySQL Connector

```python
pip install mysql-connector-python
```

### 8.2. Configure the Database Connection
import mysql.connector

# Database configuration

```python
db_config = {
    # replace with the actual username, password and database
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'sakila'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection
```

## 8.3. Fetch and Display Data:

1. Route and Data Fetching

Assuming you have a table called actors in the `sakila` database

```python
@app.route('/actors')
def fetch_actors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT actor_id, first_name, last_name FROM actor LIMIT 10")
    actors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('actors.html', actors=actors)
```

2. Template File (`templates/actors.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Actors List</title>
</head>
<body>
    <h1>Actors List</h1>
    <table>
        <tr>
            <th>Actor ID</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        {% for actor in actors %}
        <tr>
            <td>{{ actor.actor_id }}</td>
            <td>{{ actor.first_name }}</td>
            <td>{{ actor.last_name }}</td>
        </tr>
        {% endfor %}
    </table>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>

```

## Conclusion

This tutorial covered the basics of using Flask as a web framework, defining routes, working with templates, handling dynamic content, and integrating a MySQL database. With these fundamentals, you can start building more complex and robust web applications using Flask.
