# Rumus gaya newton
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Rumus gaya newton')
print('='*30)

def newton():
    m = int(input('Masukan massa benda (kg) : '))
    a = int(input('Masukan percepatan (m/s) : '))
    F = m * a
    print('Gaya yang dihasilkan adalah : ', F, 'N')
    print()
def massa():
    F = int(input('Masukan gaya (N): '))
    a = int(input('Masukan percepatan (m/s) : '))
    m = F / a
    print('Massa benda adalah : ', m, 'kg')
    print()
def percepatan():
    F = int(input('Masukan gaya (N) : '))
    m = int(input('Masukan massa benda (kg) : '))
    a = F / m
    print('Percepatan benda adalah : ', a, 'm/s')
    print()

def dit():
    ditanyakan = input('Masukan simbol yang ditanyakan (F/m/a) : ')
    if ditanyakan == 'f' or ditanyakan == 'F':
        newton()
    elif ditanyakan == 'm':
        massa()
    elif ditanyakan == 'a':
        percepatan()
    else:
        print('Inputan salah')
        dit()
dit()

    
    