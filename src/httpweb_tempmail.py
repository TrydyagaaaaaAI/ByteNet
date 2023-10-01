import requests
import random
import string
import time
import os
import requests
from bs4 import BeautifulSoup


COLOR_CODE = {
    "RESET": "\033[0m",      # Сброс цвета [Стиль]
    "UNDERLINE": "\033[04m", # Нижнее подчеркивание [Стиль]
    "GREEN": "\033[32m",     # Зеленый
    "YELLOW": "\033[93m",    # Желтый
    "RED": "\033[31m",       # Красный
    "CYAN": "\033[36m",      # Светло голубой
    "BOLD": "\033[01m",      # Жирный [Стиль]
    "PINK": "\033[95m",      # Розовое
    "URL_L": "\033[36m",     # Ссылки [Стиль]
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m"}      # Темный


class HttpWebTempMail:
    def __init__(self):
        self.checked_ids = []
        self.API = 'https://www.1secmail.com/api/v1/'
        self.domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
        self.domain = random.choice(self.domain_list)


    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def generate_username(self):
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))

        return username

    def check_mail(self, mail=''):
        req_link = f'{self.API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
        r = requests.get(req_link).json()
        length = len(r)

        if length == 0:
            print('')
            time.sleep(4)
            self.clear_console()
        else:
            for msg in r:
                if not msg.get('read') and msg.get('id') not in self.checked_ids:
                    sender = msg.get('from')
                    subject = msg.get('subject')
                    date = msg.get('date')
                    content = msg.get('textBody')

                    if content:
                        print(f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nContent: {content}')
                    else:
                        print(f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nContent: No content')

                    read_msg = f'{self.API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={msg.get("id")}'
                    requests.get(read_msg)

                    self.checked_ids.append(msg.get('id'))


    def delete_mail(self, mail=''):
        url = 'https://www.1secmail.com/mailbox'

        data = {
            'action': 'deleteMailbox',
            'login': mail.split('@')[0],
            'domain': mail.split('@')[1]
        }

        r = requests.post(url, data=data)
        print(f'[X] Почтовый адрес {mail} - удален!\n')

    def print_tempmail_info(self):
        print(f'{COLOR_CODE["CYAN"]}[+] {COLOR_CODE["YELLOW"]}Создание временной почты...{COLOR_CODE["RESET"]}')

    def print_tempmail_results(self):
        try:
            username = self.generate_username()
            mail = f'{username}@{self.domain}'
            print(f'{COLOR_CODE["CYAN"]}[+] {COLOR_CODE["YELLOW"]}Ваш почтовый адрес: {mail}')

            mail_req = requests.get(f'{self.API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

            while True:
                self.check_mail(mail=mail)
                time.sleep(5)

        except(KeyboardInterrupt):
            self.delete_mail(mail=mail)
            print('Программа прервана!')
            input(
                f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' +
                f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}PRESS ')

if __name__ == '__main__':
    httptemp_mail = HttpWebTempMail()
    username = httptemp_mail.generate_username()
    mail = f'{username}@{domain}'
    print(f'{COLOR_CODE["CYAN"]}[+] {COLOR_CODE["YELLOW"]}Ваш почтовый адрес: {mail}')
    httptemp_mail.print_tempmail_info()
    httptemp_mail.print_tempmail_results()
    input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' +
          f'Чтобы удалить почту, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}PRESS ')
