# operator comparison itu ada > ,  < , => , <= , == , !=
# ada juga operator comparison "is"
a = 1
b = 1.0
print(a == b) #hasilnya true karena value dari a dan b sama
print(a is b) #hasilnya false karena objek a != b

# Operator "in" memeriksa untuk melihat apakah kedua string cocok sebagian
print('aaa' in 'aaa-bbb-ccc')   #hasilnya akan menjadi true karena ada aaa di dalam aaa-bbb-ccc
print('bbb' in 'aaa-bbb-ccc')   #hasilnya akan menjadi true karena ada bbb di dalam aaa-bbb-ccc
print('ddd' in 'aaa-bbb-ccc')   #hasilnya akan menjadi false karena tidak ada ddd dalam aaa-bbb-ccc
