from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Cargar datos del portfolio
def load_portfolio_data():
    with open('data/portfolio_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
@app.route('/es/')
def index():
    data = load_portfolio_data()
    return render_template('index.html', data=data)

@app.route('/projects')
def projects():
    data = load_portfolio_data()
    return render_template('projects.html', projects=data['projects'])

@app.route('/skills')
def skills():
    data = load_portfolio_data()
    return render_template('skills.html', skills=data['skills'])

@app.route('/about')
def about():
    data = load_portfolio_data()
    return render_template('about.html', about=data['about'])

@app.route('/experience')  # <-- ESTA ES LA NUEVA RUTA
def experience():
    data = load_portfolio_data()
    return render_template('experience.html', 
                         experience=data['experience'],
                         education=data['education'])

@app.route('/education')
def education():
    data = load_portfolio_data()
    return render_template('education.html', 
                         education=data['education'],
                         certifications=data.get('certifications_detail', []))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return jsonify({'status': 'success', 'message': 'Mensaje enviado correctamente'})
    
    return render_template('contact.html')

@app.route('/api/github-stats')
def github_stats():
    stats = {
        'repos': 25,
        'stars': 150,
        'followers': 50,
        'contributions': 1250
    }
    return jsonify(stats)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)