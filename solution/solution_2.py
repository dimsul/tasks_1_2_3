import requests
from bs4 import BeautifulSoup
import csv


class CountWikipedia:
    def __init__(self, url: str):
        self.__html = requests.get(url)
        self.__soup = BeautifulSoup(self.__html.text, 'html.parser')
        self.__result = {}

    def __check_for_next_page(self) -> str | None:
        for link in self.__soup.find_all('a', title='Категория:Животные по алфавиту'):
            if link.text == 'Следующая страница':
                return f'https://ru.wikipedia.org{link["href"]}'
        return None

    def search_animals(self):
        for a in self.__soup.find('div', class_="mw-category mw-category-columns").find_all('a'):
            if a.text[0] not in self.__result:
                self.__result[a.text[0]] = 0
            self.__result[a.text[0]] += 1

        next_page = self.__check_for_next_page()
        if next_page:
            self.__html = requests.get(next_page)
            self.__soup = BeautifulSoup(self.__html.text, 'html.parser')
            self.search_animals()

    @property
    def result(self):
        return sorted(self.__result.items())


def load_to_csv(data: list[tuple]):
    with open('beasts.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\r')
        for str_ in data:
            writer.writerow(str_)


def run_parser():
    searcher = CountWikipedia('https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')
    searcher.search_animals()
    load_to_csv(searcher.result)


if __name__ == '__main__':
    run_parser()
