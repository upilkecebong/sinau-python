list=[]

for i in range (5):
    nilai = int(input("Masukkan nilai peserta ke" + str(i+1) + ": "))
    list.append(nilai)

for x,y in enumerate(list):
    y*=2
    list[x]=y

print(list)