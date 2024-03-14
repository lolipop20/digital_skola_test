class Mainan:
    def __init__(self,nama,warna):
        self.nama = nama
        self.warna = warna

    def info(self):
        return f"{self.nama} berwarna {self.warna}"
    
mainan_saya = Mainan("Balon","Biru")
print(mainan_saya.info())

# -----------------------------------------

# class with attributes class
class Mainan:
    #attribute class
    jumlah_mainan = 0

    def __init__(self,nama,warna):
        #attribute object
        self.nama = nama
        self.warna = warna
        # menambahkan 1 ke attribute class setiap object dibuat
        Mainan.jumlah_mainan += 1

# membbuat beberapa object dari class Mainan
mainan1 = Mainan("Balon","Jingga")
mainan2 = Mainan("Boneka","tosca")

# akses attribute class
print(f"jumlah mainan: {Mainan.jumlah_mainan}")

# ------------------------------------------------------

# class methods
# class with attributes class
class Mainan:
    #attribute class
    jumlah_mainan = 0

    def __init__(self,nama,warna):
        #attribute object
        self.nama = nama
        self.warna = warna
        # menambahkan 1 ke attribute class setiap object dibuat
        Mainan.jumlah_mainan += 1
    
    # class methods untuk mendapatkan jumlah mainan
    @classmethod
    def get_jumlah_mainan(cls):
        return cls.jumlah_mainan

# membbuat beberapa object dari class Mainan
mainan1 = Mainan("Balon","Jingga")
mainan2 = Mainan("Boneka","tosca")

# akses attribute class
print(f"jumlah mainan: {Mainan.get_jumlah_mainan()}")

# -------------------------------------------------------

class Mainan:
    #attribute class
    jumlah_mainan = 0

    def __init__(self,nama,warna,tahun_produksi):
        #attribute object
        self.nama = nama
        self.warna = warna
        self.tahun_produksi = tahun_produksi
        # menambahkan 1 ke attribute class setiap object dibuat
        Mainan.jumlah_mainan += 1
    
    # class methods untuk mendapatkan jumlah mainan
    @classmethod
    def get_jumlah_mainan(cls):
        return cls.jumlah_mainan

# metode object untuk mendapatkan informasi tentang mainan
    def info(self):
        return(f"{self.nama} ({self.tahun_produksi}), berwarna {self.warna}")

# instace methods untuk menentukan apakah mainan baru atau usang
    def cek_usia(self):
        if 2022 - self.tahun_produksi > 5 :
            return "mainan usang"
        else :
            return "mainan baru"
        
# membbuat beberapa object dari class Mainan
mainan1 = Mainan("Balon","Jingga",2010)
mainan2 = Mainan("Boneka","tosca",2022)

# menggunakan akses attribute class
print(f"jumlah mainan: {Mainan.get_jumlah_mainan()}")

#menggunakan metode object untuk mendapatka informasi
print(mainan1.info())
print(mainan2.info())

# menggunakan instance method untuk menentukan usia mainan
print(mainan1.cek_usia())
print(mainan2.cek_usia())