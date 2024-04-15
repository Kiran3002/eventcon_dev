from flask import Flask, jsonify, render_template, request
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Define database connection parameters
DB_NAME = 'Kiran'
DB_USER = 'Kiran'
DB_PASSWORD = 'goneMad@1900'
DB_HOST = 'local_pgdb'
DB_PORT = '5432'

# Define a function to connect to the PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    # Extract data from the form
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Establish a database connection
    conn = connect_to_db()
    cur = conn.cursor()

    # Insert data into the database
    insert_query = sql.SQL("INSERT INTO contact_detail (name, email, subject,message) VALUES (%s, %s, %s,%s)")
    data = (name, email, subject,message)
    cur.execute(insert_query, data)
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()

    # Return a JSON response indicating success
    return jsonify({'message': 'Contact details submitted successfully'})

   

if __name__ == '__main__':
    app.run(debug=True)
