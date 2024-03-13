DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS pemesanan;
DROP TABLE IF EXISTS pembayaran;

CREATE TABLE menu (
  id_menu INTEGER PRIMARY KEY AUTOINCREMENT,
  nama TEXT NOT NULL,
  harga TEXT NOT NULL,
  kuantitas TEXT,
  deskripsi TEXT
);

CREATE TABLE pemesanan (
  id_pembeli INTEGER PRIMARY KEY AUTOINCREMENT,
  nama TEXT,
  alamat TEXT NOT NULL,
  telp TEXT NOT NULL,
  pesan TEXT NOT NULL,
  makanditempat BOOLEAN
);

CREATE TABLE pembayaran (
  id_pembayaran INTEGER PRIMARY KEY AUTOINCREMENT,
  id_pembeli FOREIGN REFERENCES FROM pemesanan,
  opsi_bayar TEXT,
  total_harga INTEGER
);