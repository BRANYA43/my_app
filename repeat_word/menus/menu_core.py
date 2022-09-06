class Menu:
    """Класс Меню"""

    def __init__(self, items: tuple | list):
        """Инициализирует флаг цикла, список пунктов меню и словарь связей пунктов с функциями/объектами"""
        self._looping = True
        self.__items = items
        self.__binded_items = {i: self.__pass for i, _ in enumerate(self.__items)}

    def show(self, register='upper'):
        """Выводит в консоль пункты меню."""
        for i, item in enumerate(self.__items):
            print(f'{i}.{item.capitalize()}')

    def bind(self, item: str, _function, *args):
        """Связывает пункт меню с методов/функцией/объектом"""
        key = self.__items.index(item)
        if args:
            self.__binded_items[key] = (_function, args)
        else:
            self.__binded_items[key] = _function

    def select(self, choice: int):
        """Обрабатывает выбранный пункт меню"""
        if type(self.__binded_items[choice]) is tuple:
            args = self.__binded_items[choice][1]
            self.__binded_items[choice][0](*args)
        else:
            self.__binded_items[choice]()

    def __pass(self):
        """Заглушка"""
        pass

    def back(self):
        """Возвращает в предыдущее меню"""
        self._looping = False
        return

    @staticmethod
    def exit():
        """Полный выход из программы"""
        quit()

    @staticmethod
    def get_num_input(message: str) -> int:
        """Возвращает только число введённое пользователем"""
        ret = ''
        while not ret.isdigit():
            ret = input(message)
        return int(ret)

    def run(self):
        """Запускает работу меню"""
        while self._looping:
            self.show()
            choice = self.get_num_input('Selection item menu: ')
            self.select(choice)


def main():
    class Menu2(Menu):
        def __init__(self):
            super().__init__(('1', '2', '3', 'back'))
            self.bind('back', self.back)
            self.run()

    class Menu1(Menu):
        def __init__(self):
            super().__init__(('1', '2', '3', 'exit'))
            self.bind('1', Menu2)
            self.bind('exit', self.exit)
            self.run()

    menu_1 = Menu1()


if __name__ == '__main__':
    main()
