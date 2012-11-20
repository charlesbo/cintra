from cintra.models.quoteofthedays import QuoteOfTheDayFolder
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import logging


class QuoteOfTheDayViews(object):
    def __init__(self, context, request):
        self.request = request
        self.context = context

    @view_config(name='add_quoteoftheday',
                 context=QuoteOfTheDayFolder,
                 renderer="cintra:templates/edit_quoteoftheday.pt")
    def add_quoteoftheday(self):
        #Add new instrument
        if 'form.submitted' in self.request.params:
            name = self.request.params['quoteoftheday']
            quoteoftheday = name
            self.context[name] = quoteoftheday
            approot = self.context.__parent__
            return HTTPFound(location=self.request.resource_url(self.context, name))
        save_url = self.request.resource_url(self.context, 'add_instrument')
        quoteoftheday = ""
        #quoteoftheday.__name__ = ''
        #quoteoftheday.__parent__ = self.context
        return dict(quoteoftheday=quoteoftheday, save_url=save_url)

    '''
    @view_config(context=Instrument, renderer='cintra:templates/view_quoteoftheday.pt')
    def view_quoteoftheday(self):
        # view quote of the day
        quoteoftheday = self.context
        return dict(inst=inst)

    @view_config(name='edit', context=Instrument, renderer='cintra:templates/edit_instrument.pt')
    def edit_instrument(self):
        inst = self.context
        save_url = self.request.resource_url(self.context)
        return dict(inst=inst, save_url=save_url)
    '''


    @view_config(context=QuoteOfTheDayFolder, renderer='cintra:templates/view_quoteofthedays.pt')
    def view_quoteofthedays(self):
        # view all quotes of the day
        return dict(quoteofthedays=self.context.items())
