import random
class MyClass:
    def main_menu(self):
        print('===================================')
        print('Пограємно в "Вгадай число" :))')
        print('Давай спершу оберемо рівень складності:')
        print('1 рівень - від 0 до 10, 5 спроб')
        print('2 рівень - від 0 до 25, 5 спроб')
        print('3 рівень - від 0 до 25, 3 спроби')
        print('4 рівень - від 0 до 50, 5 спроб')
        print('5 рівень - від 0 до 50, 3 спроби')
        print('0 рівень - кастомний')
        print('===================================')
        level = input('Обери рівень складності від 0 до 5: ')
        score = int(0)
        self.game(level, score)
        

    def game(self, level, score):
        print('===================================')
        if level == '1':
            number = random.randint(1, 10)
            print('Я загадав число від 1 до 10.')
            att = 5
        elif level == '2':
            number = random.randint(1, 25)
            print('Я загадав число від 1 до 25.')
            att = 5
        elif level == '3':
            number = random.randint(1, 25)
            print('Я загадав число від 1 до 25.')
            att = 3
        elif level == '4':
            number = random.randint(1, 50)
            print('Я загадав число від 1 до 50.')
            att = 5
        elif level == '5':
            number = random.randint(1, 50)
            print('Я загадав число від 1 до 50.')
            att = 3
        elif level == '0':
            us_min_range = int(input('Введи мінімальне значення: '))
            us_max_range = int(input('Введи максимальне значення: '))
            us_att = int(input('Введи кількість спроб: '))
            number = random.randint(us_min_range, us_max_range)
            print(f'Я загадав число від {us_min_range} до {us_max_range}.')
            att = us_att
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
                print('===================================')
                print('Вітаю! Ти вгадав!')
                score = score + 1
                print(f'Твій рахунок вгаданих чисел: {score}')
                self.menu(score)
                return
            elif us_num > number:
                print('===================================')
                print('Не вгадав! Менше!')
            else:
                print('===================================')
                print('Не вгадав! Більше!')

        print(f'Ти не вгадав. Загадане число було: {number}')
        print(f'Твій рахунок: {score}')
        self.menu()

    def menu(self, score):
        print('===================================')
        ch = input('Бажаєш грати знову? 1 - так / 2 - вийти: ')
        if ch == '1':
            self.main_menu()
        elif ch == '2':
            print(f'До побачення! Ти вгадав {score} чисел, ти молодець!')
            exit()
        else:
            print('Неправильне введення.')
            self.menu()

app = MyClass()
app.main_menu()
