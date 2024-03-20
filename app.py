from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from website.db import Menu, Pemesanan, Pembayaran
# import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11111@localhost/palupi'
app.config['SECRET_KEY'] = 'secret_key'  # Mengatur kunci rahasia untuk session Flask
db = SQLAlchemy(app)

Base = declarative_base()

antrian_restoran = []

class Menu(db.Model):
    id_menu = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer)
    kuantitas = db.Column(db.Integer)
    deskripsi = db.Column(db.String)

class Pemesanan(db.Model):
    id_pembeli = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    alamat = db.Column(db.String(50))
    telp = db.Column(db.String(15))
    pesan = db.Column(db.String(50))
    makanditempat = db.Column(db.Boolean())

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))

class Pembayaran(db.Model):
    id_pembayaran = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pemesanan.id_pembeli'))
    opsi_bayar = db.Column(db.String(20))
    total_harga = db.Column(db.Integer)

engine = create_engine('postgresql://postgres:11111@localhost/palupi')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route("/")
def home():
    return render_template('dashboard.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_pengguna():
    id_user = request.form['username']
    password = request.form['password']

    # Cek apakah pengguna ada dalam database
    user = User.query.filter_by(id_user=id_user, password=password).first()
    if user:
        return f"Selamat datang, {id_user}!"
    else:
        return "Login gagal. Cek kembali username dan password Anda."
    
@app.route("/daftar")
def daftar():
    return render_template('daftar.html')

@app.route('/daftar', methods=['POST'])
def daftar_akun():
    id_user = request.form['id_user']
    password = request.form['password']

    # Tambahkan pengguna baru ke dalam database
    try:
        new_user = User(id_user=id_user, password=password)
        db.session.add(new_user)
        db.session.commit()
        return f"Akun {id_user} berhasil didaftarkan."
    except IntegrityError:
        db.session.rollback()
        return "Username sudah digunakan. Silakan pilih username lain."
    
# Endpoint untuk mendapatkan seluruh menu
@app.route('/menu', methods=['GET'])
def menu():
    session = Session()
    menus = session.query(Menu).all()
    session.close()
    output = []
    for menu in menus:
        menu_data = {}
        menu_data['id_menu'] = menu.id_menu
        menu_data['nama'] = menu.nama
        menu_data['harga'] = menu.harga
        menu_data['kuantitas'] = menu.kuantitas
        output.append(menu_data)
    return jsonify({'menu': output})


# Endpoint untuk mendapatkan semua data antrian
@app.route('/pesan', methods=['GET'])
def pesan():
    return jsonify({'pesan': antrian_restoran})

# Endpoint untuk menambahkan nomor meja ke dalam antrian
@app.route('/pesan', methods=['POST'])
def add_to_antrian():
    data = request.get_json()
    nomor_meja = data.get('nomor_meja')

    if not nomor_meja:
        return jsonify({'error': 'Nomor meja harus disertakan'}), 400

    antrian_restoran.append({'nomor_meja': nomor_meja, 'status': 'menunggu'})
    return jsonify({'message': f'Nomor meja {nomor_meja} telah ditambahkan ke dalam antrian'})

# Endpoint untuk memperbarui status antrian (misalnya: dipanggil, selesai)
@app.route('/pesan/<int:nomor_meja>', methods=['PUT'])
def update_antrian_status(nomor_meja):
    status = request.args.get('status')
    for antrian in antrian_restoran:
        if antrian['nomor_meja'] == nomor_meja:
            antrian['status'] = status
            return jsonify({'message': f'Status antrian untuk nomor meja {nomor_meja} diperbarui menjadi {status}'})

    return jsonify({'error': f'Nomor meja {nomor_meja} tidak ditemukan'}), 404


# Endpoint untuk melakukan pembayaran
@app.route('/pembayaran', methods=['POST'])
def pembayaran():
    data = request.get_json()
    pemesanan_id = data['pemesanan_id']
    total_harga = data['total_harga']

    pembayaran = Pembayaran(pemesanan_id=pemesanan_id, total_harga=total_harga)
    db.session.add(pembayaran)
    db.session.commit()

    return jsonify({'message': 'Pembayaran berhasil'}), 201

if __name__ == '__main__':
    app.run(debug=True)
