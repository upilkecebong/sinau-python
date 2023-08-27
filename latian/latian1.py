"""
Pak Eka ingin mengetahui nilai tertinggi dari siswa di kelasnya menggunakan program python sederhana. 
Buatkan koding menggunakan python yang dapat menampung n jumlah siswa dan nilai dari masing-masing siswa tersebut.
"""

list_nilai=[]

for i in range (3):
    nilai=int(input("Masukkan nilai siswa no absen " + str(i+1) + ": "))#masukin input
    list_nilai.append(nilai) #masukkan nilai ke list

nilaimax=max(list_nilai) #masukan nilai tertinggi dalam variabel nilaimax
absen=list_nilai.index(nilaimax) #lihat nilai maksimal pada list ada di index ke berapa

for y,x in enumerate(list_nilai):
    print(str(x) + " milik no absen " + str(y+1))

print("Nilia tertinggi adalah " + str(nilaimax) + " milik no absen " + str(absen+1)) #absen + 1 karena index list dimulai dari 0


