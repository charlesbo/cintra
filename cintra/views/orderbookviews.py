from cintra.models.instruments import DigitalOption, Instrument
from cintra.models.books import Orderbook, OrderbookFolder
from cintra.models.models import InstrumentFolder
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


class OrderbookViews(object):
    def __init__(self, context, request):
        self.request = request
        self.context = context

    @view_config(context=Orderbook, renderer='cintra:templates/view_orderbook.pt')
    def view_orderbook(self):
        ob = self.context
        return dict(orderbook = ob, inst = ob.instrument)


    @view_config(context=OrderbookFolder, renderer='cintra:templates/view_orderbooks.pt')
    def view_orderbooks(self):
        return dict(orderbooks = self.context.items())


