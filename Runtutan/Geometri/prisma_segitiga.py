# rumus prisma segitiga
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus prisma segitiga')
print('='*30)

tp = int(input('\nMasukan tinggi prisma : '))
a = int(input('Masukan alas : '))
t = int(input('Masukan tinggi : '))

LP = (a * t) * tp * 2 * (1/2 * a * t) 
V = a * t * tp

print('\nLuas Permukaan = ', LP, 'cm2')
print('Volume = ', V, 'cm3\n')