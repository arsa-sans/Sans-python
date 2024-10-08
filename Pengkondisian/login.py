# Login
# created by Arsa
# 7-10-2024

print('\n')
print('='*30)
print('Login')
print('='*30)

USERNAME = "arsaprayata72@gmail.com"
PASSWORD = "54n5tamv4n5"

username = input('Masukan username : ')
password = input('Masukan pasword  : ')

if username != USERNAME and password == PASSWORD :
    print('Username tidak tersedia\n')
elif username == USERNAME and password != PASSWORD:
    print('Password salah\n')
else :
    print('Login berhasil\n')