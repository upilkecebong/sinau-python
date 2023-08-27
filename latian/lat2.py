nilai_list = []

for i in range(3):
    nilai = input("Masukkan nilai siswa no absen " + str(i + 1) + ": ")
    try:
        nilai = int(nilai)  # Mengubah input menjadi tipe data integer
        nilai_list.append(nilai)
    except ValueError:
        print("Input harus berupa angka. Coba lagi.")
        continue

if nilai_list:
    nilaimax = max(nilai_list)
    print("Nilai tertinggi adalah", nilaimax)
else:
    print("Tidak ada nilai yang dimasukkan.")
