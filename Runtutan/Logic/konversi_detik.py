# Menentukan konversi detik
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan konversi detik')
print('='*30)

HARI_DETIK = 24 * 60 * 60
JAM_DETIK = 60 * 60

detik = int(input("\nMasukan detik: "))

hari = int(detik/HARI_DETIK)
detik = detik % HARI_DETIK
jam = int(detik / JAM_DETIK)
detik = detik % JAM_DETIK
menit = int(detik/60)
detik = detik % 60

print(hari, 'hari', jam, 'jam', menit, 'menit', detik, 'detik')