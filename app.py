from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global name
    if request.method == 'POST':
            name = request.form['NAME']
            return render_template('hello.html', name = name)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()
