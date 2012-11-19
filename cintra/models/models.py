from persistent.mapping import PersistentMapping
from cintra.models.instruments import InstrumentFolder
from cintra.models.users import UserFolder
from cintra.models.books import OrderbookFolder, BookFolder, TradeFolder
from cintra.models.security import SecurityFolder, UsersLoginInfo, GroupsInfo
from pyramid.security import Allow, Everyone


class CintraModel(PersistentMapping):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:managers', 'add_user'),
                (Allow, 'group:superusers', 'add_instrument'),
                (Allow, 'group:users', 'buy'),
                (Allow, 'group:users', 'sell'),
                ]
    __parent__ = __name__ = None


def appmaker(zodb_root):
    if not 'cintra_root' in zodb_root:
        cintra_root = CintraModel()

        instFolder = InstrumentFolder()
        cintra_root['instruments'] = instFolder
        instFolder.__name__='instruments'
        instFolder.__parent__ = cintra_root
        
        orderbookFolder = OrderbookFolder()
        cintra_root['orderbooks'] = orderbookFolder
        orderbookFolder.__name__='orderbooks'
        orderbookFolder.__parent__ = cintra_root
         
        bookFolder = BookFolder()
        cintra_root['books'] = bookFolder
        bookFolder.__name__='books'
        bookFolder.__parent__ = cintra_root

        userFolder = UserFolder()
        cintra_root['users'] = userFolder
        userFolder.__name__ = 'users'
        userFolder.__parent__ = cintra_root

        securityFolder = SecurityFolder()
        cintra_root['security'] = securityFolder
        securityFolder.__name__ = 'security'
        securityFolder.__parent__ = cintra_root

        userslogininfo = UsersLoginInfo()
        cintra_root['security']['userslogininfo'] = userslogininfo
        userslogininfo.__name__ = 'userslogininfo'
        userslogininfo.__parent__ = cintra_root['security']

        groupsinfo = GroupsInfo()
        cintra_root['security']['groupsinfo'] = groupsinfo
        groupsinfo.__name__ = 'groupsinfo'
        groupsinfo.__parent__ = cintra_root['security']


        tradeFolder = TradeFolder()
        cintra_root['trades'] = tradeFolder
        tradeFolder.__name__ = 'trades'
        tradeFolder.__parent__ = cintra_root

        zodb_root['cintra_root'] = cintra_root
        import transaction
        transaction.commit()
    return zodb_root['cintra_root']
