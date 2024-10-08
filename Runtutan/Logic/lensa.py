# Menentukan lensa objektif dan lensa okuler
# created by Arsa
# 5-10-2024

print('\n')
print('='*30)
print('Menentukan lensa objektif dan lensa okuler')
print('='*30)

fob = int(input('\033[35mMasukan lensa objektif : '))
fp = int(input('\033[35mMasukan lensa pembalik : '))
fok = int(input('\033[35mMasukan lensa okuler : '))

d = fob + (4*fp) + fok

print(f'\n\033[37mPanjang teropong : {round(d,2)}\n')