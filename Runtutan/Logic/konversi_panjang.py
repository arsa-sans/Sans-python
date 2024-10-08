# Menentukan konversi panjang
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan konversi panjang')
print('='*30)

panjang_benda = int(input('\nMasukan panjang barang dalam satuan meter : '))

inch = panjang_benda // 39
panjang_benda = panjang_benda % 39

kaki = panjang_benda // 3
panjang_benda = panjang_benda % 3

yard = panjang_benda // 1
panjang_benda = panjang_benda % 1

print('Panjang benda dalam satuan berikut adalah : ', inch, 'inci,', kaki, 'kaki,', yard, 'yard\n')