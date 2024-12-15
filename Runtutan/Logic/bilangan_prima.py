# Menentukan bilangan prima
# created by Arsa
# 15-12-2024

print('\n')
print('='*30)
print('Menentukan bilangan prima')
print('='*30)

angka = int(input('Masukan angka : '))

if angka > 1:
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            print(f'{angka} bukan bilangan prima')
            break
    else:
        print(f'{angka} adalah bilangan prima')
else:
    print(f'{angka} bukan bilangan prima')