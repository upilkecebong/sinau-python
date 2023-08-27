siswa = int(input("Jumlah siswa: "))
list_nilai = []
salah = 0

for i in range (siswa):
    nilai = input("Masukan nilaisiswa ke-" + str(i+1) + ": ")
    list_nilai.append(nilai)
    
for x in list_nilai:
    if x.isnumeric():
        print("valid")
    else:
        print("tidak valid")