from flask import request

__author__ = 'wuxian'


scopes = ['AdminScope', 'UserScope']


class UserScope:
    auths = ['v1.get_user']


class AdminScope:
    auths = ['v1.super_get_user']


def is_in_scope(scope_code):
   scope = globals()[scopes[scope_code]]()
   if request.endpoint in scope.auths:
       return True
   else:
       return False



