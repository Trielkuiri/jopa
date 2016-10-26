def print_options():
      print('"p" для опций')
      print('"k" чтобы посчитать квадрат числа')
      print('"s" чтобы посчитать сумму 2 чисел')
      print('"q" чтобы выйти')
def kvad(a):            #квадрат числа
      return(a*a)
def sum(b, c):          #сумма чисел
      return(b+c)
choise='p'
while choise!='q':
      if choise=='k':
            print('поиск квадрата числа')
            a=int(input('введи число:  '))
            print('квадрат равен:', kvad(a))
      elif choise=='s':
            print('поиск суммы')
            b=int(input('введи число 1:  '))
            c=int(input('введи число 2:  '))
            print('сумма равна:', sum(b, c))
      elif choise!='q':
            print_options()
      choise=input('options: ')
                  
            

