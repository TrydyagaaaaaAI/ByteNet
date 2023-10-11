import requests
from .config import COLOR_CODE, console_clear
from functools import lru_cache

class HttpWebNumber:
    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "Информация отсутствует"

    # Получение данных по номеру
    @lru_cache(maxsize=None)
    def __return_number_data(self, user_number: str) -> dict:
        # Получение данных MNP по номеру тел. клиента 
        try:
            __result_number_data = requests.get(self.__check_number_link + user_number)
        
            if __result_number_data.ok:
                __result_number_data: dict = __result_number_data.json()

            else:
                __result_number_data: dict = {"status_error": True}

        except requests.exceptions.ConnectionError as connection_error:
            __result_number_data: dict = {"status_error": True}
        
        return __result_number_data

    # Ввод данных в консоль
    @property
    def print_number_results(self) -> str:
        """Вывод полученных данных"""

        try:
            console_clear()
            _user_number: str = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}1{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                f'Введите номер телефона{COLOR_CODE["DARK"]} (+7): {COLOR_CODE["RESET"]}').strip()
            
            # Если ввели номер телефона
            if _user_number:
                print(f'{COLOR_CODE["RED"]}[~] {COLOR_CODE["YELLOW"]}Ищем данные.. {COLOR_CODE["RESET"]}\n')
                _get_user_number_data = self.__return_number_data(user_number=_user_number)

                # Проверка статуса ошибки
                if _get_user_number_data.get("limit") <= 0:
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] '+
                        f'{COLOR_CODE["RESET"]}К сожалению, вы израсходовали {COLOR_CODE["DARK"]}все лимиты')
                    
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["RESET"]}Всего лимитов: {COLOR_CODE["DARK"]}'+
                        f'{str(_get_user_number_data.get("limit", self.__not_found_text))}{COLOR_CODE["RESET"]}')
                
                elif _get_user_number_data.get("status_error") or _get_user_number_data.get("error"):
                    print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Данные не найдены {COLOR_CODE["RESET"]}\n')


                # Ввод данных о номере
                else:
                    _number_data_unknown = _get_user_number_data
                    _number_data_country = _get_user_number_data.get('country')
                    _number_data_capital = _get_user_number_data.get('capital')
                    _number_data_region = _get_user_number_data.get('region')
                    _number_data_other = _get_user_number_data.get('0')

                    if not _number_data_region:
                        _number_data_region: dict = {"autocod": self.__not_found_text, 
                        "name": self.__not_found_text,
                        "okrug": self.__not_found_text}

                    # Страна            
                    # Для украины информация о стране отсутствует
                    if _number_data_country.get("country_code3") == 'UKR':
                        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                            f'{COLOR_CODE["LI_G"]}Страна:{COLOR_CODE["F_CL"]} Украина{COLOR_CODE["RESET"]}')
                    
                    else:
                        print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] '+
                            f'{COLOR_CODE["CYAN"]}Страна:{COLOR_CODE["YELLOW"]} '+
                            f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                            f'{_number_data_country.get("fullname", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Город
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Город:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_other.get("name", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Почтовый индекс
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Почтовый индекс:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_other.get("post", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Код валюты
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Код валюты:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_country.get("iso", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Телефонные коды
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Телефонные коды:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_capital.get("telcod", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Посмотреть в wiki
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Посмотреть в wiki:{COLOR_CODE["RESET"]}{COLOR_CODE["YELLOW"]}{COLOR_CODE["UNDERLINE"]} ' +
                          f'{_number_data_other.get("wiki", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Регион номереа авто
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Гос. номер региона авто:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_region.get("autocod", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Оператор
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Оператор:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_other.get("oper", self.__not_found_text)}, {COLOR_CODE["DARK"]}' +
                          f'{_number_data_other.get("oper_brand", self.__not_found_text)}, ' +
                          f'{_number_data_other.get("def", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Местоположение
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Местоположение:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                          f'{_number_data_region.get("name", self.__not_found_text)}, ' +
                          f'{_number_data_other.get("name", self.__not_found_text)}{COLOR_CODE["DARK"]} (' +
                          f'{_number_data_other.get("latitude", self.__not_found_text)}, ' +
                          f'{_number_data_other.get("longitude", self.__not_found_text)}){COLOR_CODE["RESET"]}')

                    # Открыть на карте (google)
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Открыть на карте (google):{COLOR_CODE["RESET"]}{COLOR_CODE["YELLOW"]}{COLOR_CODE["UNDERLINE"]} ' +
                          f'https://www.google.com/maps/place/' +
                          f'{_number_data_other.get("latitude", self.__not_found_text)}+' +
                          f'{_number_data_other.get("longitude", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Локация
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Локация:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_unknown.get("location", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Язык
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Язык общения:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_country.get("lang", self.__not_found_text).title()}, ' +
                          f'{_number_data_country.get("langcod", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Край/Округ/Область
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Край/Округ/Область:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_region.get("name", self.__not_found_text)}, ' +
                          f'{_number_data_region.get("okrug", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Столица
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Столица:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_capital.get("name", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    # Широта/Долгота
                    print(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[*] ' +
                          f'{COLOR_CODE["CYAN"]}Широта/Долгота:{COLOR_CODE["YELLOW"]} ' +
                          f'{_number_data_other.get("latitude", self.__not_found_text)}, ' +
                          f'{_number_data_other.get("longitude", self.__not_found_text)}{COLOR_CODE["RESET"]}')

                    
                    print(f'\n{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[-] {COLOR_CODE["LI_G"]}Возможные соц. сети/меседжери : {COLOR_CODE["RESET"]}')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}0{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://www.instagram.com/accounts/password/reset{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск аккаунта в Instagram')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}2{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск аккаунта FaceBook')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}3{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://www.linkedin.com/checkpoint/rp/request-password-reset?{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск аккаунта Linkedin')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}4{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск аккаунта OK')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}5{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://twitter.com/account/begin_password_reset{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск аккаунта Twitter')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}6{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://viber://add?number={COLOR_CODE["PINK"]}{_user_number}{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Поиск номера в Viber')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}7{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://skype:{COLOR_CODE["PINK"]}{_user_number}{COLOR_CODE["URL_L"]}?call{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Звонок на номер с Skype')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}8{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://t.me/{COLOR_CODE["PINK"]}{_user_number}{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Открыть аккаунт в Телеграмме')
                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}9{COLOR_CODE["CYAN"]}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}tel:{COLOR_CODE["GREEN"]}{_user_number}{COLOR_CODE["RESET"]}{COLOR_CODE["DARK"]} - Звонок на номер с телефона')
                
                    # Всего лимитов
                    print(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[+] '+
                        f'{COLOR_CODE["RED"]}Всего лимитов: '+
                        f'{str(_get_user_number_data.get("limit", self.__not_found_text))}{COLOR_CODE["RESET"]}')

                    input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                        f'Чтобы завершить поиск, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}PRESS ')
            
            # Если не ввели номер телефона
            else:
                print(f'{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Ошибка, введите номер телефона! {COLOR_CODE["RESET"]}\n')

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')

