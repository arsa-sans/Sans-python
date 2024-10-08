# var data mapel
mapel = []

# tampilkan semua data
def lihat_tugas():
    if len(mapel) <= 0:
        print('\tBelum ada tugas mapel ganteng')
    else:
        print('\t*Id nya 0 berarti mepet ke deadline*')
        print('\tKerjain yaaa!')
        for indeks in range(len(mapel)):
            print('\t[%d] %s' % (indeks, mapel[indeks]))

# menambah tugas mapel
def tambah_tugas():
    tugas_baru = input('\tTugas mapel : ')
    mapel.append(tugas_baru)

# edit tugas mapel
def edit_tugas():
    lihat_tugas()
    try:
        indeks = int(input("\tMasukkan id tugas: "))
        if 0 <= indeks < len(mapel):
            tugas_edit = input("\tTugas baru: ")
            mapel[indeks] = tugas_edit
        else:
            print("\tId salah\n")
    except ValueError:
        print("\tPilihannya cuman angka bang\n")

# hapus tugas mapel
def hapus_tugas():
    lihat_tugas()
    try:
        indeks = int(input("\tMasukkan id tugas: "))
        if 0 <= indeks < len(mapel):
            del mapel[indeks]
        else:
            print("\tId salah\n")
    except ValueError:
        print("\tpilihannya cuman angka bang\n")



# menampilkan menu
def lihat_menu():
    print('\n\t==================== Nugas Brayyy ====================\n')
    daftar_menu = {
        1: "Lihat tugas",
        2: "Tambah tugas",
        3: "Edit tugas",
        4: "Hapus tugas",
        5: "Keluar",
    }
    for i in daftar_menu:
        print("\t Id :",i, '\tMenu :',daftar_menu[i])

    try:
        menu = int(input('\n\tPilih menu : '))
        print('\n')
        if menu == 1 in daftar_menu:
            lihat_tugas()
        elif menu == 2 in daftar_menu:
         tambah_tugas()
        elif menu == 3 in daftar_menu:
            edit_tugas()
        elif menu == 4 in daftar_menu:
            hapus_tugas()
        elif menu == 5 in daftar_menu:
            exit()
    except ValueError:
        print("\tPilihannya cuman angka bang")


if __name__ == "__main__":
    while True:
        lihat_menu()


