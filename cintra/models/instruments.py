from   persistent import Persistent
from   persistent.mapping import PersistentMapping
import datetime


class InstrumentFolder( PersistentMapping ):
    pass


class Instrument( Persistent ):
    def __init__(self, orderbook=None,
                 expireDate=datetime.date.today()+datetime.timedelta(30),
                 settleConditions='',
                 tag='general', description='', category='',
                 marketPrice=5, priceUnit='CNY', priceScale=0.1):
        self.orderbook = orderbook
        self.expireDate = expireDate
        self.settleConditions = settleConditions # conditions when settle 
        self.tag = tag
        self.description = description # description of instrument to users
        self.category = category
        self.marketPrice = marketPrice
        self.lastTradedPrice = -1
        self.priceUnit = priceUnit
        self.priceScale = priceScale # scale for converting price into probability of instrument between 0 and 1.

    def marketProbability( self ):
        return self.marketPrice * self.priceScale


class Option( Instrument ):
    pass


class DigitalOption( Option ):
    pass
