from cintra.models.instruments import DigitalOption, Instrument
from cintra.models.books import Orderbook, Order
from cintra.models.models import InstrumentFolder
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import logging


class InstrumentViews(object):
    def __init__(self, context, request):
        self.request = request
        self.context = context


    @view_config(name='add_instrument', context=InstrumentFolder, renderer="cintra:templates/edit_instrument.pt")
    def add_instrument(self):
        '''
        Add new instrument
        '''
        if 'form.submitted' in self.request.params:
            name = self.request.params['name']
            tag = self.request.params['tag']
            description = self.request.params['description']
            settleConditions = self.request.params['settleConditions']
            category = self.request.params['category']
            marketPrice = self.request.params['marketPrice']
            priceUnit = self.request.params['priceUnit']
            logging.debug( 'marketPrice: %s, type: %s'%(marketPrice, type(marketPrice)) )
            inst = DigitalOption( tag=tag, description=description,
                                  settleConditions=settleConditions,
                                  category=category, marketPrice=marketPrice,
                                  priceUnit=priceUnit)
            inst.__name__ = name
            inst.__parent__ = self.context
            self.context[name] = inst
            approot = self.context.__parent__
            ob = Orderbook(instrument=inst)
            approot['orderbooks'][name] = ob
            inst.orderbook = ob
            return HTTPFound( location = self.request.resource_url(self.context, name) )
        save_url = self.request.resource_url(self.context, 'add_instrument')
        inst = DigitalOption()
        inst.__name__ = ''
        inst.__parent__ = self.context
        return dict(inst=inst, save_url=save_url)

    @view_config(context=Instrument, renderer='cintra:templates/view_instrument.pt')
    def view_instrument(self):
        inst = self.context
        return dict(inst=inst)

    @view_config(name='edit', context=Instrument, renderer='cintra:templates/edit_instrument.pt')
    def edit_instrument(self):
        inst = self.context
        save_url = self.request.resource_url(self.context)
        return dict(inst=inst, save_url=save_url)

    @view_config(context=InstrumentFolder, renderer='cintra:templates/view_instruments.pt')
    def view_instruments(self):
        return dict(insts=self.context.items())

    @view_config(name='buy', context=Instrument, renderer='cintra:templates/edit_order.pt')
    def buy_instrument(self):
        '''
        Buy an instrument.
        '''
        return self._trade_instrument(buy=True)

    @view_config(name='sell', context=Instrument, renderer='cintra:templates/edit_order.pt')
    def sell_instrument(self):
        '''
        Sell an instrument.
        '''
        return self._trade_instrument(buy=False)

    def _trade_instrument(self, buy=True):
        inst = self.context
        if 'form.submitted' in self.request.params:
            price = float(self.request.params['price'])
            amount = int(self.request.params['amount'])
            odr = Order( instrument = inst,
                          user = None, # TODO: add user arguement here
                          buy = buy,
                          amount = amount,
                          price = price,
                          )
            inst.orderbook.addOrder(odr)
            return HTTPFound( location = self.request.resource_url(self.context) )
        tradebehavior = 'buy' if buy else 'sell'
        save_url = self.request.resource_url(self.context, tradebehavior)
        odr = Order()
        return dict(inst=inst, order=odr, save_url=save_url)

