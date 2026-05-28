class Barang:
    def __init__(self, nama, kategori, jumlah, harga):
        # Menggunakan double underscore (__) di depan variabel 
        # membuat atribut ini bersifat PRIVATE (Encapsulation)
        self.__nama = nama
        self.__kategori = kategori
        self.__jumlah = jumlah
        self.__harga = harga

    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori
    
    def get_jumlah(self):
        return self.__jumlah
    
    def get_harga(self):
        return self.__harga
    
    # Setter (Fungsi untuk mengubah data private dengan aman)
    def set_nama(self, nama):
        self.__nama = nama

    def set_kategori(self, kategori):
        self.__kategori = kategori

    def set_jumlah(self, jumlah):
        self.__jumlah = jumlah

    def set_harga(self, harga):
        self.__harga = harga

    # SETTER( Fungsi untuk mengubah data private dengna aman)
    def set_jumlah(self, jumlah_baru):
        if jumlah_baru >= 0: #validasi agar jumlah tidak minu
            self.__jumlah = jumlah_baru
        else:
            print("Error: Jumlah barang tidak boleh minus!")

    def set_harga(self, harga_baru):
        if harga_baru >= 0:
            self.__harga = harga_baru
        else:
            print("Error: Harga barang tidak boleh minus!")

# CLASS INVENTARIS (Menampung kumpulan barang)
class Inventaris:
    def __init__(self):
        #List kosong untuk menampung objek2 dari class barang
        self.__daftar_barang = []

    #Fungsi untuk menambah objek barang ke dalam list
    def tambah_barang(self, barang_baru):
        self.__daftar_barang.append(barang_baru)
        print(f"Sukses: {barang_baru.get_nama()} berhasil ditambahkan!")

    #Fungsi untuk menampilkan semua barang yang ada dalam list
    def tampilkan_semua(self):
        if not self.__daftar_barang:
            print("\n Inventaris Kosong")
            return
        
        print("Daftar Inventaris Barang")
        for barang in self.__daftar_barang:
            print(f"Nama: {barang.get_nama()} | Kategori: {barang.get_kategori()} | Stok: {barang.get_jumlah()} | harga: Rp. {barang.get_harga()}")