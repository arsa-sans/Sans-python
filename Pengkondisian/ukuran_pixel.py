# Menentukan ukuran pixel
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Menentukan ukuran pixel')
print('='*30)

pixel = int(input('\nMasukan ukuran pixel : '))

if pixel > 255 :
    print('Ukuran max pixel adalah 255, ukuran pixel anda menjadi 255\n')
elif pixel < 0 :
    print('Ukuran min pixel adalah 0, ukuran pixel anda menjadi 0\n')
else :
    print('Ukuran pixel anda adalah', pixel, '\n')