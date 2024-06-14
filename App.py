from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from pony.orm import Database, PrimaryKey, Required, db_session, select

app = Flask(__name__)
CORS(app)  

db = Database()
db.bind(provider='sqlite', filename='skladiste.sqlite', create_db=True)

class Artikli(db.Entity):
    id = PrimaryKey(int, auto=True)
    kolicina = Required(int)
    cijena = Required(float)
    dio = Required(str)

class Marka(db.Entity):
    id = PrimaryKey(int, auto=True)
    ime = Required(str)
    model = Required(str)
    godina_proizvodnje = Required(int)

db.generate_mapping(create_tables=True)

@app.route('/')
@db_session
def home():
    return "Dobrodošli u skladište automobilske robe!"

@app.route('/artikli', methods=['GET'])
@db_session
def get_artikli():
    artikli = select(a for a in Artikli)
    return render_template('index.html', artikli=artikli)

@app.route('/artikli', methods=['POST'])
@db_session
def dodaj_artikl():
    kolicina = request.form['kolicina']
    cijena = float(request.form['cijena'])
    dio = request.form['dio']
    artikl = Artikli(kolicina=kolicina, cijena=cijena, dio=dio)
    return redirect(url_for('home'))

@app.route('/artikli/<int:artikl_id>', methods=['PUT'])
@db_session
def azuriraj_artikl(artikl_id):
    artikl = Artikli[artikl_id]
    kolicina = request.form.get('kolicina')
    cijena = request.form.get('cijena')
    dio = request.form.get('dio')
    if kolicina:
        artikl.kolicina = int(kolicina)
    if cijena:
        artikl.cijena = float(cijena)
    if dio:
        artikl.dio = dio
    return redirect(url_for('home'))

@app.route('/artikli/<int:artikl_id>', methods=['DELETE'])
@db_session
def obrisi_artikl(artikl_id):
    artikl = Artikli[artikl_id]
    artikl.delete()
    return redirect(url_for('home'))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)


