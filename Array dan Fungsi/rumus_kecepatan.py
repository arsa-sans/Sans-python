# Rumus kecepatan
# Created by arsa
# 22-10-2024

print('\n')
print('='*30)
print('\tRumus kecepatan')
print('='*30)

def kecepatan():
    s = int(input('Masukan nilai jarak dalam satuan meter : '))
    t = int(input('Masukan nilai waktu : '))
    v = s / t
    print('Kecepatan benda adalah : ', v, 'm/s')
    print()

def jarak():
    v = int(input('Masukan nilai kecepatan : '))
    t = int(input('Masukan nilai waktu : '))
    s = v * t
    print('Jarak yang ditempuh adalah : ', s, 'm')
    print()

def waktu():
    v = int(input('Masukan nilai kecepatan : '))
    s = int(input('Masukan nilai jarak : '))
    t = v * s
    print('Waktu yang ditempuh adalah : ', t, 's')
    print()

match input('Masukan simbol yang ditanyakan (v/s/t) : '):
    case 'v':
        kecepatan()
    case 's':
        jarak()
    case 't':
        waktu()
    case _:
        print('Invalid input')