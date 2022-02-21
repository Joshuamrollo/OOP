class CellPhone:
    def __init__(self, manu,mdl,rp):
        self.__manufact = manu
        self.__model = mdl
        self.__retail_price = rp
        self.get_model
        self.get_manufact
        self.get_retail_price

    def set_manufact(self, manu):
        self.__manufact = manu
        self.get_manufact
    
    def set_model(self, mdl):
        self.__model = mdl
        self.get_model
    
    def set_retail_price(self, rp):
        self.__retail_price = rp
        self.get_retail_price

    def get_manufact(self):
        print(self.get_manufact)
        return self.__manufact
    
    def get_model(self):
        print(self.get_model)
        return self.__model
    
    def get_retail_price(self):
        print(self.get_retail_price)
        return self.__retail_price