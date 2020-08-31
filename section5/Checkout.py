class Checkout:
    class Discount:
        def __init__(self, nItems, price):
            self.nItems = nItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price


    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1


    def addDiscount(self, item, quantity, price):
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount


    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nItems:
                total += self.caclulateItemDiscountedTotal(item, count, discount)
            else:
                total += (self.prices[item] * count)
        else:
            total += (self.prices[item] * count)
        return total

    def caclulateItemDiscountedTotal(self, item, count, discount):
        total = 0 
        nDiscounts = count/discount.nItems
        total += nDiscounts * discount.price
        remaining = count % discount.nItems
        total += remaining * self.prices[item]
        return total 

    

