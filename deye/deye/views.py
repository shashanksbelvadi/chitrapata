from django.http import HttpResponse
import authentication

def authenticate():
    auth = authentication.Authentication()
    url = auth.get_auth_url()
    print url


def get_featured_images():
    authenticate()

    template_name = 'deye/index.html'
    context_object_name = ''

    return HttpResponse('Under construction!')
