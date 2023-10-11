import os
import webbrowser
import pyfiglet
import time
from time import sleep
import subprocess

text = "ByteNet"
font = "slant"
ascii_banner = pyfiglet.figlet_format(text, font=font).upper()

try:
    # Checking for module availability
    from hltp.config import COLOR_CODE, GLOBAL_SOFT_INFO, print_banner, print_welcome_text
    from hltp.check_ip import HttpWebIp
    from hltp.check_mnp import HttpWebMnp
    from hltp.news.Update import Update
    from hltp.check_name import HttpWebName
    from hltp.check_number import HttpWebNumber
    from hltp.blocked_countries import BlockedCountries
    from hltp.check_tempmail import HttpWebTempMail
except ImportError:
    # Module installation advice and exit
    print(
        f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] {COLOR_CODE["DARK"]}Attention! There is a problem, but we will solve it!{COLOR_CODE["RESET"]}')
    print(
        f'{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}The original software is available at: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}{COLOR_CODE["RESET"]}\n{COLOR_CODE["RED"]}[+] {COLOR_CODE["YELLOW"]}')
    exit(
        f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}You are missing modules: {COLOR_CODE["CYAN"]}requests{COLOR_CODE["RESET"]} and/or {COLOR_CODE["CYAN"]}bs4{COLOR_CODE["RESET"]}. {COLOR_CODE["RED"]}\n[*] {COLOR_CODE["YELLOW"]}Please type in the terminal/console: {COLOR_CODE["GREEN"]}apt-get install python3-pip && pip3 install requests bs4 && pip3 install webbrowser{COLOR_CODE["RESET"]}')

if __name__ == "__main__":
    correct_pass = 'ByteNetFA'
    wpass = input(f'{COLOR_CODE["RED"]}[@]{COLOR_CODE["YELLOW"]} pass: {COLOR_CODE["RESET"]}')
    if wpass != correct_pass:
        print(f'{COLOR_CODE["RED"]}Incorrect password{COLOR_CODE["RESET"]}')
        exit(0)


    def console_clear() -> None:
        """Clear console (Windows / Linux)"""
        # Clearing for Windows
        if os.sys.platform == "win32":
            os.system("cls")
        # Clearing for Linux
        else:
            os.system("clear")


    # Show welcome text
    print_welcome_text()

    while True:
        # Show banner
        ascii_banner = pyfiglet.figlet_format(text, font=font)

        # Menu
        console_clear()
        print(f'{COLOR_CODE["URL_L"]}{ascii_banner}{COLOR_CODE["RESET"]}')
        print(
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[1] {COLOR_CODE["URL_L"]}Проверить {COLOR_CODE["YELLOW"]}Номер{COLOR_CODE["CYAN"]} телефона.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[2] {COLOR_CODE["URL_L"]}Проверить {COLOR_CODE["YELLOW"]}MNP{COLOR_CODE["CYAN"]} номера.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[3] {COLOR_CODE["URL_L"]}Проверить {COLOR_CODE["YELLOW"]}IP{COLOR_CODE["CYAN"]} адресс.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[4] {COLOR_CODE["URL_L"]}Создать {COLOR_CODE["YELLOW"]}Временную{COLOR_CODE["CYAN"]} почту.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[5] {COLOR_CODE["URL_L"]}Найти {COLOR_CODE["YELLOW"]}По{COLOR_CODE["CYAN"]} ФИ.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[7] {COLOR_CODE["URL_L"]}Запустить {COLOR_CODE["YELLOW"]}DDoS атаку.{COLOR_CODE["RESET"]}\n'
            f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[6] {COLOR_CODE["URL_L"]}Проверить {COLOR_CODE["YELLOW"]}Обновления{COLOR_CODE["CYAN"]} программы.{COLOR_CODE["RESET"]}\n'
        )

        try:
            user_choice: str = input(
                f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[–] {COLOR_CODE["LI_G"]}Choose an option: {COLOR_CODE["RESET"]}').strip()

            # Search by phone number
            if not user_choice or user_choice == "1":
                httpweb_number = HttpWebNumber()
                httpweb_number.print_number_results
                sleep(3)

            # Search MNP by phone number
            elif user_choice == "2":
                httpweb_number = HttpWebMnp()
                httpweb_number.print_mnp_results
                sleep(3)

            # Search by IP address
            elif user_choice == "3":
                httpweb_number = HttpWebIp()
                httpweb_number.print_ip_results
                sleep(3)

            # Create temporary mail
            elif user_choice == "4":
                httptemp_mail = HttpWebTempMail()
                httptemp_mail.print_tempmail_info()
                httptemp_mail.print_tempmail_results()

            # Search by name
            elif user_choice == "5":
                http_web_name = HttpWebName()
                name = input(f'{COLOR_CODE["CYAN"]}Enter name: {COLOR_CODE["RESET"]}')
                surname = input(f"{COLOR_CODE['CYAN']}Enter surname: {COLOR_CODE['RESET']}")
                town = input(f"{COLOR_CODE['CYAN']}Enter town: {COLOR_CODE['RESET']}")
                country = input(f"{COLOR_CODE['CYAN']}Enter country: {COLOR_CODE['RESET']}")
                print(
                    f"{COLOR_CODE['URL_L']}https://rfpoisk.ru/search/?search={name}+{surname}&town={town}&country={country}{COLOR_CODE['RESET']}")
                time.sleep(0.3)
                print(f'{COLOR_CODE["CYAN"]}Copy the link above and open it in a web browser.{COLOR_CODE["BOLD"]}')

            elif user_choice == '7':

                ip = input('ip address?: ')

                def pkg():
                    subprocess.call(['ping', ip, '-t', '-l', '500000'])

                for i in range(1000):
                    pkg()

                input(
                    f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}Press any key to go back: {COLOR_CODE["DARK"]}{COLOR_CODE["RESET"]}')

            # Check for technical updates
            elif user_choice == "6":
                # Check for IP blocking
                BlockedCountries().print_ip_result()

                # Check for updates
                Update().get()

            else:
                continue

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Forced interruption!{COLOR_CODE["RESET"]}\n')
            break
