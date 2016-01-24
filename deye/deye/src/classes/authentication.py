import flickr_api as api


class Authentication(object):

    def __init__(self):
        a = api.auth.AuthHandler() #creates the AuthHandler object
        perms = "read" # set the required permissions
        url = a.get_authorization_url(perms)
        print url
