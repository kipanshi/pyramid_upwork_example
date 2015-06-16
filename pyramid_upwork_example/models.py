from pyramid.security import Allow, Authenticated, Deny, Everyone


class RootFactory(object):
    """This object sets the security for our application."""
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Deny, Authenticated, 'login'),
        (Allow, Everyone, 'login'),
    ]

    def __init__(self, request):
        pass
