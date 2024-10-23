# rumus deret aritmatika menggunakan suku pertama (a) dan selisih (b)
# created by Arsa
# 5-10-2024

print('\n')
print('='*80)
print('Rumus deret aritmatika menggunakan suku pertama (a) dan selisih (b)')
print('='*80)

n = int(input('Masukan banyak suku yang dijumlahkan (n) : '))
a = int(input('Masukan suku pertama (a) : '))
b = int(input('Masukan selisih antara dua bilangan (b) : '))

Sn = n/2 * (2*a + (n - 1)*b)

print('Hasil hitungan deret aritmatika adalah : ', Sn)