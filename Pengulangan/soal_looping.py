# kumpulan soal looping
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Kumpulan soal looping')
print('='*30)
print('\n')

# buah = ['apel', 'mangga', 'jeruk', 'sirsak', 'melon']
# print(buah[0])
# print(buah[3])

# # inisialisasi
# i = 1
# # kondisi
# while i < 6:
#     print(i)
# # iterasi
#     i = i + 1

i = 1 
while i < 4:
    print(i, '-Hello ', end='')
    i = i + 1
print( )

j = 3
while j > 0:
    print(j, '-Hello ', end='')
    j = j - 1
print( )

k = 1
while k < 6:
    print(k, '-Hello ', end='')
    k = k + 2
print( )

l = 0
while l < 7:
    print(l, '-Hello ', end='')
    l = (l + 1) * 2
print( )

m = 10
while m < 101:
    print(m, end=' ')
    m = m + 10
print( )

n = 2000
while n < 2006:
    print(n, end=' ')
    n = n + 1
print( )

BARIS = 5
for a in range(BARIS):
    for b in range(BARIS-a):
        print("", end="")
    for c in range(a+1):
        print("*", end="")
    print('')
BARIS1 = 4
for d in range(BARIS1):
    for d in range(BARIS1-d):
        print(end='')
    for e in range(d+1):
        print("*", end='')
    print()

print('\n')

BARIS = 5
for a in range(BARIS):
    for b in range(BARIS-a):
        print("", end="")
    for c in range(a+1):
        print("*", end="")
    print('')
print('*'*9)
BARIS1 = 5
for d in range(BARIS1):
    for d in range(BARIS1-d):
        print(end='')
    for e in range(d+1):
        print("*", end='')
    print()

print('\n')

BARIS1 = 5
for d in range(BARIS1):
    for d in range(BARIS1-d):
        print(end='')
    for e in range(d+1):
        print("*", end='')
    print()

print('\n')

BARIS2 = 5
for f in range(BARIS2):
    for g in range(BARIS2+f-1):
        print(end='')
    for h in range(f+1):
        print("*", end='')
    print()
baris = 5
for i in range(baris, 0, -1):
    for j in range(i, baris):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

print('\n')

jumlah_baris = 5

for l in range(jumlah_baris):
  spasi = jumlah_baris - l
  print(' ' * spasi, end='')
  for n in range(l+1):
    print(" *", end="")
  print()

print('\n')
print('\n')

jumlah_baris = 10  # Ubah nilai ini untuk mengatur tinggi diamond

# Segitiga atas
for i in range(1, jumlah_baris + 1):
    spasi = jumlah_baris - i
    print(" " * spasi, end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Segitiga bawah
for i in range(jumlah_baris - 1, 0, -1):
    spasi = jumlah_baris - i
    print(" " * spasi, end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

angka = 1
while angka < 6:
    print(angka)
    angka = angka + 1
print('------+')
print(15)

print('\n')

angka = 1
while angka < 6:
    print(angka, end=' ')
    angka = angka + 1
print('= 15')

angka = 3
print(1, end='')
while angka < 6:
    print(' +', angka, end='')
    angka = angka + 2
print(' = 9')

angka = 4
print(2, end='')
while angka < 11:
    print(' +', angka, end='')
    angka = angka + 2
print(' = 30')

angka = 2
print(1, end='')
while angka < 6:
    print(' +', angka, end='')
    angka = angka + 1
print(' = 15')



