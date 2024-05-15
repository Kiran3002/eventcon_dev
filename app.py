from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app = Flask(__name__)

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_NAME = 'Kiran'
DB_USER = 'Kiran'
DB_PASSWORD = 'goneMad@1900'

# Connect to PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print("Database connection error:", e)
        return None

@app.route('/')
def demo1():
    return render_template('demo1.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO registration (username, email, password) VALUES (%s, %s, %s)", 
                            (username, email, hashed_password))
                conn.commit()
                cur.close()
                conn.close()
                # Redirect to login page after registration
                return redirect(url_for('login'))
            except psycopg2.Error as e:
                print("Error while inserting data:", e)
                conn.rollback()
                cur.close()
                conn.close()
                error = "An error occurred while registering. Please try again."
                return render_template('register.html', error=error)
        else:
            error = "Database connection error. Please try again later."
            return render_template('register.html', error=error)

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT password FROM registration WHERE username = %s", (username,))
                result = cur.fetchone()
                cur.close()
                conn.close()
                if result and check_password_hash(result[0], password):
                    # If login is successful, redirect to index page
                    return redirect(url_for('demo1'))
                else:
                    error = "Invalid username or password. Please try again."
                    return render_template('login.html', error=error)
            except psycopg2.Error as e:
                print("Error while fetching data:", e)
                conn.close()
                error = "An error occurred while logging in. Please try again."
                return render_template('login.html', error=error)
        else:
            error = "Database connection error. Please try again later."
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO queries (name, email, subject, message) VALUES (%s, %s, %s, %s)", 
                            (name, email, subject, message))
                conn.commit()
                cur.close()
                conn.close()
                # Optionally, you can redirect to a success page
                #return render_template('query_success.html', name=name, email=email, subject=subject, message=message)
            except psycopg2.Error as e:
                print("Error while inserting query:", e)
                conn.rollback()
                cur.close()
                conn.close()
                error = "An error occurred while submitting the query. Please try again."
                return render_template('contact.html', error=error)
        else:
            error = "Database connection error. Please try again later."
            return render_template('contact.html', error=error)

    return render_template('contact.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        contact_number = request.form['contact_number']
        no_of_tickets = request.form['no_of_tickets']
        payment_method = request.form['payment_method']

        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO bookings (name, contact_number, no_of_tickets, payment_method) VALUES (%s, %s, %s, %s)", 
                            (name, contact_number, no_of_tickets, payment_method))
                conn.commit()
                cur.close()
                conn.close()
                # Optionally, you can redirect to a success page
                return redirect(url_for('payment'))
            except psycopg2.Error as e:
                print("Error while inserting booking data:", e)
                conn.rollback()
                cur.close()
                conn.close()
                error = "An error occurred while booking tickets. Please try again."
                return render_template('booking.html', error=error)
        else:
            error = "Database connection error. Please try again later."
            return render_template('booking.html', error=error)

    # Redirect to the booking page if accessed directly via GET method
    return render_template('booking.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        card_number = request.form['cardNumber']
        card_holder = request.form['cardHolder']
        expiry_date = request.form['expiryDate']
        cvv = request.form['cvv']

        conn = connect_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO payment (card_number, card_holder, expiry_date, cvv) VALUES (%s, %s, %s, %s)", 
                            (card_number, card_holder, expiry_date, cvv))
                conn.commit()
                cur.close()
                conn.close()
                # Redirect to booking success page after payment
                return redirect(url_for('demo1'))
            except psycopg2.Error as e:
                print("Error while inserting payment data:", e)
                conn.rollback()
                cur.close()
                conn.close()
                error = "An error occurred while processing the payment. Please try again."
                return render_template('payment.html', error=error)
        else:
            error = "Database connection error. Please try again later."
            return render_template('payment.html', error=error)

    return render_template('payment.html')


if __name__ == '__main__':
    app.run(debug=True)
