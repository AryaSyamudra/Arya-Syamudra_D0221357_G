print('hello world') #print

#tipe data
boolean = 5 == 5 #tipe data boolean
print(boolean)
string = 'arya syamudra'#tipe data string
print(string)
integer = 5 #tipe data integer
print(integer)
desimal = 2.5 #tipe data Float
print(desimal)
print(type(string))
buah = ['mangga', 'anggur', 'langsat'] #tipe data list
print(type(buah))
negara = ('indonesia', 'malaysia', 'singapura') #tipe data tuple
print(type(negara))
makanan = {'nasi', 'ikan', 'daging'} #tipe data set
print(type(makanan))

#operasi aritmatika
a = 5
b = 2
jumlah = a+b #penjumlahan
print(jumlah)
kurang = a-b #pengurangan
print(kurang)
kali = a*b #perkalian
print(kali)
bagi = a/b #pembagian
print(bagi)
modus = a%b #sisa hasil bagi
print(modus)
pangkat = a**b #perpangkatan
print(pangkat)
bulat = a//b #pembagian bulat
print(bulat)

#operator penugasan
n = 2
n += 3
print(n)

print(2<4) #operator perbandingan

#Operator logika
c = 5 == 5 and 6 != 7 #and
print(c)
d = 10 == 5 or 10 != 5 #or
print(d)
e = not 5==5 #not
print(e)

#operator bitwise
f = 10010001
g = 10010010
print(f & g) #AND

#percabangan
umur = 20
if umur > 18:
    print('anda adalah orang dewasa')
elif umur > 12:
    print('anda adalah remaja')
else:
    print('anda adalah anak anak')
