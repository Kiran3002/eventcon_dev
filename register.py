import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

# Define your PostgreSQL connection parameters
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Kiran'
DB_USER = 'Kiran'
DB_PASSWORD = 'goneMad@1900'


@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Insert user data into the database
    try:
        cursor.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()
        return "Registration successful!"
    except Exception as e:
        conn.rollback()
        return f"Error: {str(e)}"
    finally:
        cursor.close()
        conn.close()

# Define the route to render the registration form
@app.route('/')
def registration_form():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)