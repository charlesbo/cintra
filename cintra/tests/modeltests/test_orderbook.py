import unittest
from   cintra.models.books import Order, Orderbook
from   cintra.models.instruments import Instrument


class OrderbookTest( unittest.TestCase ):
    def _makeEmptyOrderbook(self, instrument):
        return Orderbook(instrument=instrument)

    def test_create_orderbook(self):
        inst = Instrument()
        ob = self._makeEmptyOrderbook( inst )
        inst.orderbook = ob
        self.assertEqual(ob.instrument, inst)
        self.assertEqual(inst.orderbook, ob)

    def test_addOrder(self):
        inst = Instrument()
        ob = self._makeEmptyOrderbook( inst )
        inst.orderbook = ob
        # [6.5, 6.0, 5.5, 5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0]
        buyprices = [x*0.5 for x in xrange(13,3,-1)]
        buyorders = [Order(inst, buy=True, amount=amt, price=p)
                     for amt, p in zip(xrange(1,11),buyprices)]
        buyorders.sort()
        #[6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0]
        sellprices = [x*0.25 for x in xrange(27,37)]
        sellorders = [Order(inst, buy=False, amount=amt, price=p)
                      for amt, p in zip(xrange(10,0,-1), sellprices)]
        sellorders.sort()
        
        #Add all buys and sells, should not match any
        [ob.addOrder(o) for o in buyorders+sellorders]

        self.assertEqual(len(ob.buyList), 10)
        self.assertEqual(len(ob.sellList),10)
        self.assertEqual(len(ob.matchedList), 0)
        self.assertEqual(inst.marketPrice, 6.625)
        self.assertEqual(inst.lastTradedPrice>0, False)

        #Add a buy order which can match
        abuy = Order(inst, buy=True, amount=5, price=7)
        ob.addOrder(abuy)
        self.assertEqual(len(ob.buyList), 10)
        self.assertEqual(len(ob.sellList),10)
        self.assertEqual(len(ob.matchedList), 1)
        self.assertEqual(ob.instrument.marketPrice, 6.75)
        self.assertEqual(ob.instrument.lastTradedPrice, 6.75)
        self.assertEqual(abuy.matched(), True)

        #Add a buy order which can match more than 1 sell orders
        abuy1 = Order(inst, buy=True, amount=15, price=7.2)
        ob.addOrder(abuy1)
        self.assertEqual(len(ob.buyList), 11)
        self.assertEqual(len(ob.sellList),8)
        self.assertEqual(len(ob.matchedList), 3)
        self.assertEqual(ob.instrument.marketPrice, 7.2)
        self.assertEqual(ob.instrument.lastTradedPrice, 7)
        self.assertEqual(abuy1.matched(), False)

        #Add a sell order which can match
        asell = Order(inst, buy=False, amount=5, price=7)
        ob.addOrder(asell)
        self.assertEqual(len(ob.buyList), 10)
        self.assertEqual(len(ob.sellList),9)
        self.assertEqual(len(ob.matchedList), 4)
        self.assertEqual(ob.instrument.marketPrice, 7)
        self.assertEqual(ob.instrument.lastTradedPrice, 7)
        self.assertEqual(asell.matched(), False)
        
        
