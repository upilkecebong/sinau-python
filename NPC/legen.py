gulungan = {}
n_gulungan = int(input("Jumlah gulungan = "))
max = 0
judul_gulungan = ""
ukuran= 0

for x in range(n_gulungan):
    isi=input().split(" ")
    gulungan[isi[0]] = [eval(i) for i in isi[2:(int(isi[1])+2)]]
    ukuran=sum(gulungan[isi[0]])

    if(ukuran > max):
        max = ukuran
        judul_gulungan = isi[0]

print(judul_gulungan)