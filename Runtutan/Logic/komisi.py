# Menentukan komisi
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan komisi')
print('='*30)

penjual = input('\nMasukan nama penjual : ')
harga_jual = int(input('Masukan harga jual : '))
komisi = 5 / 100 * harga_jual

print(penjual, 'mendapatkan komisi sebesar : Rp.',round(komisi,0), '\n')