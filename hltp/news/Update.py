import requests
import time
from ..config import GLOBAL_SOFT_INFO, COLOR_CODE
from bs4 import BeautifulSoup as bs


class Update:
    def __init__(self) -> None:
        self.__update_link: str = F'{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"][:-4]}/src/news/version'

    def __str__(self) -> str:
        return F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}"

    def __repr__(self) -> str:
        return (F"Description: Обновляет клиент и/или уведомляет о новой версии: {self.__update_link}\n" +
                F"Modules: requests, bs4\n" +
                F"GITHUB/COMMITS/MAIN")

    @property
    def check(self) -> int:

        try:
            # Проверка обновлении по ссылке
            github_commits_content = requests.get(url=self.__update_link)
            if github_commits_content.status_code != 200:
                print(
                    f'{COLOR_CODE["RED"]}[!] Ошибка,{COLOR_CODE["RESET"]}{COLOR_CODE["RED"]} не получилось проверить наличие обновлении! {COLOR_CODE["RESET"]}\n')
                return None

            else:
                bs_content_len: int = len(bs(github_commits_content.text, "html.parser")
                                          .find("div", class_="container-xl")
                                          .find_all("li"))

                return bs_content_len

        except requests.exceptions.ConnectionError as connection_error:
            print(
                f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}[!] Ошибка,{COLOR_CODE["RESET"]}{COLOR_CODE["RED"]} не получилось проверить наличие обновлении! {COLOR_CODE["RESET"]}')
            return {"connection": True}

        except Exception as error:
            print(f'{COLOR_CODE["RED"]}[!] Информация об ошибке: {COLOR_CODE["RESET"]}')
            print(f'{COLOR_CODE["DARK"]}{error}{COLOR_CODE["RESET"]}\n')
            return None

    def get(self):
        """Получение обновлений и обновление"""

        try:
            version_file_name: str = "src/news/version"
            with open(file=version_file_name, mode="r") as file_read:
                now_version = int(file_read.read().strip())
                update_checking = self.check
                if not now_version: now_version = 0

                # Проверка на полученние новой версии и сравнение версии
                if update_checking and type(update_checking) == int and now_version != update_checking:

                    print(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[^] {COLOR_CODE["LI_G"]}'
                          f'Доступно новое {COLOR_CODE["RED"]}обновление!!.{COLOR_CODE["RESET"]}')

                    print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[?] {COLOR_CODE["LI_G"]}'
                          f'Чтобы обновить, {COLOR_CODE["RED"]}удалите эту версию {COLOR_CODE["LI_G"]}и установите новую по исходной ссылке:{COLOR_CODE["CYAN"]}')

                    print(
                        F'[*] {COLOR_CODE["LI_G"]}Ссылка: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')

                    # Запись новых данных в файл версии
                    with open(file=version_file_name, mode="w") as file_write:
                        file_write.write(str(self.check))

                # Новой версии еще нет
                else:
                    if not update_checking:
                        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[*] {COLOR_CODE["LI_G"]}'
                              f'Новые обновлении еще не доступны.{COLOR_CODE["RESET"]}')
                        time.sleep(2.5)




        except FileNotFoundError:
            print(
                f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Отсутствует файл "version"{COLOR_CODE["RESET"]} (ByteNet/src/news/version)')
            user_permission = input(
                f'{COLOR_CODE["RED"]}[?] Создать файл{COLOR_CODE["YELLOW"]} (Да - 1 / Нет - 0): {COLOR_CODE["RESET"]}')
            if not user_permission or user_permission == "1":
                try:
                    open("src/news/version", "w")
                except PermissionError:
                    print(
                        F'{COLOR_CODE["RED"]}[!] К сожалению, не получилось создать файл, обновлении. {COLOR_CODE["LI_G"]}Отсутствует разрешение на создание файлов (попробуйте создать файл в ручную "ByteNet/src/news/version" и прописать там "0").')



        except ValueError:
            print(
                f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Поврежден файл "version"{COLOR_CODE["RESET"]} (ByteNet/src/news/version)')
            print(
                f'{COLOR_CODE["RED"]}[*] {COLOR_CODE["YELLOW"]}Проверка наличия обновлений, недоступно.{COLOR_CODE["RESET"]} Переустановите софт.')
            print(
                F'{COLOR_CODE["RED"]}[*] {COLOR_CODE["YELLOW"]}Ссылка: {COLOR_CODE["CYAN"]}{GLOBAL_SOFT_INFO["SOFT_ORIGINAL_LINK"]}')

        except KeyboardInterrupt:
            print(
                f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')