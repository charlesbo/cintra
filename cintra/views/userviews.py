from cintra.models.users import User, UserFolder
from cintra.models.books import Book
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import logging


class UserViews(object):
    def __init__(self, context, request):
        self.request = request
        self.context = context

    @view_config(name='add_user', context=UserFolder, renderer="cintra:templates/edit_user.pt")
    def add_user(self):
        '''
        Add new user
        '''
        if 'form.submitted' in self.request.params:
            print 'User Name: ', self.request.params['username']
            username = self.request.params['username']
            nickname = self.request.params['nickname']
            cintraid = self.request.params['cintraid']
            email = self.request.params['email']
            balance = self.request.params['balance']
            points = self.request.params['points']
            experience = self.request.params['experience']
            logging.debug( 'Creating user: %s, cintraid: %s'%(username, cintraid) )
            user = User( username=username, nickname=nickname,
                         cintraid=cintraid, email=email,
                         balance=balance, points=points,
                         experience=experience )
            user.__name__ = cintraid
            user.__parent__ = self.context
            self.context[cintraid] = user
            approot = self.context.__parent__
            bk = Book(user=user)
            approot['books'][cintraid] = bk
            user.book = bk 
            return HTTPFound( location = self.request.resource_url(self.context, cintraid) )
        save_url = self.request.resource_url(self.context, 'add_user')

        user = User()
        user.__name__ = ''
        user.__parent__ = self.context
        return dict(user=user, save_url=save_url)

    @view_config(context=User, renderer='cintra:templates/view_user.pt')
    def view_user(self):
        user = self.context
        return dict(user=user)

    @view_config(context=UserFolder, renderer='cintra:templates/view_users.pt')
    def view_users(self):
        return dict(users=self.context.items())
