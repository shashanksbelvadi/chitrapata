class Bucket(object):
    bucketname = ''
    BUCKET_PATH = ''
    photos_in_bucket = []

    def __init__(self, bucketname, filename):
        self.bucketname = bucketname
        self.BUCKET_PATH = '.photo_cache/'
        connection = connection.getconnection()

        self.download_contents(connection, bucketname, filename)

    def download_contents(self, connection, bucketname, filename):
        bucket = connection.get_bucket('shashankssamplepics')
        for pic in bucket.list():
            keystring = str(pic.key)
            if not os.path.exists('./photo_cache/' + keystring):
                pic.get_contents_to_filename(self.BUCKET_PATH + keystring)