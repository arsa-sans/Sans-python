# Menentukan konversi hari
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan konversi hari')
print('='*30)

TAHUN_HARI = 365
BULAN_HARI = 30

hari = int(input('Input hari : '))

tahun = int(hari / TAHUN_HARI)
hari = hari % TAHUN_HARI
bulan = int(hari / BULAN_HARI)
hari = hari % BULAN_HARI

print(tahun, 'tahun', bulan, 'bulan', hari, 'hari')