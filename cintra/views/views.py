from pyramid.view import view_config
from cintra.models.models import CintraModel
import random


@view_config(context=CintraModel, renderer='cintra:templates/cintra.pt')
def cintra_view(context, request):
    insts = context['instruments']
    quoteofthedays = context['quoteofthedays']
    n = len(quoteofthedays)
    if n == 0:
        return {'project': 'Cintra',
            'insts': insts.items(),
            'quote': '--quote of the day is empty...'}
    else:
        i = random.randrange(n)
        #quote = quoteofthedays[i].quote
        quote = ''
        return {'project': 'Cintra',
                'insts': insts.items(),
                'quote': quote}
