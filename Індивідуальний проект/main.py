"""
головний модуль
виводить дані на екран
"""
import os
from process_data import create_analiz
from data_service import show_goods, show_prices, get_goods, get_prices

MAIN_MENU = """
~~~~~~ Обробка заявок ~~~~~~~~
1 - вивід товарів на екран 
2 - запис товарів в файл
3 - вивід списка цін
4 - вивід списка зміни цін
0 - завершує роботу
________________________________
"""

TITLE = "Заявка на продаж устаткування по магазину"

HEADER = \
"""
========================================================================================================
    Код        | Товар             | Місяць         | avg price     |  rozdrib      | changeprice       |
========================================================================================================      
"""
FOOTER = \
'''
=========================================================================================================
'''
STOP_MESSAGE ='Для продовження натисніть Enter'

def show_analiz(analiz_list):
    """ вивід аналізу
    
    Args:
        analiz_list ([type]): список
    """
    print(f"\n\n{TITLE:^91}")
    print(HEADER)

    for analiz in analiz_list:
        print(f"{analiz['index']:<15}",
                f"{analiz['goods_name']:<20}",
                f"{analiz['month_name']:>10}",
                f"{analiz['averageprice']:>10.4}",
                f"{analiz['rozdribprice']:>16.4}",
                f"{analiz['pricechange']:>16.2}"
        ) 
    print(FOOTER) 

def write_analiz(analiz_list):

    with open('./data/dovidnuk2.txt', 'w', encoding="utf-8") as analiz_file:
        for analiz in analiz_list:
            line = \
                str(analiz['index']) + ';' +           \
                str(analiz['goods_name']) + ';' +        \
                str(analiz['month_name']) + ';' +        \
                str(analiz['averageprice']) + ';' +     \
                str(analiz['rozdribprice']) + ';' +     \
                str(analiz['pricechange']) + '\n'
                
            analiz_file.write(line)
    
    print('Файл успішно записано ...')

while True:

    # вивід головного меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    #команди користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)
        
    elif command_number == '4':
        analiz_list = create_analiz()
        show_analiz(analiz_list)
        input(STOP_MESSAGE)
    elif command_number == '2':
        analiz_list = create_analiz()
        write_analiz(analiz_list)
        input(STOP_MESSAGE)
    elif command_number == '1':
        goods = get_goods()
        show_goods(goods)
        input(STOP_MESSAGE)
    
    elif command_number == '3':
        prices = get_prices()
        show_prices(prices)
        input(STOP_MESSAGE)
