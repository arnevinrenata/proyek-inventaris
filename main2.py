#tempat untuk menjalankan program

# 1. Ambil class dari file main.py
 main  Barang, Inventaris

# 2. Menjalankkan program dan inventaris menjadi induk
kamar = Inventaris()

barang1 = Barang("Laptop", "Elektronik", 1, 8000000)
barang2 = Barang("Komputer", "Elektronik", 1, 15000000)
barang3= Barang("Ipad", "Elektronik", 1, 5000000)

# 3. Memasukan barang ke sistem inventaris induk
kamar.tambah_barang(barang1)
kamar.tambah_barang(barang2)
kamar.tambah_barang(barang3)

#Menampilkan hasil
kamar.tampilkan_semua()