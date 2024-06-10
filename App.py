from flask import Flask, request, jsonify

app = Flask(__name__)

# Skladište automobilske robe (u memoriji)
skladiste = []

@app.route('/')
def home():
    return "Dobrodošli u skladište automobilske robe!"

@app.route('/artikli', methods=['GET'])
def get_artikli():
    return jsonify(skladiste)

@app.route('/artikli', methods=['POST'])
def dodaj_artikl():
    novi_artikl = request.json
    skladiste.append(novi_artikl)
    return jsonify(novi_artikl), 201

@app.route('/artikli/<int:artikl_id>', methods=['GET'])
def get_artikl(artikl_id):
    for artikl in skladiste:
        if artikl['id'] == artikl_id:
            return jsonify(artikl)
    return jsonify({'poruka': 'Artikl nije pronađen'}), 404

@app.route('/artikli/<int:artikl_id>', methods=['PUT'])
def azuriraj_artikl(artikl_id):
    for artikl in skladiste:
        if artikl['id'] == artikl_id:
            artikl.update(request.json)
            return jsonify(artikl)
    return jsonify({'poruka': 'Artikl nije pronađen'}), 404

@app.route('/artikli/<int:artikl_id>', methods=['DELETE'])
def obrisi_artikl(artikl_id):
    for artikl in skladiste:
        if artikl['id'] == artikl_id:
            skladiste.remove(artikl)
            return jsonify({'poruka': 'Artikl obrisan'})
    return jsonify({'poruka': 'Artikl nije pronađen'}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)

