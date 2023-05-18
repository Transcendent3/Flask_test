from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/spring')
def spring():
    return render_template('spring.html')


@app.route('/students/<x>/<y>')
def names(x, y):
    fio = ['Дмитрий', "Рустем", "Сергей", "Александр", "Анна", "Илья", "Евгений"]
    return render_template('names.html', fio=fio, title='Студенты', x=int(x), y=int(y))


app.run()