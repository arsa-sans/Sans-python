# Menentukan jenis segitiga
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan jenis segitiga')
print('='*30)

alas1 = int(input('\nMasukan sudut alas 1 : '))
alas2 = int(input('Masukan sudut alas 2   : '))
tinggi = int(input('Masukan sudut tiggi    : '))

if alas1 == alas2 == tinggi:
    print('Segitiga sama sisi \n')
elif alas1 == alas2 > tinggi :
    print('Segitiga sama kaki \n')
elif alas1 == 90 or alas2 == 90:
    print('Segitiga siku-siku \n')
elif alas1 > 90 or alas2 > 90 or tinggi > 90:
    print('Segitiga tumpul \n')
elif alas2 == alas1 > tinggi :
    print('Segitiga sama kaki \n')
elif alas2 == 90 or alas1 == 90:
    print('Segitiga siku-siku \n')
elif alas2 > 90 or alas1 > 90 or tinggi > 90:
    print('Segitiga tumpul \n')
else :
    print('Segitiga sembarang \n')