from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/palupi'

db = SQLAlchemy(app)
print("Connected to the database successfully!")

class Menu(db.Model):
    id_menu = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    harga = db.Column(db.Integer)
    kuantitas = db.Column(db.Integer)
    deskripsi = db.Column(db.String(255))

# Definisi model untuk tabel Pemesanan
class Pemesanan(db.Model):
    id_pembeli = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    alamat = db.Column(db.String(255))
    telp = db.Column(db.String(20))
    pesan = db.Column(db.String(255))
    makanditempat = db.Column(db.Boolean)

# Definisi model untuk tabel Pembayaran
class Pembayaran(db.Model):
    id_pembayaran = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pemesanan.id_pembeli'))
    opsi_bayar = db.Column(db.String(50))
    total_harga = db.Column(db.Integer)

# Sinkronisasi basis data dengan model
with app.app_context():
    db.create_all()
    print("Database telah berhasil dibuat.")

