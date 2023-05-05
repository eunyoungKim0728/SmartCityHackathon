from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for
import pymysql
import requests
from module import dbModule

app = Flask(__name__, static_folder='static', template_folder='templates')


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'prescriptxn'
}

# Connect to MySQL
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

#route
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        gender = request.form.get('gender')
        birthday = request.form.get('birthday')
        address = request.form.get('address')
        city = request.form.get('city')
        province = request.form.get('province')
        postal_code = request.form.get('postalCode')
        email = request.form.get('email')

        # Insert data into users table
        db = pymysql.connect(**db_config)
        cursor = db.cursor()
        sql = "INSERT INTO users (firstName, lastName, gender, birthday, address, city, province, postalCode, email) \
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, gender, birthday, address, city, province, postal_code, email)
        cursor.execute(sql, values)
        db.commit()

        # Close database connection
        cursor.close()
        db.close()

        return redirect(url_for('medlist', name=first_name))
    else:
        return render_template("register.html")

@app.route('/medlist')
def medlist():
    name = request.args.get('name')
    return render_template("medlist.html", name=name)

@app.route('/medadd', methods=['GET', 'POST'])
def medadd(): 
    if request.method == 'POST':


    name = request.args.get('name')
    return render_template("medadd.html", name=name)

@app.route('/medinfo', methods=['GET', 'POST'])
def medinfo(): 
    name = request.args.get('name')
    return render_template("medinfo.html", name=name)


def main():
    app.run(host='127.0.0.1', debug=True, port=8000)

if __name__ == '__main__':
    main()