""" 
Latihan :
Buat program yang dapat menampilkan 4 menu : 
1. Menu Lihat data siswa dengan memasukan angka 1
2. Menu Lihat mata pelajaran dengan memasukan angka 2
3. Menu Lihat Guru Mapel dengan memasukan angka 3
4. Menu keluar dari program dengan memasukan huruf q
"""
murid = ['Aurel', 'Chandrika', 'Ivory', 'Ayu']
mapel = ['pkk','paas','mpp', 'iaas']
gurumapel = ['Pak Eka', 'Pak Ugik', 'Bu Ratna','Bu Endah']

menu = True

while menu==True:
    nomermenu = input("Masukkan menu : ")
    if(nomermenu=="1"):
        print(murid)
    elif(nomermenu=="2"):
        print(mapel)
    elif(nomermenu=="3"):
        print(gurumapel)
    elif(nomermenu=="q"):
        menu = False
    else:
        print("input tidak valid")