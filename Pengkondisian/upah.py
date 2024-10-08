# Menentukan upah
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan upah')
print('='*30)

JAMKERJANORMAL = 48
UPAHLEMBUR = 3000
A = 4000
B = 5000
C = 6000
D = 7500

print('\n')
print('='*40)
print('Upah golongan')
print('='*40)

nama = input('\nMasukan nama karyawan : ')
golongan = input('Masukan Golongan Karyawan (A, B, C, D) : ').lower
jjk = int(input('Masukan jumlah jam kerja karyawan dalam seminggu : '))
lembur = int(input('Masukan jam lembur : '))

if golongan == A :
    upahperjam = A
elif golongan == B :
    upahperjam = B
elif golongan == C :
    upahperjam = C
else:
    upahperjam = D

if jjk <= JAMKERJANORMAL :
    upahtotal = jjk * upahperjam
else:
    lembur = jjk - JAMKERJANORMAL
    upahtotal = JAMKERJANORMAL * upahperjam + lembur * UPAHLEMBUR

print('\nNama karyawan : ', nama)
print('Upah total karyawan : ', upahtotal, '\n')