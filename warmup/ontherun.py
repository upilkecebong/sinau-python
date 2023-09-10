s1=input("Nama awal = ")
s2=input("Nama akhir = ")
beda = 0
def baca(s1,s2):
    nilai=True
    isi = ''
    while nilai == True:
        for i in s1:
            for x in s2:
                if i == x:
                    isi += i
                else:
                    nilai = False
    # else:
        s1.replace(isi,'')
        s2.replace(isi,'')
        isi = ''
    return s1,s2

if len(s1) == len(s2):
  for i in s1 and x in s2:
      if i == x:
        beda += 1
elif len(s1) > len(s2):
  s1,s2=baca(s1,s2)
  beda = len(s1) + len(s2)
elif len(s1) < len(s2):
  s2,s1=baca(s2,s1)
  beda = len(s1) + len(s2)

print(beda)    

        