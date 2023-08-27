"""
latihan soal (soal ini di generate oleh chatgpt ditujukan untuk manusia yang lagi mau latian belajar make python)
Pak Budi adalah seorang dosen di sebuah perguruan tinggi. 
Dia ingin mengembangkan sebuah program Python yang dapat membantu menghitung statistik sederhana dari nilai ujian mahasiswanya. 
Bantu Pak Budi dengan merancang algoritma atau langkah-langkah yang diperlukan dalam program tersebut.

Langkah-langkah yang diperlukan:

1. Minta pengguna untuk memasukkan jumlah mahasiswa yang mengikuti ujian.
2. Gunakan perulangan untuk meminta pengguna memasukkan nilai ujian masing-masing mahasiswa sebanyak jumlah yang telah dimasukkan.
3. Simpan nilai-nilai ujian dalam sebuah struktur data (misalnya: list atau array).
4. Hitung rata-rata nilai ujian.
5. Temukan nilai tertinggi dan terendah dari nilai ujian.
6. Hitung berapa banyak mahasiswa yang lulus (nilai di atas atau sama dengan 60) dan berapa yang tidak lulus.
7. Cetak rata-rata, nilai tertinggi dan pemiliknya, nilai terendah dan pemiliknya, jumlah mahasiswa lulus, dan jumlah mahasiswa tidak lulus ke layar.

Tuliskan langkah-langkah atau algoritma di atas dalam urutan yang benar, sehingga Pak Budi dapat menggunakannya sebagai panduan 
untuk membuat program Python yang sesuai dengan kebutuhan tersebut.
"""
list_nilai = []
peserta_lulus = 0
peserta_gagal = 0

input_peserta = input("Masukan jumlah peserta ujian : ")
jml_peserta = int(input_peserta)

for i in range (jml_peserta):
    nilai = int(input("Masukkan nilai peserta ke" + str(i+1) + ": "))
    list_nilai.append(nilai)

    if nilai < 60:
        peserta_gagal +=1
    else:
        peserta_lulus +=1

total = sum(list_nilai)
ratanilai = total / jml_peserta

maxnilai = max(list_nilai)
maxabsen = list_nilai.index(maxnilai)

minnilai = min(list_nilai)
minabsen = list_nilai.index(minnilai)

print("Rata-rata nilai : " + str(ratanilai))
print("Nilai tertinggi : " + str(maxnilai) + " (milik peserta ke-" + str(maxabsen+1) + ")" )
print("Nilai terrendah : " + str(minnilai) + " (milik peserta ke-" + str(minabsen+1) + ")" )
print("Peserta LULUS : " + str(peserta_lulus))
print("Peserta TIDAK LULUS : " + str(peserta_gagal))