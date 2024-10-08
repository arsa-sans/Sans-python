# rumus bola
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus Bola')
print('='*30)

r = int(input('\nMasukan jari-jari : '))

LP = lambda r : 4 * 3.14 * r * r
V = lambda r : 4/3 * 3.14 * r * r * r

print(LP(r))
print(V(r))