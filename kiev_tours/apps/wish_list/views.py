from django.shortcuts import render

def view(request):
  response = HttpResponse( 'blah' )
  response.set_cookie( 'cookie_name', 'cookie_value' )
Retrieving a cookie:

def view(request):
  if request.COOKIES.has_key( 'cookie_name' ):
    value = request.COOKIES[ 'cookie_name' ]

# Create your views here.
