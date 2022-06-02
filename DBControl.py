import discord
from discord.ext import commands
from discord.utils import get
import sys
import time
import os
def aprint(text, delay):
  for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(delay)
  print()

helpmenu = '''
--> status (1 - В сети, 2 - Неактивен, 3 - Не беспокоить) = Меняет статус бота
--> servers = Узнать на каких серверах находиться бот
--> message = Отправить сообщение от лица бота
--> file = Отправить файл от лица бота
'''

aprint("DBControl by TurboKoT#9280", 0.08)
aprint("GitHub - https://github.com/IlyaYevtyhov/dbcontrol", 0.05)
print()
while True:
    etoken = input("Введите токен вашего Discord-Бота --> ")
    if etoken == "":
        os.system('cls')
        print("DBControl by TurboKoT#9280")
        print("ERROR: Вы не ввели токен!")
    elif len(etoken) < 20:
        os.system('cls')
        print("DBControl by TurboKoT#9280")
        print("ERROR: Вы ввели некоректный токен!")
    else:
        os.system('cls')
        print("SUCCESS: Подключение к боту..")
        token = etoken
        client = commands.Bot( command_prefix = 'dbcontrol', case_insensitive=True )

        @client.event

        async def on_ready():
            print('SUCCESS: Успешно подключился!')
            await client.change_presence( status = discord.Status.online, activity = discord.Game( 'DBControl by TurboKoT#9280'))
            time.sleep(1)
            while True:
                print(helpmenu)
                select = input("--> ")
                if select == "":
                    print("ERROR: Вы ничего не ввели!")
                elif select == "status 1":
                    os.system('cls')
                    await client.change_presence( status = discord.Status.online, activity = discord.Game( 'DBControl by TurboKoT#9280'))
                    print('SUCCESS: Статус бота был изменен на "В сети"')
                elif select == "status 2":
                    os.system('cls')
                    await client.change_presence( status = discord.Status.idle, activity = discord.Game( 'DBControl by TurboKoT#9280'))
                    print('SUCCESS: Статус бота был изменен на "Неактивен"')
                elif select == "status 3":
                    os.system('cls')
                    await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game( 'DBControl by TurboKoT#9280'))
                    print('SUCCESS: Статус бота был изменен на "Не беспокоить"')
                elif select == "servers":
                    os.system('cls')
                    print("Бот находиться на серверах:")
                    print(client.guilds)
                    print("Общее количество серверов на которых находиться бот:", len(client.guilds))
                elif select == "message":
                    os.system('cls')
                    print(helpmenu)
                    print("|| Введите ID канала")
                    schannel = int(input("--> "))
                    if schannel == "":
                        print("ERROR: Вы ничего не ввели!")
                    elif schannel < 5:
                        print("ERROR: Некоректный ID канала!")
                    else:
                        channel = client.get_channel(schannel)
                        os.system('cls')
                        print(helpmenu)
                        print("|| Введите сообщение")
                        smchannel = input("--> ")
                        if smchannel == "":
                            print("ERROR: Вы ничего не ввели!")
                        else:
                            os.system('cls')
                            await channel.send(smchannel)
                            print("SUCCESS: Сообщение успешно отправленно!")
                elif select == "file":
                    os.system('cls')
                    print(helpmenu)
                    print("|| Введите ID канала")
                    schannel = int(input("--> "))
                    if schannel == "":
                        print("ERROR: Вы ничего не ввели!")
                    elif schannel < 5:
                        print("ERROR: Некоректный ID канала!")
                    else:
                        channel = client.get_channel(schannel)
                        os.system('cls')
                        print(helpmenu)
                        print("|| Введите название файла")
                        schannel = input("--> ")
                        if schannel == "":
                            print("ERROR: Вы не ввели название файла!")
                        else:
                            os.system('cls')
                            await channel.send(file=discord.File(schannel))
                            print("SUCCESS: Файл успешно отправлен!")

        client.run( token )
