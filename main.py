import os
from flask import Flask, render_template, send_from_directory, request, redirect, make_response


app = Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')


@app.post('/submit')
def submit():
    name = request.form.get('name')
    context = {'name': name}
    response = make_response(render_template('request.html', **context))
    response.headers['new_cookie'] = 'request submitted'
    response.set_cookie('username', name)
    return response


@app.post('/exit')
def my_exit():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    return response


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
