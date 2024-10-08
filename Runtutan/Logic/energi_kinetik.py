# Menghitung energi kinetik
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Menghitung energi kinetik')
print('='*30)

massa = int(input('\033[35mMasukan massa : '))
v = int(input('\033[35mMasukan kecepatan : '))

ek = lambda massa, v : 1/2 * massa * v * v

print(ek(massa, v))