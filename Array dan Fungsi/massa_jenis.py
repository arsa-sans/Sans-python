# Massa jenis
# Created by arsa
# 22-10-2024

print('\n')
print('='*30)
print('\tMassa jenis')
print('='*30)

def massa_jenis():
    m = int(input('Masukan nilai massa benda : '))
    v = int(input('Masukan nilai volume benda : '))
    p = m / v
    print('Massa jenis benda adalah : ', p, 'kg/m3')
    print()

def volume():
    m = int(input('Masukan nilai massa benda : '))
    p = int(input('Masukan nilai massa jenis benda : '))
    v = m * p
    print('Massa volume benda adalah : ', v, 'm3')
    print()

def massa():
    p = int(input('Masukan nilai massa jenis benda : '))
    v = int(input('Masukan nilai volume benda : '))
    m = p * v
    print('Massa benda adalah : ', m, 'kg')
    print()

def ditanyakan():
    dit = input('Masukan simbol yang ditanyakan (p/m/V) : ')
    if dit == 'p':
        massa_jenis()
    elif dit == 'm':
        massa()
    elif dit == 'v' or dit == 'V':
        volume()
    else:
        print('Inputan salah')
        ditanyakan()
ditanyakan()

