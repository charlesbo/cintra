from persistent import Persistent
from persistent.mapping import PersistentMapping


class UserFolder( PersistentMapping ):
    pass


class User( Persistent ):
    def __init__(self, username='', nickname='', cintraid=0, 
                 email='', balance=0.0, point=0.0, experience=0.0 ):
        self.username = username
        self.nickname = nickname
        self.cintraid = cintraid
        self.email = email
        self.balance = balance    # cash
        self.point = point    # game point
        self.experience = experience    # game experience

    def level(self):
        return len(str(int(self.experience)))
