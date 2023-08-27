x = 1
ulang = True

while ulang == True:
    angka = int(input("Masukkan angka : ")) #apa yang di ulang
    if(angka>10):       #kondisi yang akan mengakhiri perulangan
        ulang = False
    else:
        x = angka