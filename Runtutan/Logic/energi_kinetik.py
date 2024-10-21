# Menghitung energi kinetik
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Menghitung energi kinetik')
print('='*30)

massa = int(input('Masukan massa : '))
v = int(input('Masukan kecepatan : '))

ek = lambda massa, v : 1/2 * massa * v * v

print(ek(massa, v))