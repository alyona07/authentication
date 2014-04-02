from flask import Flask, request, render_template

app = Flask(__name__)

def get_data():
    if request.method == 'POST':
        login = str(request.form['login'])
        password = str(request.form['password'])
    else:
        login = str(request.args.get('login'))
        password = str(request.args.get('password'))
    login_in = [login, password]
    return login_in

def file_write(login_in):
    with open('login_in.txt', 'w') as f:
        for item in login_in:
            f.write(item)
            f.write('\t')
    f.close()

def file_open_in(file_txt):
    f = open(file_txt, 'r')
    login_in = list(f.readline().split())
    f.close()
    return login_in

def file_open_out(file_txt):
    login_out = []
    f = open(file_txt, 'r')
    for line in range(0, 3, 1):
        login_out.append(f.readline().split())
    f.close()
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
