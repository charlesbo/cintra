import unittest
import tempfile
import os.path
from   cintra.models.users import User


class UserTest( unittest.TestCase ):

    def _makeOne(self, username='Chao Meng', cintraid=1):
        
        usr = User(username=username,
                   nickname='Bo',
                   cintraid=cintraid,
                   email='bobomeng@gmail.com',
                   experience = 10**99,
                   points = 100,
                   balance = 3,
                   )
        return usr

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        dbpath = os.path.join(self.tmpdir, 'test.db')
        uri = 'file://' + dbpath
        print uri

    def test_create_user(self):
        usr = self._makeOne('Chao Meng', 1)
        self.assertEqual(usr.username, 'Chao Meng')




