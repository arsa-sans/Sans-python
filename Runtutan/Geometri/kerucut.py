# rumus kerucut
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Rumus Kerucut')
print('='*30)

r = float(input('\nMasukan Jari-jari : '))
s = float(input('Masukan sisi miring : '))
tinggi = float(input('Masukan tinggi : '))
phi = 3.14

luas_selimut = lambda r, s, tinggi, phi : phi * r * s
luas_permukaan = lambda r, s, tinggi, phi : (phi * r * s) + (phi * r * r)
volume = lambda r, s, tinggi, phi : 1/3 * phi * r * r * tinggi

print(luas_selimut(r, s, tinggi, phi))
print(luas_permukaan(r, s, tinggi, phi))
print(volume(r, s, tinggi, phi))
