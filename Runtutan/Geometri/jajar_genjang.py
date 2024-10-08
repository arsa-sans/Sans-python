# rumus jajar genjang
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Rumus jajar genjang')
print('='*30)

a = int(input('\nMasukan alas : '))
t = int(input('Masukan tinggi : '))

L = lambda a, t : a * t
K = lambda a, t : 2 * (a + t)

print(L(a,t))
print(K(a,t))