""" аналіз зміни ринкових цін
"""
from data_service import get_goods, get_prices


def create_analiz():
    """ створення заявки на аналіз ринкових цін
    """
    analiz = {
    'index'         : '', # код
    'goods_name'    : '', # назва товару 
    'month_name'    : '', # назва місяця
    'averageprice'  : '', # середня ціна за місяць
    'rozdribprice'  : '', # роздрібна ціна
    'pricechange'   : '', # зміна ціни

    }



    prices = get_prices()
    def get_goods_name(goods_code):
        """повертає назву по коду
        Args:
            goods_code([type]): код товару
        Returns:
            [type]: назва товару
        """
        goods = get_goods()
        for goods in goods: 
            if goods[0] == goods_code:
                return goods[1]

    analiz_list = []
    goods = get_goods()
    for price in prices:
        price[0]=float(price[0].strip())
        price[2]=float(price[2].strip())
        price[3]=float(price[3].strip())
        price[4]=float(price[4].strip())
        price[5]=float(price[5].strip())
        analiz_tmp = analiz.copy()
        analiz_tmp['index'] = price[0]
        analiz_tmp['goods_name'] = price[1]
        analiz_tmp['month_name'] = price[6]
        analiz_tmp['averageprice'] = (price[2]+price[3]+price[4]+price[5])/4
        if price[0] == 10:
            analiz_tmp['rozdribprice']=float(goods[0][2].strip())
        if price[0] == 20:
            analiz_tmp['rozdribprice']=float(goods[1][2].strip())
        if price[0] == 30:
            analiz_tmp['rozdribprice']=float(goods[2][2].strip())
        analiz_tmp['pricechange'] = float(analiz_tmp['averageprice']) / float(analiz_tmp['rozdribprice'])

        analiz_list.append(analiz_tmp)
    return analiz_list

if __name__ == "__main__":
    result = create_analiz()

    for r in result:
        print(r)
