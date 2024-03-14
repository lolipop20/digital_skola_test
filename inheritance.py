class Mobil:
    def __init__(self,warna,merek,tahun):
        self.warna = warna
        self.merek = merek
        self.tahun = tahun

    def printname(self):
        print(self.warna)
        print(self.merek)
        print(self.tahun)

class suv(Mobil):
    def __init__ (self,warna,merek,tahun):
        Mobil.__init__(self,warna,merek,tahun)

class mvp(Mobil):
    def __init__(self, warna, merek, tahun):
        Mobil.__init__(self,warna, merek, tahun)

x = suv("Putih","Honda",2022)
y= mvp("Biru","Suzuki",2002)
x.printname()
y.printname()