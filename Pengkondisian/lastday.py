# Last day
# created by Arsa
# 21-10-2024

print('\n')
print('='*30)
print('Last day')
print('='*30)

hari = input('Masukan nama hari : ')

if hari == 'senin':
    print('Kemarinnya minggu')
elif hari == 'selasa':
    print('Kemarinnya senin')
elif hari == 'rabu':
    print('Kemarinnya selasa')
elif hari == 'kamis':
    print('Kemarinnya rabu')
elif hari == 'jumat':
    print('Kemarinnya kamis')
elif hari == 'sabtu':
    print('Kemarinnya jumat')
elif hari == 'minggu':
    print('Kemarinnya sabtu')
else:
    print('ini bukan nama hari')