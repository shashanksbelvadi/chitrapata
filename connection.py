import boto


class Connection(object):

    s3_connection = None

    def __init__(self):
        self.makeconnection()

    def makeconnection(self):
        self.s3_connection = boto.connect_s3()
