from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'movieapp123'

users = {
    "admin": "1234",
    "bro": "1234"
}

movies = [
    {"id": 1, "name": "Inception",   "year": "2010", "emoji": "🌀", "rating": 0},
    {"id": 2, "name": "Avengers",    "year": "2019", "emoji": "🦸", "rating": 0},
    {"id": 3, "name": "3 Idiots",    "year": "2009", "emoji": "🎓", "rating": 0},
    {"id": 4, "name": "RRR",         "year": "2022", "emoji": "🔥", "rating": 0},
    {"id": 5, "name": "KGF",         "year": "2022", "emoji": "💎", "rating": 0},
    {"id": 6, "name": "Interstellar","year": "2014", "emoji": "🚀", "rating": 0},
]

@app.route('/')
def home():
    if 'user' not in session:
        return redirect('/login')
    search = request.args.get('search', '').lower()
    filtered = [m for m in movies if search in m['name'].lower()]
    return render_template('index.html', movies=filtered,
                           user=session['user'], search=search)

@app.route('/login', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if u in users and users[u] == p:
            session['user'] = u
            return redirect('/')
        error = '❌ Wrong username or password!'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/rate/<int:movie_id>/<int:stars>')
def rate(movie_id, stars):
    if 'user' not in session:
        return redirect('/login')
    for m in movies:
        if m['id'] == movie_id:
            m['rating'] = stars
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
