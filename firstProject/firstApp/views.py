from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("Django is cool and Docker Volumes are super awesome")