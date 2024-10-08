# menentukan huruf vokal dan konsonan
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan huruf vokal dan konsonan')
print('='*30)

data = input('Masukan Inputan : ')
vokal = [
    "a", 
    "i", 
    "u", 
    "e", 
    "o"
]

if data in vokal :
    print('Ini Vokal\n')
elif data.isdigit() :
   print('Ini angka\n')
else :
    print('Ini konsonan\n')