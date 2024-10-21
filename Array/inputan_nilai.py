# Inputan nilai
# Created by arsa
# 18-10-2024

nilai = []

jumlah_nilai_siswa = int(input('\nMasukan keseluruhan jumlah data : '))

for i in range(jumlah_nilai_siswa):
    nilai.append(float(input(f'Nilai ke-{i+1} : ')))

total = max  = 0
min = nilai[0]
for data in nilai:
    total += data

    if data > max:
        max = data

    if data < min:
        min = data

print(total)
print(f'Rata-rata : {total/jumlah_nilai_siswa}')
print(f'Nilai max : {max}')
print(f'Nilai min : {min}')
print()
