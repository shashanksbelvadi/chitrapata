from boto.s3.connection import S3Connection
import credentials


class Connection(object):
    ACCESS_KEY = ''
    SECRET_KEY = ''

    s3_connection = None

    def __init__(self, access_key, secret_key):
        self.ACCESS_KEY = credentials.Credentials.ACCESS_KEY,
        self.SECRET_KEY = credentials.Credentials.SECRET_KEY

    def getconnection(self):
        ''' 
            Singleton to avoid making duplicate connections 
            during an execution context.
        '''
        if self.s3_connection == None:
            self.s3_connection = S3Connection(
                    self.ACCESS_KEY,
                    self.SECRET_KEY
            )

        return self.s3_connection
