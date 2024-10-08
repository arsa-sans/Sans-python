# Latihan kondisi
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Latihan kondisi')
print('='*30)

air = input('Masukan kondisi air : ')

if air == 'mendidih':
    print('Matikan kompor\n')
else:
    print('Diamkan terus\n')

suhu = int(input('Masukan suhu ruangan : '))
if suhu >= 50:
    print('Bunyikan alarm bahaya\n')
else:
    print('Diamkan')

mobil = input('Masukan kondisi mobil : ')
if mobil == 'rusak':
    print('Naik angkot\n')
else:
    print('Naik mobil\n')

x = int(input('Masukan nilai x : '))
if x % 2 == 0:
    print('Ini genap\n')
else: 
    print('Iini ganjil')


x = int(input('Masukan angka pertama : '))
y = int(input('Masukan angka kedua   : '))
z = int(input('Masukan angka ketiga  : '))

if x > y and x > z :
    print(x)
elif y > x and y > z :
    print(y)
else :
    print(z)

if x < y and x < z :
    print(x)
elif y < x and y < z :
    print(y)
else :
    print(z)