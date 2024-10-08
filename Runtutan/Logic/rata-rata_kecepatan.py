# Menentukan rata-rata kecepatan
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan rata-rata kecepatan')
print('='*30)

v1 = int(input('\033[94mMasukan kecepatan pertama : '))
v2 = int(input('\033[94mMasukan kecepatan kedua : '))
t1 = int(input('\033[95mMasukan jarak pertama : '))
t2 = int(input('\033[95mMasukan jarak kedua : '))

hasil = (v2 - v1) / (t2 - t1)

print(f'\033[93mKecepatan rata-rata :  {round (hasil,2)} m/s2 \n')