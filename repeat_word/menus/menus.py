import os

if __name__ == '__main__':
    from menu_core import Menu
else:
    from repeat_word.menus.menus import Menu


def print_header(text):
    count = (40 - len(text)) // 2 - 1
    output = f'#{" " * count + text + " " * count}#'
    if len(output) < 40:
        output = f'#{" " * count + text + " " * (count + 1)}#'

    print('#' * 40)
    print(output)
    print('#' * 40)


def print_list():
    pass


def print_separator():
    print('-' * 40)


class ListDicts(Menu):
    """Класс Меню списка словарей"""
    def __init__(self, app):
        self.file_names = [file_name for file_name in os.listdir('files')]
        self.file_names.append('назад')
        super().__init__(self.file_names)
        self.app = app

        for file_name in self.file_names:
            self.bind(file_name, self.set_file_name, file_name)
        self.bind('назад', self.back)
        self.run()

    def set_file_name(self, file_name: str):
        self.app.phonetic_word_list.set_file_name(file_name)
        self.back()


class RepeatWords(Menu):
    """Класс Меню повторить слова"""
    def __init__(self, app):
        super().__init__(('словари', 'EN -> RU', 'RU -> EN', 'назад'))
        self.app = app
        self.bind('словари', ListDicts, self.app)
        self.bind('EN -> RU', self.repeat_en_ru)
        self.bind('RU -> EN', self.repeat_ru_en)
        self.bind('назад', self.back)
        self.run()

    def run(self):
        while self._looping:
            print_header(f'Выбран словарь: {self.app.phonetic_word_list.file_name}')
            self.show()
            choice = self.get_num_input('Selection item menu: ')
            self.select(choice)

    def repeat_en_ru(self):
        if self.app.phonetic_word_list.file_name is None:
            ListDicts(self.app)
        self.app.repeat_en_ru()

    def repeat_ru_en(self):
        if self.app.phonetic_word_list.file_name is None:
            ListDicts(self.app)
        self.app.repeat_ru_en()


class WorkDict(Menu):
    """Класс Меню работа со словарями"""
    def __init__(self, app):
        super().__init__(('словари', 'добавить', 'изменить', 'удалить', 'назад'))
        self.app = app
        self.bind('словари', ListDicts, app)
        self.bind('добавить', self.add)
        self.bind('изменить', self.edit)
        self.bind('удалить', self.delete)
        self.bind('назад', self.back)
        self.run()

    def run(self):
        while self._looping:
            print_header(f'Выбран словарь: {self.app.phonetic_word_list.file_name}')
            self.show()
            choice = self.get_num_input('Selection item menu: ')
            self.select(choice)

    def add(self):
        new_file_name = input('Название нового словаря: ')
        open(f'files/{new_file_name}.txt', 'a').close()
        self.app.phonetic_word_list.set_file_name(new_file_name)

    def edit(self):
        if self.app.phonetic_word_list.file_name is None:
            self.select(0)
        self.app.phonetic_word_list.file_launcher()

    def delete(self):
        if self.app.phonetic_word_list.file_name is None:
            self.select(0)
        os.remove(f'files/{self.app.phonetic_word_list.file_name}')
        self.app.phonetic_word_list.file_name = None


class Main(Menu):
    """Класс Меню главное"""
    def __init__(self, app):
        super().__init__(('повторить слова', 'работа с словарями', 'выход'))
        self.app = app
        self.bind('повторить слова', RepeatWords, self.app)
        self.bind('работа с словарями', WorkDict, self.app)
        self.bind('выход', self.exit)
        self.run()


def main():
    class PhoneticWord:
        def __init__(self, word: str, transcription: str, translation: str):
            """Инициализирует слово его транскрипцию и перевод."""
            self.word = word
            self.transcription = transcription
            self.translation = translation

        def __str__(self) -> str:
            pass

        def __repr__(self) -> str:
            pass

        def get_word(self) -> str:
            pass

        def get_transcription(self) -> str:
            pass

        def get_translation(self) -> str:
            pass

    class PhoneticWordList:
        def __init__(self):
            """Инициализирует список с PhoneticWord и имя файла(по умолчанию None)"""
            self.list: list[PhoneticWord] = []
            self.file_name = None

        def get_phonetic_word(self, index: int) -> PhoneticWord:
            """Возвращает PhoneticWord и удаляет его из списка"""
            pass

        def clear(self):
            pass

        def add(self, word: str, transcription: str, translation: str):
            """Добавляет объект PhoneticWord в список"""
            pass

        def set_file_name(self, file_name: str):
            pass

        def load_file(self):
            """Загружает словарь по названию из переменной self.file_name и заполняет список PhoneticWord."""
            pass

    class App:
        """Класс Программа"""

        def __init__(self):
            """Инициализирует список с PhoneticWord и главное меню"""
            self.phonetic_word_list = PhoneticWordList()
            self.main_menu = Main(self)

        @staticmethod
        def get_answer(correct_answer: str, input_answer: str) -> str:
            """Проверяет введённый ответ и возвращает результат."""
            pass

        def repeat_en_ru(self):
            """Запускает мини программу повторения слов."""
            pass

        def repeat_ru_en(self):
            """Запускает мини программу повторения слов."""
            pass
    app = App()


if __name__ == '__main__':
    main()

