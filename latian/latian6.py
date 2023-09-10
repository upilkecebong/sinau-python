# import math

# angka=input("Masukkan angka: ")
# angkaanu = []
# output=0

# for i in angka :
#     angkaanu.append(int(i))

# for a in angkaanu:
#     output += math.pow(a,3)

# if output == int(angka):
#     print("armstrong")  
# else:   
#     print("bukan angka armstrong")


import math

angka = input("Masukkan angka: ")
angkaanu = [int(i) for i in angka]
output = sum(math.pow(a, 3) for a in angkaanu)

result = "armstrong" * (output == int(angka)) + "bukan angka armstrong" * (output != int(angka))
print(result)
