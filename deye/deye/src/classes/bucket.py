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
        try:
            bucket = connection.get_bucket(self.BUCKET_NAME, validate=True)
            print bucket.list()
            for pic in bucket.list():
                keystring = str(pic.key)

                if not os.path.exists('./photo_cache/' + keystring):
                    filepath = os.path.join(self.BUCKET_PATH, '') + keystring
                    self.write_cache_file(pic, filepath, keystring)
        except:
            raise

    def write_cache_file(self, pic, filepath, filename):
        if not os.path.exists(filepath):
            os.makedirs('./' + filepath)
        pic.get_contents_to_filename('/Users/sbelvadi/documents/personal_workspace/deye-website/src/photo_cache/' + filename)