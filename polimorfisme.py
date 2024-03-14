# Overload

class Kalkulator:
    def jumlah(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0

# buat object dari class kalkulator
kalkulator = Kalkulator()

# menggunakan metode dengan jumlah argument yang beda
hasil1 = kalkulator.jumlah(1)
hasil2 = kalkulator.jumlah(2,1)
hasil3 = kalkulator.jumlah(3,2,1)

print(hasil1)
print(hasil2)
print(hasil3)

#-------------------

# Override

class Hewan:
    def __init__(self,nama,jenis):
        self.nama = nama
        self.jenis = jenis

    def info(self):
        return f"{self.jenis} bernama {self.nama}"
    
class Kucing(Hewan):
    def __init__(self, nama, warna):
        # memanggil konstruktor dari kelas dasar/induk
        super().__init__(nama, "Kucing")
        self.warna = warna

    def info(self):
        return f"{self.jenis} bernama {self.nama}, berwarna {self.warna}"

# membuat object dari kelas kucing
kucing1 = Kucing("catty","biru")

# menggunakan method dari kelas turunan setelah melakukan override
print(kucing1.info())