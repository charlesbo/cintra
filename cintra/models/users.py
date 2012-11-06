from persistent import Persistent
from persistent.mapping import PersistentMapping


class UserFolder( PersistentMapping ):
    pass


class User( Persistent ):
    def __init__(self, book=None, username='', nickname='', cintraid='0', 
                 email='', balance=0.0, points=0.0, experience=0.0 ):
        self.book = book
        self.username = username
        self.nickname = nickname
        self.cintraid = cintraid
        self.email = email
        self.balance = balance    # cash
        self.points = points    # game points
        self.experience = experience    # game experience

    def level(self):
        return len(str(int(self.experience)))
