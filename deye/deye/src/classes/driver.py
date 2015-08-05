import connection
import bucket


class Driver(object):

    def __init__(self):
        c = connection.Connection()
        b = bucket.Bucket('shashankssamplepics', c.getconnection())
        

if '__name__' == '__main__':
    d = Driver()