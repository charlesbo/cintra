from persistent import Persistent
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
from datetime import datetime
import logging
log = logging.getLogger(__name__)


class OrderbookFolder( PersistentMapping ):
    pass


class BookFolder( PersistentMapping ):
    pass


class TradeFolder( PersistentMapping ):
    pass

class Order( Persistent ):
    def __init__(self, instrument=None, user=None, buy=True, amount=0, price=5, priceUnit='CNY', orderTime=datetime.utcnow()):
        self.instrument = instrument
        self.user = user
        self.buy = buy
        self.sell = False if buy else True
        self.amount = amount
        self.amountMatched = 0
        self.price = price
        self.priceMatched = -1.0
        self.pricesAmountsMatched = PersistentList()
        self.priceUnit = priceUnit
        self.orderTime = orderTime

    def __cmp__(self, order):
        if self.priceUnit <> order.priceUnit:
            raise ValueError('Cannot compare two orders with different priceUnit!')
        # the cheaper one is smaller
        # when same price, the ealier order is smaller 
        price_cmp_result = self.price>order.price and 1 or (self.price<order.price and -1 or 0)
        time_cmp_result = self.orderTime>order.orderTime and 1 or (self.orderTime<order.orderTime and -1 or 0)
        return price_cmp_result or time_cmp_result

    def matched(self):
        return self.amountMatched==self.amount and self.amountMatched<>0

    def amountAvailable(self):
        return self.amount - self.amountMatched

    def cost(self):
        return sum([p*a for p, a in self.pricesAmountsMatched])

    def match(self, order):
        if order.buy==self.buy:
            return False
        else:
            buyside = self if self.buy else order
            sellside = self if self.sell else order
            if buyside.price >= sellside.price:
                # record match price
                buyside.priceMatched = sellside.price
                sellside.priceMatched = sellside.price

                # recore match amount
                amountMatched = buyside.amountAvailable()<sellside.amountAvailable() and buyside.amountAvailable() or sellside.amountAvailable()
                buyside.amountMatched += amountMatched
                sellside.amountMatched += amountMatched

                buyside.pricesAmountsMatched.append(sellside.price, amountMatched)
                sellside.pricesAmountsMatched.append(sellside.price, amountMatched)
                return True
            else:
                return False


class Trade( Persistent ):
    def __init__(self, buyer=None, seller=None, instrument=None, 
                 amount=0.0, price=0.0, priceUnit='CNY'):
        self.buyer = buyer
        self.seller = seller
        self.instrument = instrument
        self.amount = amount
        self.price = price
        self.priceUnit = priceUnit
        self.tradeTime = datetime.datetime.now()


class Book( Persistent ):
    ''' This is a user book to include user's orders, one per user '''
    def __init__(self, user=None):
        self.user = user
        self.orders = PersistentList()
        self.positions = PersistentMapping()

    def addOrder(self, order):
        if order.instrument in self.positions:
            self.positions[order.instrument].append(order)
        else:
            self.positions[order.instrument] = PersistentList(order)

    def cost(self):
        cost=0.0
        for orders in self.positions.itervalues():
            cost += sum([o.cost() for o in orders])
        return 

    def marketValue(self):
        mktval = 0.0
        for inst, orders in self.positions.iteritems():
            mktval += inst.marketPrice * sum([o.amountMatched for o in orders])
        return mktval


class Orderbook( Persistent ):
    def __init__(self, instrument=None):
        self.instrument = instrument
        self.buyList = PersistentList()
        self.sellList = PersistentList()
        self.matchedList = PersistentList()

    def addOrder(self, order):
        ''' add order in buyList or sellList '''
        if self._matchOrder(order):
            self.instrument.lastTradedPrice = order.priceMatched

        defaultMktP = self.instrument.marketPrice
        lastTradedPrice = self.instrument.lastTradedPrice
        bestBuyPrice = self.buyList[0].price if self.buyList else 0.0
        bestSellPrice = self.sellList[0].price if self.sellList else 0.0
        if bestBuyPrice <= lastTradedPrice <= bestSellPrice:
            mktp = lastTradedPrice
        elif 0<lastTradedPrice<bestBuyPrice:
            mktp = bestBuyPrice
        elif bestSellPrice<lastTradedPrice:
            mktp = bestSellPrice
        else:
            mktp = (bestBuyPrice+bestSellPrice)/2.0 if (bestBuyPrice and bestSellPrice) else (bestBuyPrice or bestSellPrice or defaultMktP)
        self.instrument.marketPrice = mktp

    def _insertOrder(self, order):
        if order.buy:
            self.buyList.append(order)
            self.buyList.sort(reverse=True)
        else:
            self.sellList.append(order)
            self.sellList.sort()

    def _matchOrder(self, order):
        ''' match order with the ones in buyList or sellList '''
        orderList = self.sellList if order.buy else self.buyList
        matchedIdx = -1
        for idx, odr in enumerate(orderList):
            order.match(odr)
            if odr.matched():
                matchedIdx = idx
            if order.matched():
                break
        if matchedIdx > -1:
            log.debug('Matched until %s in %s list'%(matchedIdx, 'sell' if order.buy else 'buy'))
            self.matchedList += orderList[:matchedIdx+1]
            del orderList[:matchedIdx+1]
        if order.matched():
            self.matchedList.append(order)
        else:
            self._insertOrder(order)
        return matchedIdx > -1 or order.matched()
        
