"""
Pak Dani adalah seorang guru matematika di sebuah sekolah. Ia ingin mengembangkan program Python untuk menghitung statistik lebih kompleks dari nilai ujian siswanya. 
Bantu Pak Dani dengan merancang algoritma atau langkah-langkah yang diperlukan dalam program tersebut.

Langkah-langkah yang diperlukan:

1. Minta pengguna untuk memasukkan jumlah siswa yang mengikuti ujian.
2. Gunakan perulangan untuk meminta pengguna memasukkan nilai ujian masing-masing siswa sebanyak jumlah yang telah dimasukkan.
3. Simpan nilai-nilai ujian dalam sebuah struktur data (misalnya: list atau array).
4. Hitung rata-rata nilai ujian.
5. Temukan nilai tertinggi dan terendah dari nilai ujian.
6. Hitung berapa banyak siswa yang mendapatkan nilai A (80-100), B (70-79), C (60-69), dan D (50-59).
7. Cetak rata-rata, nilai tertinggi, nilai terendah, dan jumlah siswa yang mendapatkan masing-masing nilai A, B, C, dan D ke layar.

Tuliskan langkah-langkah atau algoritma di atas dalam urutan yang benar, sehingga Pak Dani dapat menggunakannya sebagai panduan untuk membuat 
program Python yang sesuai dengan kebutuhan tersebut.

"""

list_nilai = []
peserta_lulus = 0
peserta_gagal = 0
nilaiA = 0
nilaiB = 0
nilaiC = 0
nilaiD = 0

input_peserta = input("Masukan jumlah peserta ujian : ")
jml_peserta = int(input_peserta)

for i in range (jml_peserta):
    nilai = int(input("Masukkan nilai peserta ke" + str(i+1) + ": "))
    list_nilai.append(nilai)

    if nilai < 60:
        peserta_gagal +=1
    else:
        peserta_lulus +=1

for nilai in list_nilai:
    if 80<= nilai <=100:
        nilaiA +=1
    elif 70<= nilai <=79:
        nilaiB +=1
    elif 60<= nilai <=69:
        nilaiC +=1
    elif 50<= nilai <=59:
        nilaiD +=1

ratanilai = sum(list_nilai) // jml_peserta

maxnilai = max(list_nilai)
maxabsen = list_nilai.index(maxnilai)

minnilai = min(list_nilai)
minabsen = list_nilai.index(minnilai)

print("Rata-rata nilai : " + str(ratanilai))
print("Nilai tertinggi : " + str(maxnilai) + " (milik peserta ke-" + str(maxabsen+1) + ")" )
print("Nilai terrendah : " + str(minnilai) + " (milik peserta ke-" + str(minabsen+1) + ")" )
print("Peserta LULUS : " + str(peserta_lulus))
print("Peserta nilai A : " + str(nilaiA))
print("Peserta nilai B : " + str(nilaiB))
print("Peserta nilai C : " + str(nilaiC))
print("Peserta nilai D : " + str(nilaiD))
