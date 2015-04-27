import boto
import uuid

class Photo(object):
    bucketname = ''
    filename = ''

    def __init__(self, bucketname, filename):
        connection = connection.getconnection()
        photo = self.downloadphoto(connection, bucketname, filename)

    def downloadphoto(self, connection, bucketname, filename):
        key = connection.get_bucket('media.yourdomain.com').get_key('shashankssamplepics/IMG_3759.JPG')
        key.get_contents_to_filename('./photo_cache/cached_photo.JPG')