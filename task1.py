menu_item=0
l1=[]
l2=[]

c=0
while menu_item != 9:
    print('выберите 1, чтобы заполнить лист вручную')
    print('выберите 2, чтобы заполнить лист автоматически')
    print('выберите 9, чтобы завершить программу')
    menu_item=int(input('выбери команду:   '))
    if menu_item == 1:
        l1.clear()
        l=int(input('введи длину списка:  '))
        while len(l1) < l:
            name=int(input('введите четное число:  '))
            if (name%2 == 1):
                print('это не четное число')
            elif name == 0:
                print('сегодня 0 не считается за четное.') #Потому что я так хочу
            else:
                l1.append(name)
        print(l1)
    elif menu_item == 2:
        l2.clear()
        l2=[]
        f=0
        e=0
        step=2
        print('создает список четных в выбранном диапазоне')
        while f == 0:
            first=int(input('введите первое значение в списке:  '))
            if (first%2 == 1):
                print('это не четное число')
            elif first == 0:
                print('сегодня 0 не считается за четное.') 
            else:
                l2.append(first)
                f=f+1
        while e == 0:
            end=int(input('введите последнее значение в списке:  '))
            if (end%2 == 1):
                print('это не четное число')
            elif end == 0:
                print('сегодня 0 не считается за четное.') 
            else:
                l2.append(end)
                e=e+1
        l2=list(range(first, end+1, step))
        print(l2)        
             
            

    


