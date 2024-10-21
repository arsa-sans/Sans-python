# Next day
# created by Arsa
# 21-10-2024

print('\n')
print('='*30)
print('Next day')
print('='*30)

hari = input('Masukan nama hari : ')

if hari == 'senin':
    print('Besoknya selasa')
elif hari == 'selasa':
    print('Besoknya rabu')
elif hari == 'rabu':
    print('Besoknya kamis')
elif hari == 'kamis':
    print('Besoknya jumat')
elif hari == 'jumat':
    print('Besoknya sabtu')
elif hari == 'sabtu':
    print('Besoknya minggu')
elif hari == 'minggu':
    print('Besoknya senin')
else:
    print('ini bukan nama hari')