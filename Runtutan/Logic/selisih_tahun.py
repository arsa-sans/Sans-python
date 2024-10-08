# Menentukan selisih tahun
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan selisih tahun')
print('='*30)

TAHUN_HARI = 365
BULAN_HARI = 30

tahun1 = int(input('\nMasukan Tahun Pertama : '))
bulan1 = int(input('Masukan Bulan Pertama : '))
hari1 = int(input('Masukan Tanggal Pertama : '))

tahun2 = int(input('\nMasukan Tahun Kedua : '))
bulan2 = int(input('Masukan Bulan Kedua : '))
hari2 = int(input('Masukan Tanggal Kedua : '))

total_hari1 = tahun1 * TAHUN_HARI + bulan1 * BULAN_HARI + hari1
total_hari2 = tahun2 * TAHUN_HARI + bulan2 * BULAN_HARI + hari2

selisih_hari = total_hari2 - total_hari1

tahun = int(selisih_hari / TAHUN_HARI)
sisa_hari = selisih_hari % TAHUN_HARI
bulan = int(sisa_hari / BULAN_HARI)
hari = sisa_hari % BULAN_HARI

print('Selisihnya adalah : ', tahun, 'tahun', bulan, 'bulan', hari, 'hari\n')
