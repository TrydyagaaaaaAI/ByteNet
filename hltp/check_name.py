from functools import lru_cache
import requests
import webbrowser

class HttpWebName:
    def __init__(self) -> None:
        self.__base_link: str = "https://rfpoisk.ru/search/?search={name}+{surname}&town={town}&country={country}"
        self.__not_found_text: str = "Информация отсутствует"

    def search(self, name: str, surname: str, town: str, country: str) -> str:
        url = self.__base_link.format(name=name, surname=surname, town=town, country=country)
        response = requests.get(url)
        if response.status_code == 200:
            if self.__not_found_text not in response.text:
                return response.text
            else:
                return "Сайт не найден"
                webbrowser.open(result)
        else:
            return "Ошибка при выполнении запроса"

http_web_number = HttpWebName



