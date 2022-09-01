import csv
from random import randint
import os


class Word:
    def __init__(self, word: str, transcription: str, translation: str):
        self.word = word
        self.transcription = transcription
        self.translation = translation

    def __str__(self):
        return f'{self.word}-{self.transcription}-{self.translation}'

    def __repr__(self):
        return self.__str__()


class App:
    def __init__(self):
        self.word_list: list[Word] = []
        self.file_list = [file_name for file_name in os.listdir('files')]
        self.file_name: str | None = None

    def get_words(self) -> list[Word]:
        return self.word_list.copy()

    @staticmethod
    def is_translation(word: Word, translation: str) -> bool:
        if word.translation == translation:
            return True
        return False

    @staticmethod
    def is_transcription(word: Word, transcription: str) -> bool:
        if word.transcription == transcription:
            return True
        return False

    @staticmethod
    def is_word(word: Word, _word: str) -> bool:
        if word.word == _word:
            return True
        return False

    def add_word(self, word: str, transcription: str, translation: str):
        self.word_list.append(Word(word, transcription, translation))

    def load_file(self, file_name: str):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.add_word(row['word'], row['transcription'], row['translation'])
        except FileNotFoundError:
            self.save_file(file_name)

    def save_file(self, file_name: str):
        with open(file_name, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('word', 'transcription', 'translation'))
            if self.word_list:
                for word in self.word_list:
                    writer.writerow((word.word, word.transcription, word.translation))
            else:
                writer.writerow(('SIZE', '[САЙЗ]', 'РАЗМЕР'))


def get_num_input(message: str) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


def main():
    app = App()
    app.load_file('files/word_dict.csv')
    point = 0
    max_point = len(app.get_words())
    words = app.get_words()
    menu = ['EN -> RU', 'RU -> EN']
    for i, menu in enumerate(menu):
        print(f'{i}.{menu.upper()}')

    choice = get_num_input('Выберите пункт меню: ')

    if choice == 0:
        while len(words) > 0:
            word = words.pop(randint(0, len(words) - 1))
            print(word.word)
            transcription = f"[{input('Транскрипция: ')}]"
            translation = input('Перевод: ').upper()
            is_translation = app.is_translation(word, translation)
            is_transcription = app.is_transcription(word, transcription)
            if is_translation and is_transcription:
                point += 1
                print('Правильно')
            else:
                if not is_transcription:
                    print(f'Неправильная транскрипция {transcription}.\nДолжно быть {word.transcription}')
                if not is_translation:
                    print(f'Неправильный перевод {translation}.\nДолжно быть {word.translation}')

            print('=' * 20)

        print(f'{point}/{max_point}.')

    else:
        while len(words) > 0:
            word = words.pop(randint(0, len(words) - 1))
            print(word.translation)
            _word = input('Перевод: ').upper()
            is_word = app.is_word(word, _word)
            if is_word:
                point += 1
                print('Правильно')
            else:
                if not is_word:
                    print(f'Неправильный перевод {_word}.\nДолжно быть {word.word}')

            print('=' * 20)

        print(f'{point}/{max_point}.')


if __name__ == '__main__':
    main()
