sale = int(input("请输入价格："))
"""
if sale>100:
    new_sale = sale*0.8
    print("购买金额超过100元，给20%折扣，折后价为：", new_sale)
elif sale<50:
    new_sale = sale
    print("购买金额低于50元，无折扣，价格为：", new_sale)
else:
    new_sale = sale*0.9
    print("购买金额介于50-100元，给10%折扣，折后价为：", new_sale)
 """
if sale < 50:
    new_sale = sale
    print("购买金额低于50元，无折扣，价格为：", new_sale)
elif sale < 100:
    new_sale = sale * 0.9
    print("购买金额介于50-100元，给10%折扣，折后价为：", new_sale)
else:
    new_sale = sale * 0.8
    print("购买金额超过100元，给20%折扣，折后价为：", new_sale )