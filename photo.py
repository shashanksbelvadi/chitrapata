import boto
import uuid

class Photo(object):
    bucketname = ''
    filename = ''

    def __init__(self, connection, bucketname, filename):
        photo = self.downloadphoto(connection, bucketname, filename)

    def downloadphoto(self, connection, bucketname, filename):
        # TO DO