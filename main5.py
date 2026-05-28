# File main5.py (Versi aga pro penyimpanan otomatis)

import json
import os
from main import Barang, Inventaris

# Nama file text yang akan jadi database lokal kita
FILE_DATA = "inventaris.json"
kamar = Inventaris()

# !BARU! Logika membaca data (saat program baru dibuka)

if os.path.exists(FILE_DATA):
    with open(FILE_DATA, "r") as file:
        try:
            data_lama = json.load(file)
            for b in data_lama:
                # Mengubah data teks mentah dari file menjadi Objek PBO kembali
                objek_barang = Barang(b["nama"], b["kategori"], b["jumlah"],b["harga"])
                kamar.tambah_barang(objek_barang)
            print("\n[Sistem] Berhasil memuat data lama dari database!")
        except json.JSONDecodeError:
            print("\n[Sistem] File data kosong atau rusak, memulai Inventaris baru.")

while True:
    print("\n --- MENU UTAMA INVENTARIS ---")
    print("1. Tampilkan Semua Barang")
    print("2. Tambah Barang Baru")
    print("3. Simpan & Keluar")

    pilih = input("Pilih Menu (1/2/3): ")

    if pilih == "1":
        kamar.tampilkan_semua()

    elif pilih == "2":
        print("--- Input Barang Baru ---")
        nama = input("Masukan Nama Barang: ")
        kategori = input("Masukan Kategori: ")
        
        try:
            jumlah = int(input("Masukan jumlah/stok (angka): "))
            harga = int(input("Masukan Harga (angka): "))

            barang_baru = Barang(nama, kategori, jumlah, harga)
            kamar.tambah_barang(barang_baru)

        except ValueError:
            print("\n[!] Error: Jumlah dan Harga harus berupa angka Bulat!")

    elif pilih == "3":
        # BARU! Logika menyimpan data (saat memilih keluar)
        data_simpan = []

        # Mengambil list barang privat dari dalam objek Kamar
        # Menggunakan trik name Mangling Python (__ClassName__variable)

        for barang in kamar._Inventaris__daftar_barang:
            data_simpan.append({
                "nama": barang.get_nama(),
                "kategori": barang.get_kategori(),
                "jumlah": barang.get_jumlah(),
                "harga": barang.get_harga()
            })

            # Tulis data ke file inventaris.json
            with open(FILE_DATA, "w") as file:
                json.dump(data_simpan, file, indent=4)

            print("\n[Sukses] Semua data telat disimpan aman di 'inventaris.json'!")
            print("Terimakasih sudah menggunakan program ini")

    else:
        print("\n[!]Error: Pilihan tidak valid")


