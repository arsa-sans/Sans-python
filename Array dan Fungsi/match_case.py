# Match case
# Created by arsa
# 22-10-2024

print('\n')
print('='*30)
print('\tMatch case')
print('='*30)

def sekolah():
    print()
    print('Yang harus dilakukan di sekolah adalah : ')
    print('Perhatikan guru sedang menjelaskan')
    print('Kerjakan tugas')
    print('Pahami materi')
    print('Piket')
    print('Bayar uang kas')
    print()

def rumah():
    print()
    print('Yang harus dilakukan di rumah adalah :')
    print('''Cuci baju
Sertika baju
Cuci piring
Kerjakan PR
Belajar
''')
    print()
    
match input('Tempat yang ingin dikunjungi (rumah/sekolah): '):
    case 'sekolah':
        sekolah()
    case 'rumah':
        rumah()
    case _:
        print('Invalid input')

