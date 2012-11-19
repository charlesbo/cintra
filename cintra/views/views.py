from pyramid.view import view_config
from cintra.models.models import CintraModel



@view_config(context=CintraModel, renderer='cintra:templates/cintra.pt')
def cintra_view(context, request):
    insts = context['instruments']
    quotesoftheday = context['quotesoftheday']
    n = len(quotesoftheday)
    i = n-(n-1)
    quoteoftheday = quotesoftheday[i]
    return {'project':'Cintra', 'insts':insts.items(), 'quoteoftheday':quoteoftheday}
