#temperatur suhu untuk manusia
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Temperatur suhu untuk manusia')
print('='*30)

while True:
 temperatur = float(input('\nmasukan suhu tubuh : '))

 if temperatur < 0 :
    print("dapet dry teks dari dia yaa?")
 elif temperatur < 35 :
    print("kamu hipotermia")
 elif temperatur == 36 :
    print("alhamdulillah sehat")
 elif temperatur >= 38 :
    print("kamu demam")
 elif temperatur <= 100 :
    print("selamat! kamu di neraka")