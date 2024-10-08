# rumus tabung
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Rumus tabung')
print('='*30)

def tabung() :
    r = int(input('\nMasukan jari-jari : '))
    t = int(input('Masukan tinggi : '))

    LP = lambda r, t : 2*3.14*r* t + 2*3.14*r**2
    V = lambda r, t : 3.14 * r**2 * t

    print(LP(r,t))
    print(V(r,t))
tabung()