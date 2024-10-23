# Rumus gelombang bunyi
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Rumus gelombang bunyi')
print('='*30)

def kecepatan():
    f = int(input('Masukan frekuensi (Hz) : '))
    λ = int(input('Masukan panjang gelombang (m) : '))
    v = f * λ
    print('Kecepatan gelombang adalah : ', v, 'm/s')
    print()
def frekuensi():
    v = int(input('Masukan kecepatan gelombang (m/s) : '))
    λ = int(input('Masukan panjang gelombang (m) : '))
    f = v / λ
    print('Frekuensi gelombang adalah : ', f, 'Hz')
    print()
def panjang_gelombang():
    f = int(input('Masukan frekuensi (Hz) : '))
    v = int(input('Masukan kecepatan gelombang (m/s) : '))
    λ = v / f
    print('Panjang gelombang adalah : ', λ, 'm')
    print()

def dit():
    ditanyakan = input('Masukan simbol yang ditanyakan (v/f/λ) : ')
    if ditanyakan == 'v':
        kecepatan()
    elif ditanyakan == 'f':
        frekuensi()
    elif ditanyakan == 'λ' or ditanyakan == 'lambda':
        panjang_gelombang()
    else:
        print('Inputan salah')
        dit()
dit()

    
    