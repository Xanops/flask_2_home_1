from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('page.html', title=title)


@app.route('/distribution')
def loop():
    sp = ['Ридли Скотт', "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('loop.html', sp=sp)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
