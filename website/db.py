import psycopg2 as pg
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11111@localhost/palupi'
db = SQLAlchemy(app)

try:
    connection = pg.connect(
        dbname="palupi",
        user="postgres",
        password="11111",
        host="localhost"
    )

    cursor = connection.cursor()
    print("succes")

except Exception as e:
    print(f"An error occurred: {e}")

class Menu(db.Model):
    id_menu = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer)
    kuantitas = db.Column(db.Integer)
    deskripsi = db.Column(db.String)
    # Add other relevant fields

class pemesanan(db.Model):
    id_pembeli = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    alamat = db.Column(db.String(50))
    telp = db.Column(db.String(15))
    pesan = db.Column(db.String(50))
    makanditempat = db.Column(db.Boolean())

class user(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))

class pembayaran(db.Model):
    id_pembayaran = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pemesanan.id_pembeli'))
    opsi_bayar = db.Column(db.String(20))
    total_harga = db.Column(db.Integer)

with app.app_context():
    db.create_all()
    print("sukses")