from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    form_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
    }
    valid = User.user_validation(form_data)
    if valid:
        results = User.create_user(form_data)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:user_id>')
def get_one(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('info.html', user = user)

