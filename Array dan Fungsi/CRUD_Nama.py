# CRUD daftar nama
# Created by arsa
# 18-10-2024

nama_siswa = []

def lihat_nama():
    if len(nama_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        print('\t','='*45)
        print('\t\t\tDaftar Nama Siswa')
        print('\t','='*45)
        for i, nama in enumerate(nama_siswa):
            print(f"\t {i+1}. {nama}")

def tambah_nama():
    print()
    nama_baru = input("Masukkan nama baru: ")
    if nama_baru in nama_siswa:
        print('Nama sudah ada silahkan input nama lain')
    else:
        nama_siswa.append(nama_baru)
        print(f"Nama {nama_baru} telah ditambahkan.")

def edit_nama():
    lihat_nama()
    print()
    indeks = int(input("Masukkan indeks nama yang ingin diedit: ")) - 1
    if 0 <= indeks < len(nama_siswa):
        nama_baru = input("Masukkan nama baru: ")
        nama_siswa[indeks] = nama_baru
        print("Nama berhasil diedit.")
    else:
        print("Indeks tidak valid.")

def hapus_nama():
    print()
    lihat_nama()
    indeks = int(input("Masukkan indeks nama yang ingin dihapus: ")) - 1
    if 0 <= indeks < len(nama_siswa):
        nama_siswa.pop(indeks)
        print("Nama berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def cari_nama():
    print()
    nama_cari = input("Masukkan nama yang ingin dicari: ")
    if nama_cari in nama_siswa:
        print(f"Nama {nama_cari} ditemukan.")
    else:
        print("Nama tidak ditemukan.")

def menu():
    print('\n')
    print('\t','='*40)
    print('\t\t\tMain Menu')
    print('\t','='*40)
    print()

    daftar_menu = [
        'Lihat',
        'Tambah',
        'Edit',
        'Hapus',
        'Cari',
        'Keluar'
    ]

    i = 1
    for data in daftar_menu:
        print('\t',i,':', data)
        i = i + 1
    print()

    pilihan = int(input("Pilih menu: "))
    print()

    if pilihan == 1:
        lihat_nama()
    elif pilihan == 2:
        tambah_nama()
    elif pilihan == 3:
        edit_nama()
    elif pilihan == 4:
        hapus_nama()
    elif pilihan == 5:
        cari_nama()
    elif pilihan == 6:
        print("Terima kasih!")
        exit()
    else:
        print("Pilihan tidak valid.")
while True:
    menu()