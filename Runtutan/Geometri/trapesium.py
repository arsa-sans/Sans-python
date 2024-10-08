# rumus trapesium
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus trapesium')
print('='*30)

ab = int(input('Masukan panjang AB : '))
bc = int(input('Masukan panjang BC : '))
cd = int(input('Masukan panjang CD : '))
ad = int(input('Masukan panjang AD : '))
t = int(input('Masukan tiggi : '))

L = (bc + ad) / 2 * t
K = ab + bc + cd + ad

print('\nLuas = ', L, 'cm2')
print('Keliling = ', K, 'cm\n')