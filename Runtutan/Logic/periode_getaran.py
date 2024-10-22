# Menghitung periode getaran
# Created by arsa
# 22-10-2024

print('\n')
print('='*30)
print('\tMenghitung periode getaran')
print('='*30)
print()

t = int(input('Masukan lama waktu : '))
n = int(input('Masukan jumlah getaran : '))
T = lambda t, n : t / n

print('Periode getaran adalah : ', T(t,n), 'sekon')
print()