# Shorthand if else
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Shorthand if else')
print('='*30)

a = int(input('Masukan angka pertama : '))
b = int(input('Masukan angka kedua : '))

print(f'{a} > {b}') if a > b else print(f'{a} = {b}') if a == b else print(f'{a} < {b}')
