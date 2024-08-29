from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'sakila'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def home():
    return render_template('home_old.html')


@app.route('/films')
def fetch_films():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT film_id, title, description FROM film LIMIT 10")
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('films.html', films=films)

@app.route('/actors')
def fetch_actors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT actor_id, first_name, last_name FROM actor LIMIT 10")
    actors = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('actors_old.html', actors=actors)

@app.route('/film/<int:film_id>')
def fetch_film_details(film_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT film_id, title, description, release_year, language_id, original_language_id, rental_duration, 
               rental_rate, length, replacement_cost, rating, special_features, last_update
        FROM film
        WHERE film_id = %s
    """, (film_id,))
    film = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if film is None:
        return "Film not found", 404
    
    return render_template('film_details.html', film=film)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
