from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Python is running'

@app.route('/dessert')
def apple_pie():
    return 'Apple pie is fantastic'

@app.route('/dessert/<name>')
def dessert(name):
    return f'{name.capitalize()} is fantastic'

@app.route('/person/<string:first_name>') # By default this is a string
def person(first_name):
    return f'Welcom {first_name.capitalize()} to Today'

@app.route('/dessert/<int:x>/<int:y>')
def dessert_count(x, y):
    sum = x + y
    return str(sum)

if __name__=="__main__":
    app.run(debug=True)