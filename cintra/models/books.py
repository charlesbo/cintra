from persistent import Persistent


class Book( Persistent ):
    def __init__(self, positions={}):
        self.positions = positions


class Order( Persistent ):
    def __init__(self, instNum=-1, bos=1, price=0.5):
        self.instNum = instNum
        self.bos = bos
        self.price = price


class OrderBook( Persistent ):
    def __init__(self, buyList=[], sellList=[]):
        self.buyList = buyList
        self.sellList = sellList


    def addOrder(self, order):
        ''' match order, add order in buyList or sellList '''
        pass

    def matchOrder(self, order):
        ''' match order with the ones in buyList or sellList '''
        pass
