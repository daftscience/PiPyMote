
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
from pymote import pyMote
from pprint import pprint


tv = pyMote()
app = Flask(__name__)


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display', methods=['POST'])
def display():

    command(request.form)
    # command(request.form['tvfunction'])
    return redirect(url_for('index'))


@app.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return "Quitting..."


def command(command):
    pprint(command)
    if command.has_key('tvfunction'):
        tvfunction(command['tvfunction'])
    elif command.has_key('pifunction'):
        pifunction(command['pifunction'])


def tvfunction(command):
    if command == "Tv On":
        tv.set_input(1)
    elif command == "Tv Off":
        tv.power_off()
    elif command == "input 1":
        tv.set_input(1)
    elif command == "input 2":
        tv.set_input(2)
    elif command == "input 3":
        tv.set_input(3)
    elif command == "input 4":
        tv.set_input(4)


def pifunction(command):
    if command == "restart":
        restart()


def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
