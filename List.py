tersedia = ['beras', 'minyak', 'kerupuk', 'garam', 'gula']
def barang():
#Menu
    print('''1. Menambah Barang
2. Menghapus Barang
3. Mengedit Barang
4. Tampilkan Semua Barang
5. Cari Barang
6. Tampilkan Indeks Barang''')
    pilihan = int(input('Masukkan Pilihan : '))
#Menambah Barang
    if pilihan == 1:
        tambah = input('Masukkan Barang yang Ingin Ditambah : ')
        tersedia.append(tambah)
        print(tambah, 'Berhasil Ditambahlkan')
#Menghapus Barang
    elif pilihan == 2:
        hapus = input('Masukkan Nama Barang Yang Ingin Dihapus : ')
        if hapus in tersedia:
            tersedia.remove(hapus)
            print(hapus, 'Berhasil Dihapus')
        else:
            print(hapus, 'Tidak Dapat Dihapus Karena Tidak Terdapat Di Daftar')
#Mengedit Barang
    elif pilihan == 3:
        edit = input('Masukkan Nama Barang Yang ingin Diubah : ')
        editan = input('Ubah Ke : ')
        sedia = False
        for ada in range(0, len(tersedia)):
            if edit == tersedia[ada]:
                ada = True
                if ada:
                    tersedia[ada] = editan
                    print(edit, 'Dapat Diedit')
                else:
                    print(edit, 'Tidak Dapat Diedit')
#Menampilkan Barang
    elif pilihan == 4:
        for brg in tersedia:
            print(brg)
#Cari Barang
    elif pilihan == 5:
        cari = input('Masukkan Nama Barang yang Ingin Anda Cari : ')
        if cari in tersedia:
            print(cari, 'Barang Tersedia')
        else:
            print(cari, 'Barang Tidak Tersedia')
#Menampilkan Indeks Barang
    elif pilihan == 6:
        print('Kode Barang |Nama Barang')
        for indeks, Barang in enumerate(tersedia):
            print(indeks, ' '*10, Barang)
    else:
        print('Perintah Tidak Ditemukan')

        
barang()
print(tersedia)

