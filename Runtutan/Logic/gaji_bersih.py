# Menentukan gaji bersih karyawan
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan gaji bersih karyawan')
print('='*30)

karyawan = input('\nMasukan nama karywan : ')
gaji_pokok = int(input('Masukan gaji pokok karyawan : '))

tunjangan = int(0.2 * gaji_pokok)
pajak = int(0.15 * (gaji_pokok + tunjangan))

gaji_bersih = int((gaji_pokok + tunjangan) - pajak)

print(f'''
gaji pokok : Rp.{gaji_pokok}
tunjangan  : Rp.{tunjangan}
pajak      : Rp.{pajak}
gaji bersih: Rp.{gaji_bersih}
\n''')