# rumus balok
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Rumus Balok')
print('='*30)

p = int(input('\nMasukan panjang : '))
l = int(input('Masukan lebar : '))
t = int(input('Masukan tinggi : '))

LP = lambda p, l, t : 2 * (p*l + p+t * l+t)
V = lambda p, l, t : p * l * t

print(LP(p,l,t))
print(V(p,l,t))