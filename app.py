from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, static_url_path='/static')

# Database connection settings
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'Kiran'
DB_USER = 'Kiran'
DB_PASSWORD = 'goneMad@1900'

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
            )
            cur = conn.cursor()

            # Insert data into the database
            cur.execute(
                "INSERT INTO contact_detail (name, email, subject, message) VALUES (%s, %s, %s, %s)",
                (name, email, subject, message)
            )
            conn.commit()

            # Close connection
            cur.close()
            conn.close()

            return "Contact details submitted successfully!"
        except Exception as e:
            return "Error: " + str(e)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
