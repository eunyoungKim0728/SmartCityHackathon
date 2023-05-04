from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register')
def register():
    return render_template("register.html")

def main():
    app.run(host='127.0.0.1', debug=True, port=8000)

if __name__ == '__main__':
    main()