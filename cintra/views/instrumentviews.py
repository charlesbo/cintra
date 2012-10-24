from cintra.models.instruments import DigitalOption, Instrument
from cintra.models.models import InstrumentFolder
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


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
            inst = DigitalOption( tag=tag, description=description,
                                  settleConditions=settleConditions,
                                  category=category)
            inst.__name__ = name
            inst.__parent__ = self.context
            self.context[name] = inst
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

    @view_config(context=InstrumentFolder, renderer='cintra:templates/view_instruments.pt')
    def view_instruments(self):
        return dict(insts=self.context.items())
