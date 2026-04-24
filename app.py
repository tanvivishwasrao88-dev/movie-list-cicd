from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {"name": "Inception", "year": "2010", "emoji": "🌀"},
    {"name": "Avengers", "year": "2019", "emoji": "🦸"},
    {"name": "3 Idiots",  "year": "2009", "emoji": "🎓"},
    {"name": "RRR",       "year": "2022", "emoji": "🔥"},
    {"name": "KGF",       "year": "2022", "emoji": "💎"},
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
