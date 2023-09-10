ax=[]
baris = int(input("Masukkan jumlah baris: "))
a = 0

for i in range(baris):
    sequence = int(input())
    for i in range(sequence):
        angka=input().split(" ")
        ax.append(angka)

print(ax)
print(sequence)

