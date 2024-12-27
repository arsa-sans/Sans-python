# Menentukan nilai mutlak
# created by Arsa
# 15-12-2024

print('\n')
print('='*30)
print('Menentukan nilai mutlak')
print('='*30)

angka = int(input('Masukan angka : '))

# negatif -> positif
if angka < 0:
    mutlak = angka - angka - angka
    double = mutlak * 2
    print('Nilai mutlak ', mutlak)
    print('Nilai double ', double)
else:
    double = angka * 2
    print('Nilai mutlak ',angka)
    print('Nilai double ', double)

# double

# true = ganjil | false = genap
def boolean():
    if angka % 2 == 1:
        print('True')
    else:
        print('False')
boolean()