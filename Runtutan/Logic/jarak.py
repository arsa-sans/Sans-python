# Menentukan jarak tempuh
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan jarak tempuh')
print('='*30)

jarak = int(input('\nMasukan jarak tempuh semut dengan satuan cm : '))

kilometer = jarak // 10000
sisa_jarak = jarak % 10000

meter = jarak // 100
sisa_jarak = sisa_jarak % 100

cm = jarak
sisa_jarak = sisa_jarak % jarak

print('Jarak tempuh semut adalah : ', kilometer, 'km,', meter, 'm,', cm, 'cm\n')