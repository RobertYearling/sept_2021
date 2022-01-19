from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.artist import Artist


@app.route('/')
def index():
    artists = Artist.get_all()
    return render_template('index.html', artists = artists )

@app.route('/new_artist')
def new_artist():
    return render_template('new_artist.html')

@app.route('/process', methods=['POST'])
def create_artist():
    Artist.create(request.form)
    return redirect('/')

# Edit Artist Renders our artist update page
@app.route('/edit/<int:artist_id>')
def edit_artist(artist_id):
    data = {
        'id' : artist_id
    }
    artist = Artist.get_one(data)
    return render_template('edit_artist.html', artist = artist)

# Update Artist
@app.route('/update/<int:artist_id>', methods=['POST'])
def update(artist_id):
    data = {
        'id' : artist_id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    Artist.update(data)
    return redirect('/')

# Deleting an Artist from the Database
@app.route('/delete/<int:artist_id>/artist')
def destroy(artist_id):
    data = {
        'id' : artist_id
    }
    Artist.destroy(data)
    return redirect('/')