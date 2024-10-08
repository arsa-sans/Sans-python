# Kalkulator sederhana
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Kalkulator sederhana')
print('='*30)

angka1 = float(input('\nMasukan angka pertama : '))
operator = input('Masukan operator : ')
angka2 = float(input('Masukan angka kedua : '))

if operator == '+' :
    print(angka1 + angka2)
elif operator == '-' :
    print(angka1 - angka2)
elif operator == '*' :
    print(angka1 * angka2)
elif operator == '/' :
    print(angka1 / angka2)