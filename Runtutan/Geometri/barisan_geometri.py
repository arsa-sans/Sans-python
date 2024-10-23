# rumus barisan geometri
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus barisan geometri')
print('='*30)

n = int(input('Masukan banyak suku yang dijumlahkan (n) : '))
a = int(input('Masukan suku pertama (a) : '))
r = int(input('Masukan rasio (r) : '))

Un = a * r**(n-1)

print('Hasil barisan geometrinya adalah : ', Un)
