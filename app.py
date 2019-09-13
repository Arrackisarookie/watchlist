from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask.'


@app.route('/user/<name>')
def user_page(name):
    return "Welcome, %s" % name


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='haha'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test_page'
