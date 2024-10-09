import random

user_position = random.randint(1, 5)

print('\n')
print('='*45)
print('\t\tGame random')
print('='*45)
print()

username = input('Masukan nama kamu : ')

print()
print(f'''Halo {username} perhatikan goa di bawah ini!
[_]  [_]  [_]  [_]  [_]
''')

# jawaban
def answare():
    user_chose =  int(input('Menurutmu goa yang selamat untuk dilewati ada di nomor berapa? [masukan angka antara 1 sampai 5] : '))
    confirm = input('Apakah kamu yakin ? [y/n] : ')

# hasil
    def result():
        if user_chose == user_position:
            print(f'''Kamu selamat melewati rintangan {username}! Kembangkan lagi instingmu!''')
            print()
        elif user_chose > 5:
            print('Goanya cuman ada 5', username,'!')
            answare()
        else:
            print(f'''Kamu mati {username}! satu-satunya goa yang selamat adalah nomor {user_position}''')
            print()
# konfirmasi
    def confirmation():
        if confirm == 'y' or confirm == 'Y':
            print()
            result()
        elif confirm == 'n' or confirm == 'N':
            print()
            answare()
    confirmation()
answare()