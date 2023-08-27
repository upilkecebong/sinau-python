list_nilai=[]
list_nilai_lulus=[]
list_nilai_tidak_lulus=[]

siswa = int(input("Masukkan jumlah siswa: "))
jmlh_lulus = 0
jmlh_tdk_lulus = 0

for a in range(siswa):
    nilai_input = input("masukan nilai siswa no absen " + str(a+1) + ": ") 
    nilai = int(nilai_input)
    list_nilai.append(nilai)

    if nilai >=60:
        jmlh_lulus += 1
    else:
        jmlh_tdk_lulus += 1

for x in list_nilai:
    if x >=60:
        list_nilai_lulus.append(x)
    else:
        list_nilai_tidak_lulus.append(x)


nilaitertinggi=max(list_nilai)
nilaiterendah=min(list_nilai)
nilairata=sum(list_nilai)/siswa

print("jumlah siswa adalah " + str(siswa))
print("nilai tertinggi adalah " + str(nilaitertinggi))
print("nilai terendah adalah " + str(nilaiterendah))
print("rata rata nilai siswa adalah " + str(nilairata))
print("jumlah siswa yang lulus adalah " + str(jmlh_lulus)+ " " + str(list_nilai_lulus) )
print("jumlah siswa yang tidak lulus adalah " + str(jmlh_tdk_lulus)+ " " + str(list_nilai_tidak_lulus) )