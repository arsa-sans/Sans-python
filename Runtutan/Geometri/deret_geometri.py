# rumus deret geometri
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus deret geometri')
print('='*30)

n = int(input('Masukan banyak suku yang dijumlahkan (n) : '))
a = int(input('Masukan suku pertama (a) : '))
r = int(input('Masukan rasio (r) : '))

if r > 1:
    Sn = a * (r**n - 1) / r - 1
    print('Hasil deret geometri menaik adalah : ', Sn)
elif r < 1:
    Sn = a * (1 - r**n) / 1 - r**n
    print('Hasil deret geometri menurun adalah : ', Sn)
elif r == 1:
    Sn = n * a
    print('Hasil deret geometri rasio = 1 adalah : ', Sn)
