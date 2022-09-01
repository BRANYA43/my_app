import csv
import os
from random import randint

from menus.menus import Main


class PhoneticWord:
    def __init__(self, word: str, transcription: str, translation: str):
        """Инициализирует слово его транскрипцию и перевод."""
        self.word = word
        self.transcription = transcription
        self.translation = translation

    def __str__(self) -> str:
        return f'{self.word}-{self.transcription}-{self.translation}'

    def __repr__(self) -> str:
        return self.__str__()

    def get_word(self) -> str:
        return self.word

    def get_transcription(self) -> str:
        return self.transcription

    def get_translation(self) -> str:
        return self.translation


class PhoneticWordList:
    def __init__(self):
        """Инициализирует список с PhoneticWord и имя файла(по умолчанию None)"""
        self.list: list[PhoneticWord] = []
        self.file_name = None

    def get_phonetic_word(self, index: int) -> PhoneticWord:
        """Возвращает PhoneticWord и удаляет его из списка"""
        return self.list.pop(index)

    def clear(self):
        self.list.clear()

    def add(self, word: str, transcription: str, translation: str):
        """Добавляет объект PhoneticWord в список"""
        self.list.append(PhoneticWord(word, transcription, translation))

    def set_file_name(self, file_name: str):
        self.file_name = file_name

    def file_launcher(self):
        os.startfile(os.path.normpath(f'files/{self.file_name}'))

    def load_file(self):
        """Загружает словарь по названию из переменной self.file_name и заполняет список PhoneticWord."""
        self.clear()
        path = f'files/{self.file_name}'
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = f.readlines()
                for row in reader:
                    row = row.replace('\n', '').split(',')
                    self.add(row[0], row[1], row[2])
        except FileNotFoundError:
            print('Файл не найден.')


class App:
    """Класс Программа"""
    def __init__(self):
        """Инициализирует список с PhoneticWord и главное меню"""
        self.phonetic_word_list = PhoneticWordList()
        self.main_menu = Main(self)

    @staticmethod
    def get_answer(correct_answer: str, input_answer: str) -> str:
        """Проверяет введённый ответ и возвращает результат."""
        ret = ''
        if input_answer.lower() == correct_answer.lower():
            ret += f'Правильно, {input_answer}.'
        else:
            ret += f'Ответ {input_answer} не правильный.\n'\
                   f'Правильно будет {correct_answer}.'
        return ret

    def repeat_en_ru(self):
        """Запускает мини программу повторения слов."""
        self.phonetic_word_list.load_file()
        count_word = len(self.phonetic_word_list.list) - 1

        while count_word > 0:
            rand_index = randint(0, count_word)
            phonetic_word = self.phonetic_word_list.get_phonetic_word(rand_index)
            print(phonetic_word.get_word())
            transcription = f'[{input("Транскрипция: ")}]'
            translation = input('Перевод: ')
            print(self.get_answer(phonetic_word.get_transcription(), transcription))
            print(self.get_answer(phonetic_word.get_translation(), translation))

    def repeat_ru_en(self):
        """Запускает мини программу повторения слов."""
        self.phonetic_word_list.load_file()
        count_word = len(self.phonetic_word_list.list) - 1

        while count_word > 0:
            rand_index = randint(0, count_word)
            phonetic_word = self.phonetic_word_list.get_phonetic_word(rand_index)
            print(phonetic_word.get_translation())
            word = input('Перевод: ')
            print(phonetic_word.get_word(), word)


def main():
    app = App()


if __name__ == '__main__':
    main()