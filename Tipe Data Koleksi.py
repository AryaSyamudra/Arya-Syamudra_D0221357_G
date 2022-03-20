#Tipe Data List
buah = ['mangga', 'rambutan', 'durian']
print(buah)
for nama_buah in buah:
    print(nama_buah)
del buah[1]
print(buah)
buah.insert(1, 'langsat')
print(buah)

#Tipe Data Tuple
hewan = ('ayam', 'sapi', 'kambing')
print(hewan)
for nama_hewan in hewan:
    print(nama_hewan)

#Tipe Data Set
warna = {'merah', 'hijau', 'biru'}
print(warna)
for tinta in warna:
    print(tinta)
warna.discard('hijau')
print(warna)
warna.add('kuning')
print(warna)

#Tipe Data Dictionary
contoh = dict(
    Universitas = 'Universitas Sulawesi Barat',
    Fakultas = 'Teknik'
)
print(contoh)
print(contoh.get('Universitas'))
for kunci, nilai in contoh.items():
    print(kunci, '=', nilai)
contoh['Jurusan'] = 'Informatika'
print(contoh)
del contoh['Fakultas']
print(contoh)
