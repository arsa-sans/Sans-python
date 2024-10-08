# menentukan index nilai
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan index nilai')
print('='*30)

nilai = int(input('Masukan Nilai Siswa : '))

if nilai >= 90 :
    print('Nilai siswa : A')
elif nilai >= 80 :
    print('Nilai siswa : B')
elif nilai >= 70 :
    print('Nilai siswa : C')
elif nilai >= 60 :
    print('Nilai siswa : D')
elif nilai < 60 :
    print('Nilai siswa : E')