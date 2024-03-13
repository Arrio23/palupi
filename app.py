from flask import Flask, jsonify, render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from website.db import Menu, pembayaran, pemesanan  # Memperbaiki impor
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11111@localhost/palupi'
app.config['SECRET_KEY'] = 'secret_key'  # Mengatur kunci rahasia untuk session Flask
db = SQLAlchemy(app)
Session(app)

@app.route("/")
def home():
    return render_template('dashboard.html')

@app.route("/login")
def login():
    return render_template('login.html')

# Endpoint untuk mendapatkan seluruh menu
@app.route('/menu', methods=['GET'])
def get_menu():
    menu = Menu.query.all()
    result = []
    for item in menu:
        menu_data = {
            'id': item.id_menu,
            'nama': item.nama,
            'harga': item.harga
        }
        result.append(menu_data)
    return jsonify(result)

# Endpoint untuk memesan menu
@app.route('/pesan', methods=['POST'])
def pesan_menu():
    data = request.get_json()
    user_id = data['user_id']
    menu_id = data['menu_id']
    jumlah = data['jumlah']

    pemesanan = pemesanan(user_id=user_id, menu_id=menu_id, jumlah=jumlah)
    db.session.add(pemesanan)
    db.session.commit()

    return jsonify({'message': 'Pemesanan berhasil'}), 201

# Endpoint untuk melakukan pembayaran
@app.route('/pembayaran', methods=['POST'])
def bayar_pesanan():
    data = request.get_json()
    pemesanan_id = data['pemesanan_id']
    total_harga = data['total_harga']

    pembayaran = pembayaran(pemesanan_id=pemesanan_id, total_harga=total_harga)
    db.session.add(pembayaran)
    db.session.commit()

    return jsonify({'message': 'Pembayaran berhasil'}), 201

if __name__ == '__main__':
    app.run(debug=True)
