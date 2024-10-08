# Menentukan kecepatan
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Menentukan kecepatan')
print('='*30)

jarak = int(input('\nMasukan jarak yang ditempuh : '))
waktu = int(input('Masukan waktu yang ditempuh : '))

v2 = lambda jarak, waktu : jarak / waktu

print(v2(jarak,waktu))

