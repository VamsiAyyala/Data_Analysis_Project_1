#A class to represent food item
class FoodItem: 
    def __init__(self):
        self.count = 0

    def addItem(self):
        self.count = self.count + 1

    def getCount(self):
        return self.count
#class to represent fruit item
class FruitItem(FoodItem):
    def __init__(self,types):
        FoodItem.__init__(self)
        self.types = types
    def isFruitItem(self, item):
        for i in self.types:
            if i in item:
                FoodItem.addItem(self)
               
#class to represent vegetable item
class VegetableItem(FoodItem):
    def __init__(self,types):
        FoodItem.__init__(self)
        self.types = types

    def isVegetbleItem(self, item):
        for i in self.types:
            if i in item:
                FoodItem.addItem(self)
               
#class to represent meat item
class MeatItem(FoodItem,):
    def __init__(self,types):
        FoodItem.__init__(self)
        self.types = types

    def isMeatItem(self, item):
        for i in self.types:
            if i in item:
                FoodItem.addItem(self)
               

#class to represent sugary item
class SugaryItem(FoodItem):
    def __init__(self,types):
        FoodItem.__init__(self)
        self.types = types

    def isSugaryItem(self, item):
        for i in self.types:
            if i in item:
                FoodItem.addItem(self)
              
