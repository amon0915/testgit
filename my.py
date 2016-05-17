from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.update(
    SERVER_NAME='127.0.0.1:8080'
)
@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('hello.html', name='name', user='ooooop!')
if __name__ == '__main__':
    app.run('0.0.0.0')