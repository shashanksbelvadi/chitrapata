import flickr_api as api


class Authentication(object):

    url = ''
    is_authenticated = False

    def __init__(self):
        if self.is_authenticated == False:
            a = api.auth.AuthHandler() # creates the AuthHandler object
            perms = "read" # set the required permissions
            self.url = a.get_authorization_url(perms)
            self.is_authenticated = self.set_auth_flag(True)

    def get_auth_url(self):
        return self.url

    def get_oauth_token(self):
        pass

    def get_oauth_verifier(self):
        pass

    def set_auth_flag(self, val):
        self.is_authenticated = val
