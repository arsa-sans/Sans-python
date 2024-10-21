# Dasar matriks
# Created by arsa
# 18-10-2024

print('\n')
print('='*30)
print('\tMatriks')
print('='*30)

data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]
# menampilkan matriks
print('\nMenampilkan matriks')
print(data)
print()
print()
print('Menampilkan matriks ke bawah')
for i in data:
    print(i)
print()
print()


# membuat operasi di matriks
operasi = [[0 for j in range(5)] for i in range(2)]

for i in range(len(data)):
  for j in range(len(data[0])):
    operasi[i][j] = data[i][j]*2

print('Menampilkan operasi matriks (dikali 2 dari angka variabel data)')
print(operasi)
print()
print()

print('Menampilkan operasi matriks ke bawah (dikali 2 dari angka variabel data)')
for i in operasi:
   print(i)
print()
print()


# menampilkan angka 10 dari matriks
print('Menampilkan angka 10 dari matriks')
print(data[1][4])
print()
print()


# membuat matriks menggunakan perulangan
print('Membuat matriks menggunakan perulangan')
matriks = [[1 for j in range(4)] 
              for i in range(5)
              ]
print(matriks)
print()
print()


# matriks agar menampilkan ke bawah
print('Membuat matriks menggunakan perulangan dan menampilkan ke bawah')
for i in matriks:
    print(i)
print()
print()