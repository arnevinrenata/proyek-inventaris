# 1. Ambil class dari main.py
from main import Barang, Inventaris

# 2. Wadah induk menampung barang
kamar = Inventaris()

# 3 Membuat perulangan agar menu terus muncul
while True:
    print("\n--- MENU UTAMA INVENTARIS ---")
    print("1. Tampilkan Semua Barang")
    print("2. Tambah Barang Baru")
    print("3. Keluar")

    pilih = input("Pilih Menu (1/2/3): ")

    if pilih == "1":
        kamar.tampilkan_semua()

    elif pilih == "2":
        print("--- Input Barang Baru ---")
        nama = input("Masukan Nama Barang: ")
        kategori = input("Masukan Kategori: ")
        
        # Menerapkan Exception Handling (Materi UTS PBO)
        # Agar program tidak crash/mati jadi pake try kalo orang ngeinputnya salah pun program tetep jalan
        try:
            jumlah = int(input("Masukan jumlah/stok (angka): "))
            harga = int(input("Masukan Harga (angka): "))

            barang_baru = Barang(nama, kategori, jumlah, harga)
            kamar.tambah_barang(barang_baru)

        except ValueError:
            print("\n[!] Error: Jumlah dan Harga harus berupa angka Bulat!")

    elif pilih == "3":
        print("Terimakasih sudah menggunakan program ini")
        break
         
    else: 
        print("\nError: Pilihan tidak valid, silakan pilih 1, 2, atau 3")                                      



          