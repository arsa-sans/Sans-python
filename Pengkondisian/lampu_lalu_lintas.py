# Lampu lalu lintas
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Lampu lalu lintas')
print('='*30)

WARNA1 = 'merah'
WARNA2 = 'kuning'
WARNA3 = 'hijau'

inputan = input('\nMasukan warna lampu : ').lower()
if inputan == WARNA1 :
    print('Berhenti\n')
elif inputan == WARNA2 :
    print('Hati-hati\n')
elif inputan == WARNA3 :
    print('jalan\n')
else :
    print('Bukan warna lampu lalu lintas')