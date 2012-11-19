USERS = {'editor':'editor',  'viewer':'viewer'}
GROUPS = {'editor':['group:editors']}

#from persistent import Persistent
from persistent.mapping import PersistentMapping
from pyramid_zodbconn import get_connection


class SecurityFolder( PersistentMapping ):
    pass


class UsersLoginInfo( PersistentMapping ):
    pass


class GroupsInfo( PersistentMapping ):
    pass


def groupfinder(userid, request):
    conn = get_connection(request)
    app_root = conn.root()['cintra_root']
    userslogininfo = app_root['security']['userslogininfo']

    if userid in userslogininfo:
        return app_root['security']['groupsinfo'].get(userid, [])
