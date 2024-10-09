print('\n')
print('='*40)
print('Pengelompokan')
print('='*40)

kel = int(input('\nMasukan nomor pemain : '))

if kel < 50:
    print('Kel A')
    if kel < 25:
        print('A1')
    elif kel > 25:
        print('A2')
elif kel >= 50:
    print('Kel B')
    if kel < 75:
        print('B1')
    elif kel > 75:
        print('B2')
