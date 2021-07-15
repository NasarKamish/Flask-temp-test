from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/<name>')
def homepage(name):
    return render_template('home.html', name=name)

@app.route('/loopy/<int:number>')
def loopy(number):
    return render_template('numbers_page.html', number=number)

@app.route('/students')
def form():
    dictionary = {'Godwin': 40, 'Mufasa': 200, 'Scar': 24, 'Nae': 20, 'Rafiki': 18, 'ed': 22, 'Pumba': 40}
    return render_template('Students.html', dictionary=dictionary)


if __name__ == "__main__":
    app.debug = True
    app.run()
