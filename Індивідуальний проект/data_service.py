

def get_goods():
    """ повертає вміст файла 'dovidnuk.txt` у вигляді списка
    Returns:
        'from_file' - список рядків файла
    """
    with open('./data/dovidnuk.txt', encoding="utf8") as goods_file:
        from_file = goods_file.readlines()

    # накопичувач товару
    goods_list =[]

    for line in from_file:
        line_list = line.split(';')
        goods_list.append((line_list))

    return goods_list

def get_prices():

    with open('./data/runok.txt', encoding="utf8") as prices_file:
        from_file = prices_file.readlines()

    prices_list = []
    for line in from_file:
        line_list = line.split(';')
        prices_list.append(line_list)
        
    return prices_list 

def show_goods(goods):
    """виводить список товарів
    Args:
        goods (list): список товару
    """

    # задати інтервал виводу
    goods_code_from = int(input("З якого кода товару? "))
    goods_code_to   = int(input("По який код товару? "))
    
    # накопичує кількість виведених рядків
    kol_lines = 0

    for goods in goods:
        if  goods_code_from  <= int(goods[0]) <= goods_code_to:
            print("код: {:3} назва: {:16} кг: {:20}".format(goods[0], goods[1], goods[2]))
            kol_lines += 1

    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("По вашому запиту товарів не знайдено!")


def show_prices(prices):

    prices_code_from = int(input("З якого коду? "))
    prices_code_to = int(input("По який? ")) 

    kol_lines = 0


    for price in prices:
        if prices_code_from <= int(price[0]) <= prices_code_to:
            print("код: {:5} назва: {:5} кг на 2 число: {:5} на 10: {:5} на 14: {:5} на 24: {:5} місяць: {:5}".format(price[5], price[1],price[2],price[3],price[4],price[5],price[6]))
            kol_lines += 1

    if kol_lines == 0:
        print("По вашому запиту не знайдено")
if __name__ == "__main__":
    goods = get_goods()
    show_goods(goods)

    prices = get_prices()
    show_prices(prices)
