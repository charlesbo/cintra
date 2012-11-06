from persistent.mapping import PersistentMapping
from cintra.models.instruments import InstrumentFolder
from cintra.models.users import UserFolder
from cintra.models.books import OrderbookFolder, BookFolder


class CintraModel(PersistentMapping):
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

        zodb_root['cintra_root'] = cintra_root
        import transaction
        transaction.commit()
    return zodb_root['cintra_root']
