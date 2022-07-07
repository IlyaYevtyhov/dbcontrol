import os
import sys
import time
import string
import random
prefixes = ["The", "Mr", "Mr_", "Mrs", "Mrs_", "Crazy", ""]
suffixes = ["YT", "TT", "2016", "_YT", "_TT", "_2016", "ez", "_ez", ""]
nicks = ["Nikeron", "Kristalik", "Mistik", "Prizrak", "Gently", "Henry", "Dilleron", "Jesus", "Rubix", "Dimak", "Ozzi", "Max"]


os.system("title NickGen by TurboKoT#9280")
def aprint(text, delay):
  for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(delay)
  print()
aprint("NickGen By TurboKoT#9280", 0.07)
while True:
    print()
    print("|| Введите тип генерации (в начале 1 - цифры/2 - рандом. символы/3 - реал. ники)")
    gentype = int(input("--> "))
    if not gentype == 3:
        os.system("cls")
        print("NickGen By TurboKoT#9280")
        print()
        print("|| Введите ник, который должнен быть у ботов")
        nick = input("--> ")
        if nick == "":
            os.system("cls")
            print("NickGen By TurboKoT#9280")
            print("ERROR: Вы не написали ник который должен быть у ботов!")
        elif len(nick)<3 == "":
            print("ERROR: Ник слишком маленький!")
        else:
            os.system("cls")
            print("NickGen By TurboKoT#9280")
            print()
            print("|| Введите кол-во генерируемых ников")
            kolvo = int(input("--> "))
            if kolvo == "":
                print("ERROR: Вы не ввели кол-во генерируемых ников!")
            elif kolvo<1:
                print("ERROR: Вы неккоректно ввели кол-во генерируемых ников!")
            else:
                if gentype == 1:
                    os.system("cls")
                    while kolvo !=0:
                        print(str(kolvo) + nick)
                        kolvo = kolvo-1
                    os.system("msg * Ники сгенерированны! Нажмите Ctrl + A и скопируйте их")
                    input()
                elif gentype == 2:
                    os.system("cls")
                    while kolvo !=0:
                        print(''.join(random.choice(string.ascii_uppercase) for i in range(4)) + nick)
                        kolvo = kolvo-1
                    os.system("msg * Ники сгенерированны! Нажмите Ctrl + A и скопируйте их")
                    input()
    else:
        os.system("cls")
        print("NickGen By TurboKoT#9280")
        print()
        print("|| Введите кол-во генерируемых ников")
        kolvo = int(input("--> "))
        if kolvo == "":
            print("ERROR: Вы не ввели кол-во генерируемых ников!")
        elif kolvo<1:
            print("ERROR: Вы неккоректно ввели кол-во генерируемых ников!")
        else:
            os.system("cls")
            while kolvo !=0:
                rprefix = random.randint(0, 6)
                rsuffix = random.randint(0, 8)
                rnick = random.randint(0, 11)
                print(prefixes[rprefix] + nicks[rnick] + suffixes[rsuffix])
                kolvo = kolvo-1
            os.system("msg * Ники сгенерированны! Нажмите Ctrl + A и скопируйте их")
            input()
                    
