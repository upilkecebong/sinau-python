import time
start_time=time.time()

# Buat program yang dapat menerima input nilai mapel dari sejumlah x siswa.
# contoh :
# input : 3 #jumlah siswa yg akan diinput
# input : 2 #jumlah mapel yang akan diinput

# input : nilai mapel 1 untuk siswa ke 1 :
# 	nilai mapel 2 untuk siswa ke 1 :
# 	nilai mapel 1 untuk siswa ke 2 :
# 	nilai mapel x untuk siswa ke y :
# 	.
# 	.
# 	input nilai ke 2 untuk siswa ke 3 :

# output : 
# Rata-rata nilai siswa ke 1 :
# Rata-rata nilai siswa ke 2 :
# Rata-rata nilai siswa ke 3 :
from statistics import mean 

nilai_siswa =[]
nilai_siswa_ke = []
total_nilai_siswa_ke=0
total_nilai_siswa=[]
list_rata=[]

jml_siswa =int(input("Masukkan jumlah siswa :"))
jml_mapel =int(input("Masukkan jumlah mapel :"))

for a in range(jml_siswa):
    for b in range (jml_mapel):
        nilai_input = int(input("nilai mapel " + str(a+1) + " untuk siswa ke " + str(b+1) + " :"))
        nilai_siswa_ke.append(nilai_input)

    nilai_siswa.append(nilai_siswa_ke)
    rata = mean(nilai_siswa_ke)
    list_rata.append(rata)
    #variabel sementara buat mengkosongkan variabel nilai_siswa_ke
    nilai_siswa_ke = []


for i in list_rata:
    absen = list_rata.index(i)
    print ("Nilai rata rata siswa ke " + str(absen+1) + " :"  + str(i))




print(time.time() - start_time,"detik")
