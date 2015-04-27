import os


class Bucket(object):
    BUCKET_NAME = ''
    BUCKET_PATH = ''

    photos_in_bucket = []

    def __init__(self, bucketname, connection):
        self.BUCKET_NAME = bucketname
        self.BUCKET_PATH = '.photo_cache/' + bucketname
        self.download_contents(connection)

    def download_contents(self, connection):
        bucket = connection.get_bucket(self.BUCKET_NAME)

        for pic in bucket.list():
            keystring = str(pic.key)

            if not os.path.exists('./photo_cache/' + keystring):
                pic.get_contents_to_filename(self.BUCKET_PATH + keystring)
                photos_in_bucket.add(self.BUCKET_PATH + keystring)