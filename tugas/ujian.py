"""
Pak eka ingin membuat program yang dapat mengecek daftar nilai sejumlah  siswa yg dimasukan valid atau tidak
contoh :
input :
jumlah n siswa
    nilai siswa ke-1
    nilai siswa ke-2
    ..
    nilai siswa ke-n

output:
valid/tidak valid
"""
siswa = int(input("Jumlah siswa: "))
list_nilai = []
salah = 0
 
for i in range (siswa):
    nilai = input("Masukan nilaisiswa ke-" + str(i+1) + ": ")
    list_nilai.append(nilai)  

for x in list_nilai:
    if x.isnumeric() == False:
        salah +=1

if salah > 0:
    print("tidak valid")
else:
    print("valid")