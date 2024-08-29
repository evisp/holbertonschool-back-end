from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "This is the About page."


@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"


@app.route('/users')
def show_users():
    users = [
        {'name': 'John Smith', 'active': True},
        {'name': 'Jane Brown', 'active': False},
        {'name': 'James Red', 'active': True}
    ]
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)