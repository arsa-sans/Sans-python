# if dalam if
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Pengelompokan')
print('='*30)

kel = int(input('\nMasukan nomor pemain : '))

if kel <= 50 :
    print('Kelompok A')
    if kel <= 25:
        print('A1')
    elif kel >= 25:
        print('A2')
if kel > 50 :
    print('Kelompok B')
    if kel <= 75:
        print('B1')
    elif kel > 75:
        print('B2')
