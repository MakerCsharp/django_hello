from django.test import TestCase
from django.http import *

# Create your tests here.
def HomePageView(request):
    return HttpRequest('Hello world');

