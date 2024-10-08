# Menentukan kalor jenis es
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan kalor jenis es')
print('='*30)

massa = int(input('\033[93mMasukan massa : '))
suhu2 = int(input('\033[93mMasukan suhu kedua : '))
suhu1 = int(input('\033[93mMasukan suhu pertama : '))

Q = massa * 4200 * (suhu2-suhu1)

print(f'\n\033[32mKalor jenis air : {round (Q,2)}J\n')