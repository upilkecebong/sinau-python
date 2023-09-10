angka=input("Masukkan angka: ")

terbilang={
    "1":"satu",  
    "2":"dua",
    "3":"tiga",
    "4":"empat",
    "5":"lima",
    "6":"enam",
    "7":"tujuh",
    "8":"delapan",
    "9":"sembilan",
    "0":"",
}

def se():
    if len(angka) > 1 and angka[0] == "1" and angka[1] == "0" or angka[1] == "1":
        return "se"
    else:
        return terbilang[angka[0]]

def duadigit():
    if len(angka)==2 and angka[0]!="1":
        return str(se()+"puluh "+terbilang[angka[1]])
    elif len(angka)==2 and angka[0]=="1" and angka[1]!="1" and angka[1]!="0":
        return str(terbilang[angka[1]]+" belas ")
    elif len(angka)==2 and angka[0]=="1" and angka[1]=="1":
        return str(se()+"belas ")
    elif len(angka)==2 and angka[1]=="0":
        return str(se()+"puluh ")
    #len angka ne kudune di ilangi biar bisa di pangggil di bawah

if len(angka)==3 and angka[1]!="0" and angka[1]!="1" and angka[2]!="0":
    print(se()+" ratus "+ terbilang[angka[1]]+" puluh "+terbilang[angka[2]])
elif len(angka)==3 and angka[1]=="1" and angka[2]!="0":
    print(se()+" ratus "+ se() +" belas ")
elif len(angka)==3 and angka[1]=="0":
    print(se()+"ratus "+ terbilang[angka[1]] + terbilang[angka[2]])
elif len(angka)==3 and angka[1]=="0" and angka[2]=="0":
    print(se()+"ratus ")
elif len(angka)==2:
    print(duadigit())
else:
    print(terbilang[angka])

#harusnya bisa lebih singkat lagi kalau manggil function duadigit()
