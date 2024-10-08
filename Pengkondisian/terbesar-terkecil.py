# Menentukan nilai terbesar terkecil
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan nilai terbesar dan terkecil')
print('='*30)

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