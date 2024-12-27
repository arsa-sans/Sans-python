# Menentukan validasi kartu kredit
# created by Arsa
# 27-12-2024

print('\n')
print('='*30)
print('Menentukan validasi kartu kredit')
print('='*30)

card_number = input("Masukkan nomor kartu kredit: ")

def luhn_check(card_number):

    card_number = card_number.replace(" ", "")

    if not card_number.isdigit():
        return False
    
    card_number = card_number[::-1]
    
    total = 0

    for i, digit in enumerate(card_number):
        n = int(digit)
        
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        
        total += n

    return total % 10 == 0

if luhn_check(card_number):
    print("Nomor kartu kredit valid.")
else:
    print("Nomor kartu kredit tidak valid.")