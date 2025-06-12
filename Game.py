import random

class MyClass:   
    def game(self):
        print('Пограємно в "Вгадай число" :)')
        level = input('Обери рівень складності від 1 до 3: ')
        
        if level == '1':
          number = random.randint(1,10)
          print('Я загадав рандомне число на проміжку від 1 до 10: ') 
          att = 5
          for i in range(0, 5):       
            print(f'Залишилось спроб: {att}')
            us_num = int(input(f'Введіть число: '))
            att = att - 1
            if us_num == number:
              print('Вітаю! Ти вгадав!')
              self.menu()
            else:
             if us_num > number:
                 print('Не вгадав! Менше!')
             else:
                 print('Не вгадав! Більше!')
            
               
        elif level == '2':
            number = random.randint(1,25)
            print('Я загадав рандомне число на проміжку від 1 до 25: ') 
            att = 5
            for i in range(0, 5):       
              print(f'Залишилось спроб: {att}')
              us_num = int(input(f'Введіть число: '))
              att = att - 1
              if us_num == number:
                print('Вітаю! Ти вгадав!')
                self.menu()
              else:
                if us_num > number:
                  print('Не вгадав! Менше!')
                else:
                  print('Не вгадав! Більше!')

        elif level == '3':
          number = random.randint(1,50)
          print('Я загадав рандомне число на проміжку від 1 до 50: ') 
          att = 3
          for i in range(0, 3):       
           print(f'Залишилось спроб: {att}')
           us_num = int(input(f'Введіть число: '))
           att = att - 1
           if us_num == number:
             print('Вітаю! Ти вгадав!')
             self.menu()
          else:
            if us_num > number:
                print('Не вгадав! Менше!')
            else:
                print('Не вгадав! Більше!')
        else:
         print('Неправильно введене число')
         
    def menu(self):
        ch = int(input('Бажаєш грати чи завершити гру? 1/2 - грати/завершити: '))
        if ch == 1:
           self.game()
        elif ch == 2:
           print('До побачення!')
           exit()
        else:
          print('Неправильно введене число!')
          self.menu()

app = MyClass()
app.menu()  
