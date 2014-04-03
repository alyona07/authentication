__author__ = 'lolo'
import sys
from flask import Flask, request, render_template

app = Flask(__name__)


def get_data():
    result = {}
    for name in ('login', 'password'):
        if request.method == 'POST':
            value = str(request.form[name])
        else:
            value = str(request.args.get(name))
        result[name] = value
        print(result)
    return result

def file_write(result):
    with open('login_in.txt', 'w') as f:
        for item in result:
            f.write(result[item])
            f.write('\t')

def file_open_in(file_txt):
    with open(file_txt, 'r') as f:
        login_in = list(f.readline().split())
    return login_in

def file_open_out(file_txt):
    login_out = []
    with open(file_txt, 'r') as f:
        for line in range(0, 3, 1):
            login_out.append(f.readline().split())
    return login_out

@app.route('/', methods = ['GET', 'POST'])
def index():
    login_in = get_data()
    file_write(login_in)
    if file_open_in('login_in.txt') in file_open_out('login_out.txt'):
        hello = 'Welcome!'
        return render_template('res.html', hello = hello)
    else:
        if file_open_in('login_in.txt') == ['None', 'None']:
            hello = 'Enter Login and Password'
        else:
            hello = 'Error enter Login or Password'
        return render_template('index.html', hello = hello)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
