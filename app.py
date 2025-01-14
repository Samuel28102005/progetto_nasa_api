from flask import Flask, render_template, redirect, url_for
import requests
app = Flask(__name__)
NASA_API_KEY = 'ub1Sn5e16DLaduvUDQEAfrvaBhnhZp3HMANhcuOR' #api kei della nasa
#ourte /nasa per immagine NASA
@app.route('/nasa')
def nasa_home():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json() #converte da json a dict python
    return render_template('nasa.html', title=data.get("title"),
description=data.get("explanation"), image_url=data.get("url"))

#route /cat per fatto sui gatti
@app.route('/cat')
def cat_home():
    response = requests.get('https://catfact.ninja/fact') #richiedo i dati
    data = response.json() #converte da json a dict python
    return render_template('cat_fact.html', fact=data.get("fact"))

@app.route('/cat/change', methods=['POST'])
def cat_change_fact():
    return redirect(url_for('cat_home'))
if __name__ == '__main__':
    app.run(debug=True)