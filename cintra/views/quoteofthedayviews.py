from cintra.models.quoteofthedays import QuoteOfTheDayFolder, QuoteOfTheDay
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
        #Add new quote of the day
        quote = QuoteOfTheDay()
        l = len(self.context)
        if l == 0:
            quote.__name__ = 78001
        else:
            quote.__name__ = self.context.keys()[l - 1] + 1
        if 'form.submitted' in self.request.params:
            quotecontent = self.request.params['quoteoftheday']
            idd = quote.__name__
            category = self.request.params['category']
            author = self.request.params['author']
            quote = QuoteOfTheDay(idd=idd,
                                  category=category,
                                  quote=quotecontent,
                                  author=author)
            #quote.__name__ = idd
            self.context[idd] = quote
            approot = self.context.__parent__
            return HTTPFound(location=self.request.resource_url(self.context, idd))
        save_url = self.request.resource_url(self.context, 'add_quoteoftheday')
        quote.__parent__ = self.context
        return dict(quote=quote, save_url=save_url)

    @view_config(context=QuoteOfTheDay,
                 renderer='cintra:templates/view_quoteoftheday.pt')
    def view_quoteoftheday(self):
        # view quote of the day
        quote = self.context
        return dict(quote=quote)

    '''
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
