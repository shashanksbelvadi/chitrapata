from django.http import HttpResponse

def index(request):
    template_name = 'deye/index.html'
    return HttpResponse(open('/Users/sbelvadi/Documents/personal_workspace/deye-website/deye/deye/src/views/home.html', 'r').read())
