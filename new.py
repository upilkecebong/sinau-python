buahpmebeli=input("Masukkan nama buah = ")
jumlah=int(input("Masukkan jumlah buah = "))

buah = [
    ['aple',300],
    ['pisang',400],
    ['jambu',900]
]

total=buah[0][1]*((buah[0][0]==buahpmebeli)*jumlah) + buah[1][1]*((buah[1][0]==buahpmebeli)*jumlah)+buah[2][1]*((buah[2][0]==buahpmebeli)*jumlah)

print("Harga buah adalah "+str(total))

