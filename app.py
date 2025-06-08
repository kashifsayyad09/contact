from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="contactbook"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    
    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    values = (name, phone, email)
    cursor.execute(sql, values)
    db.commit()
    
    return redirect('/view')

@app.route('/view')
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    return render_template('view.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
