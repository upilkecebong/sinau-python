jmlbatu=int(input("Jumlah batu = "))
batu=input().split(" ")

for i in batu:
    batu[batu.index(i)]=batu.index(i)+batu.index(i+1)

print(batu)