from django.http import HTTPResponse

def loadinitialpage(request):
    return HTTPResponse("Hello World!")
