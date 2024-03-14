from flask import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

db = SQLAlchemy(app)

class Menu(db.Model):
    id_menu = Column(Integer, primary_key=True)
    nama = Column(String(100))
    harga = Column(Integer)
    kuantitas = Column(Integer)
    deskripsi = Column(String(255))

class Pemesanan(db.Model):
    id_pembeli = Column(Integer, primary_key=True)
    nama = Column(String(100))
    alamat = Column(String(255))
    telp = Column(String(20))
    pesan = Column(String(255))
    makanditempat = Column(Boolean)

    pembayaran = relationship("Pembayaran", backref="pemesanan")

class Pembayaran(db.Model):
    id_pembayaran = Column(Integer, primary_key=True)
    id_pembeli = Column(Integer, ForeignKey('pemesanan.id_pembeli'))
    opsi_bayar = Column(String(50))
    total_harga = Column(Integer)
