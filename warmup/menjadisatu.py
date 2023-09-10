angka = input("Masukkan angka: ")
jumlah = angka

while len(jumlah) > 1:
    angkastor = 0
    for i in jumlah:
        angkastor += int(i)
    jumlah = str(angkastor)

print(jumlah)