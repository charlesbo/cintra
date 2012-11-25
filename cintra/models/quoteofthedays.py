from   persistent import Persistent
from   persistent.mapping import PersistentMapping
import datetime


class QuoteOfTheDayFolder(PersistentMapping):
    pass


class QuoteOfTheDay(Persistent):
    def __init__(self,
                 idd='',
                 category='',
                 quote='',
                 author='',
                 timestamp=''):
        self.idd = idd
        self.category = category
        self.quote = quote
        self.author = author
        #self.ts = ts
        self.timestamp = timestamp
