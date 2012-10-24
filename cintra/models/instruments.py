from   persistent import Persistent
from   persistent.mapping import PersistentMapping
import datetime


class InstrumentType( PersistentMapping ):
    pass


class InstrumentFolder( PersistentMapping ):
    pass


class Instrument( Persistent ):
    def __init__(self, expireDate=datetime.date.today()+datetime.timedelta(30),
                 settleConditions='',
                 tag='general', description='', category='',
                 marketPrice=5, priceScale=0.1):
        self.expireDate = expireDate
        self.settleConditions = settleConditions # conditions when settle 
        self.tag = tag
        self.description = description # description of instrument to users
        self.category = category
        self.marketPrice = marketPrice 
        self.priceScale = priceScale # scale for converting price into probability of instrument between 0 and 1.

    def marketProbability( self ):
        return self.marketPrice * self.priceScale


class Option( Instrument ):
    pass


class DigitalOption( Option ):
    def __init__(self, expireDate=datetime.date.today()+datetime.timedelta(30),
                 settleConditions='',
                 tag='general', description='', name='', category='',
                 marketPrice=5, priceScale=0.1):
        self.expireDate = expireDate
        self.settleConditions = settleConditions # conditions when settle 
        self.tag = tag
        self.description = description # description of instrument to users
        self.category = category
        self.marketPrice = marketPrice 
        self.priceScale = priceScale # scale for converting price into probability of instrument between 0 and 1.
