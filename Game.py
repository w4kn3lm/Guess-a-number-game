import random

class MyClass:
    def main_menu(self):
        print('Пограємно в "Вгадай число" :)')
        level = input('Обери рівень складності від 1 до 3: ')
        self.game(level)

    def game(self, level):
        print('================================')
        if level == '1':
            number = random.randint(1, 10)
            print('Я загадав число від 1 до 10.')
            att = 5
        elif level == '2':
            number = random.randint(1, 25)
            print('Я загадав число від 1 до 25.')
            att = 5
        elif level == '3':
            number = random.randint(1, 50)
            print('Я загадав число від 1 до 50.')
            att = 3
        else:
            print('Неправильний рівень. Спробуй ще раз.')
            self.main_menu()
            return

        while att > 0:
            print(f'Залишилось спроб: {att}')
            try:
                us_num = int(input('Введіть число: '))
            except ValueError:
                print("Це не число!")
                continue

            att -= 1
            if us_num == number:
                print('================================')
                print('Вітаю! Ти вгадав!')
                self.menu()
                return
            elif us_num > number:
                print('================================')
                print('Не вгадав! Менше!')
            else:
                print('================================')
                print('Не вгадав! Більше!')

        print(f'Ти не вгадав. Загадане число було: {number}')
        self.menu()

    def menu(self):
        ch = input('Бажаєш грати знову? 1 - так / 2 - вийти: ')
        if ch == '1':
            self.main_menu()
        elif ch == '2':
            print('До побачення!')
            exit()
        else:
            print('Неправильне введення.')
            self.menu()

app = MyClass()
app.main_menu()
