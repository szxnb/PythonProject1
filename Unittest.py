class shoppinglist:
    def __init__(self, shoppinglist):
        self.shoppinglist = shoppinglist
    
    # 返回购物清单里有多少商品
    def get_item_count(self):
        return len(self.shoppinglist)

    # 返回购物清单中商品总金额
    def get_total_price(self):
        return sum(self.shoppinglist.values())