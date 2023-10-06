import os
import webbrowser

try:
    # Проверка на наличие модулей
    from src.config import COLOR_CODE, GLOBAL_SOFT_INFO, print_banner, print_welcome_text
    from src.httpweb_ip import HttpWebIp
    from src.httpweb_mnp import HttpWebMnp
    from src.httpweb_name import HttpWebName
    from src.httpweb_number import HttpWebNumber
    from src.blocked_countries import BlockedCountries
    from src.httpweb_tempmail import HttpWebTempMail
    from time import sleep
    import requests, bs4



except ImportError:
    # Совет по установке модулей и выход
    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] {COLOR_CODE["DARK"]}ВНИМАНИЕ У ВАС ПРОБЛЕМКА, НО МЫ ЕГО РЕШИМ!{COLOR_CODE["RESET"]}')

    print(f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}Оригинально программное обеспечение находиться на: '+
         f'{COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RESET"]}\n'+
         f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}'+
         f'Мы в телеграмме: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_CHANNEL"]}{COLOR_CODE["RESET"]}')
    
    exit(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}У вас отсутствует модули: '+
         f'{COLOR_CODE["CYAN"]}requests{COLOR_CODE["RESET"]} и/или {COLOR_CODE["CYAN"]}'+
         f'bs4{COLOR_CODE["RESET"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["YELLOW"]}'+
         f'Напишите в терминал/консоль: {COLOR_CODE["GREEN"]}apt-get install python3-pip && pip3 install requests bs4 && pip3 install webbrowser{COLOR_CODE["RESET"]}')


if __name__ == "__main__":

    def console_clear() -> None:
        """Очиска консоли (Windows / Linux)"""

        # Очистка для Windows
        if os.sys.platform == "win32":
            os.system("cls")

        # Очистка для Linux
        else:
            os.system("clear")

    # Показ текст соглашении
    print_welcome_text()

    while True:
        # Показ баннера
        print_banner()

        # Меню управления
        console_clear()
        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[1] {COLOR_CODE["URL_L"]}'
            f'Проверить {COLOR_CODE["YELLOW"]}Номер{COLOR_CODE["CYAN"]} телефона.{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[2] {COLOR_CODE["URL_L"]}'
            f'Проверить {COLOR_CODE["YELLOW"]}MNP{COLOR_CODE["CYAN"]} телефона.{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[3] {COLOR_CODE["URL_L"]}'
            f'Проверить {COLOR_CODE["YELLOW"]}IP{COLOR_CODE["CYAN"]} телефона.{COLOR_CODE["RESET"]}\n'

            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[4] {COLOR_CODE["URL_L"]}'
            f'Создать {COLOR_CODE["YELLOW"]}Временную{COLOR_CODE["CYAN"]} почту.{COLOR_CODE["RESET"]}\n'

            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[5] {COLOR_CODE["URL_L"]}'
            f'Проверить {COLOR_CODE["YELLOW"]}ФИ{COLOR_CODE["CYAN"]} по данным.{COLOR_CODE["RESET"]}\n')

        try:
        
            # Выбор варианта поиска
            user_chooice: str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[–] {COLOR_CODE["LI_G"]}'
                f'Выберите вариант : {COLOR_CODE["RESET"]}').strip()
            
            # Поиск по номеру телефона
            if not user_chooice or user_chooice == "1":
                httpweb_number = HttpWebNumber()
                httpweb_number.print_number_results
                sleep(3)

            # Поиск MNP по номеру телефона
            elif user_chooice == "2":
                httpweb_number = HttpWebMnp()
                httpweb_number.print_mnp_results
                sleep(3)

            # Поиск по IP
            elif user_chooice == "3":
                httpweb_number = HttpWebIp()
                httpweb_number.print_ip_results
                sleep(3)

            # Создать временную почту
            elif user_chooice == "4":
                httptemp_mail = HttpWebTempMail()
                httptemp_mail.print_tempmail_info()
                httptemp_mail.print_tempmail_results()

                # Поиск по ФИ
            elif user_chooice == "5":
                http_web_name = HttpWebName()
                name = input(f'{COLOR_CODE["CYAN"]}Введите имя: {COLOR_CODE["RESET"]}')
                surname = input(f"{COLOR_CODE['CYAN']}Введите фамилию: {COLOR_CODE['RESET']}")
                town = input(f"{COLOR_CODE['CYAN']}Введите город: {COLOR_CODE['RESET']}")
                country = input(f"{COLOR_CODE['CYAN']}Введите страну: {COLOR_CODE['RESET']}")
                result = f"https://rfpoisk.ru/search/?search={name}+{surname}&town={town}&country={country}"
                webbrowser.open(result)

                input(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' +
                  f'Чтобы вернуться назад, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}PRESS ')

            # Повторный опрос
            else: continue

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
            break



