from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome {0}".format(request.user.first_name))
    else:
        return HttpResponseRedirect(reverse('login'))
