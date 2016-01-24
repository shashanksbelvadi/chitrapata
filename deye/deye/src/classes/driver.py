import authentication


class Driver(object):
    def __init__(self):
        auth = authentication.Authentication()
        url = auth.get_auth_url()
        print url

if __name__ == "__main__":
    d = Driver()
