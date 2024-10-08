# menentukan bulan dan hari
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan bulan dan hari')
print('='*30)

bulan = int(input('\nMasukan nomor bulan : '))
tahun = int(input('Masukan tahun : '))

if bulan == 1:
    print('Januari')
elif bulan == 2:
    print('Februari')
elif bulan == 3:
    print('Maret')
elif bulan == 4:
    print('April')
elif bulan == 5:
    print('Mei')
elif bulan == 6:
    print('Juni')
elif bulan == 7:
    print('Juli')
elif bulan == 8:
    print('Agustus')
elif bulan == 9:
    print('September')
elif bulan == 10:
    print('Oktober')
elif bulan == 11:
    print('Novermber')
elif bulan == 12:
    print('Desember')

if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12 :
    jumlah_hari1 = print('31 hari\n')
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11 :
    jumlah_hari2 = print('30 hari\n')
elif bulan == 2 :
        if tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0:
            print('Tahun kabisat berjmulah 29 hari\n')
        else :
            print('Bukan tahun kabisat berjumlah 28 hari\n')