from pyramid.view import view_config
from cintra.models.models import CintraModel

@view_config(context=CintraModel, renderer='cintra:templates/mytemplate.pt')
def my_view(request):
    return {'project':'cintra'}
