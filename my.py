from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/<name>')
def hello_world(name):
    # return 'Hello World!'
    return render_template('hello.html', name=name, user='ooooop!')
if __name__ == '__main__':
    app.run('0.0.0.0')