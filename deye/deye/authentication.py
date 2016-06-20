import flickr_api as api


class Authentication(object):

    url = ''

    def __init__(self):
        a = api.auth.AuthHandler() #creates the AuthHandler object
        perms = "read" # set the required permissions
        self.url = a.get_authorization_url(perms)

    def get_auth_url(self):
        return self.url

    def get_oauth_token(self):
        pass

    def get_oauth_verifier(self):
        pass
